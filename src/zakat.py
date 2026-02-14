from api import get_zakat_gold_silver, load_config

def handle_zakat_command(args):
    config = load_config()
    currency = args.currency or config['zakat']['currency']
    
    data = get_zakat_gold_silver(currency)
    if not data or 'data' not in data:
        print("Could not retrieve Zakat data.")
        return

    prices = data['data']
    # Example structure: {"gold": 1234.56, "silver": 23.45, "currency": "IDR"}
    # Nisab Gold: 85g, Silver: 595g
    
    gold_price = prices.get('gold', 0)
    silver_price = prices.get('silver', 0)
    
    gold_nisab = gold_price * 85
    silver_nisab = silver_price * 595
    
    print(f"Zakat Nisab ({currency}):")
    print(f"Gold (1g):   {gold_price:,.2f}")
    print(f"Gold Nisab (85g): {gold_nisab:,.2f}")
    print("-" * 20)
    print(f"Silver (1g): {silver_price:,.2f}")
    print(f"Silver Nisab (595g): {silver_nisab:,.2f}")
