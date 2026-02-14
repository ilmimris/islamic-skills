import os
import json
import time
import requests
from datetime import datetime

CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cache')
CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config.json')

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def get_cache_path(date_str):
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    return os.path.join(CACHE_DIR, f"{date_str}.json")

def fetch_data(endpoint, params):
    # Construct a cache key based on params to avoid collisions if params change
    today = datetime.now().strftime("%Y-%m-%d")
    cache_file = get_cache_path(f"{endpoint.replace('/', '_')}_{today}")

    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            return json.load(f)

    # Use Aladhan API
    url = f"http://api.aladhan.com{endpoint}"
    
    # Handle Zakat specially (mock for now as Aladhan doesn't support it)
    if 'zakat' in endpoint:
        # Mock data
        data = {
            "code": 200,
            "status": "OK",
            "data": {
                "gold": 1200000, # Example price in IDR/gram
                "silver": 15000,
                "currency": params.get('currency', 'IDR')
            }
        }
        with open(cache_file, 'w') as f:
            json.dump(data, f, indent=2)
        return data

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        with open(cache_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def get_prayer_times():
    config = load_config()
    params = {
        'latitude': config['location']['latitude'],
        'longitude': config['location']['longitude'],
        'method': config['calculation']['method'],
        'school': config['calculation']['school']
    }
    # Aladhan API uses DD-MM-YYYY in path
    today = datetime.now().strftime("%d-%m-%Y")
    return fetch_data(f'/v1/timings/{today}', params)

def get_fasting_times():
    # Same as prayer times for Aladhan
    return get_prayer_times()

def get_zakat_gold_silver(currency=None):
    config = load_config()
    curr = currency or config['zakat']['currency']
    return fetch_data(f'/v1/zakat/gold-silver', {'currency': curr})
