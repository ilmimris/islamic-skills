---
name: islamic-companion
description: Unified Islamic utilities for prayer times, fasting schedules, and Zakat calculations using a shared configuration.
---

# Islamic Companion Skill

**Unified tool for prayer times, fasting schedules, and Zakat calculations.**

This skill consolidates Islamic utilities into a single CLI with shared configuration and efficient caching.

## Features

- **Prayer Times:** Retrieve daily prayer times (Fajr, Dhuhr, Asr, Maghrib, Isha).
- **Fasting:** Check Imsak and Maghrib times for fasting.
- **Zakat:** Calculate Nisab thresholds for Gold and Silver based on current market prices.
- **Quran:** Search for verses by keyword or fetch specific Surah/Ayah with translation.
- **Calendar:** Generate a monthly prayer schedule for any city.
- **Quotes:** Fetch and display random Islamic quotes or setup daily automation.
- **Scheduler:** Generate OpenClaw cron commands to schedule daily prayer reminders.
- **Caching:** Minimizes API calls by caching daily results locally.

## Usage

Run the CLI using python:

```bash
# Get today's prayer times
python3 -m skills.islamic_companion.src.main prayer --today

# Setup daily quote automation
python3 -m skills.islamic_companion.src.main quotes --setup

# Get a random quote
python3 -m skills.islamic_companion.src.main quotes --random

# Get monthly calendar (Example: Serang, Banten)
python3 -m skills.islamic_companion.src.main calendar --city "Serang" --month 2 --year 2026

# Sync prayer schedule to cron (generates commands)
python3 -m skills.islamic_companion.src.main prayer --sync

# Check fasting times (Imsak/Maghrib)
python3 -m skills.islamic_companion.src.main fasting --today

# Check Zakat Nisab values
python3 -m skills.islamic_companion.src.main zakat --nisab

# Search Quran for keyword
python3 -m skills.islamic_companion.src.main quran --search "sabar"

# Get specific Surah (e.g., Al-Fatihah)
python3 -m skills.islamic_companion.src.main quran --surah 1

# Get specific Ayah (e.g., Al-Baqarah:255)
python3 -m skills.islamic_companion.src.main quran --surah 2 --ayah 255
```

## Configuration

Edit `skills/islamic-companion/config.json` to set your location and calculation method.

```json
{
  "location": {
    "latitude": -6.2088,
    "longitude": 106.8456,
    "name": "Jakarta"
  },
  "calculation": {
    "method": 20,
    "school": 1
  },
  "zakat": {
    "currency": "IDR",
    "gold_gram_threshold": 85,
    "api_key": ""
  },
  "quran_language": "id"
}
```

### Calculation Methods
- **Method 20:** Kemenag RI (Indonesia)
- **School 1:** Standard (Shafi, Maliki, Hanbali)
- **School 2:** Hanafi

## Intent Mappings (for Agent)

| User Intent | Command Executed |
| :--- | :--- |
| "Get prayer times" | `python3 -m skills.islamic_companion.src.main prayer --today` |
| "Show me the calendar for [City]" | `python3 -m skills.islamic_companion.src.main calendar --city [City]` |
| "Setup daily Islamic quotes" | `python3 -m skills.islamic_companion.src.main quotes --setup` |
| "Give me a random Islamic quote" | `python3 -m skills.islamic_companion.src.main quotes --random` |
| "Sync prayer schedule" | `python3 -m skills.islamic_companion.src.main prayer --sync` |
| "When is Imsak?" | `python3 -m skills.islamic_companion.src.main fasting --today` |
| "Check Zakat Nisab" | `python3 -m skills.islamic_companion.src.main zakat --nisab` |
| "Search Quran for [keyword]" | `python3 -m skills.islamic_companion.src.main quran --search "[keyword]"` |
| "Read Surah [Name/Number]" | `python3 -m skills.islamic_companion.src.main quran --surah [Number]` |
| "Read Surah [Number] Ayah [Number]" | `python3 -m skills.islamic_companion.src.main quran --surah [Number] --ayah [Number]` |

## Dependencies

- `requests`
