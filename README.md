# Islamic Companion Skill

A unified Islamic utility suite for OpenClaw agents. Manage prayer times, fasting schedules, and Zakat calculations from a single, cohesive interface.

## Features

-   **Prayer Times:** Accurate daily schedules (Fajr, Dhuhr, Asr, Maghrib, Isha) via Aladhan API.
-   **Smart Scheduler:** Auto-syncs daily prayer reminders to your agent's system cron.
-   **Fasting Info:** Imsak and Maghrib times for fasting.
-   **Zakat Calculator:** Check Nisab thresholds for Gold and Silver based on live market data.
-   **Unified Config:** Set location and calculation method once for all tools.

## Installation

Install via the skills CLI:

```bash
npx skills add ilmimris/islamic-skills
```

Or install manually:

```bash
cd skills
git clone https://github.com/ilmimris/islamic-skills.git islamic-companion
pip install -r islamic-companion/requirements.txt
```

## Configuration

The skill uses `config.json` for settings.

When first run, it will automatically copy `config.example.json` to `config.json` with default values (Jakarta).

### Update Location
You can update your location via the CLI:
```bash
python3 src/main.py config --set-loc -6.2088 106.8456 --name "Jakarta"
```

### Setup API Key (Zakat)
To get live Zakat data, get a free API key from [IslamicAPI.com](https://islamicapi.com) and add it to `config.json`:

```json
"zakat": {
    "api_key": "YOUR_API_KEY_HERE"
}
```

## Usage

The skill exposes a unified CLI `src/main.py` that your agent calls.

### Chat Examples (Onboarding)

Once installed, you can talk to your agent naturally:

> **User:** "Set my location to Jakarta"
> **Agent:** *Updates config to Jakarta coordinates*

> **User:** "Sync my prayer times"
> **Agent:** *Schedules daily prayer reminders via cron*

> **User:** "When is Maghrib?"
> **Agent:** *Checks today's schedule and replies*

> **User:** "Check Zakat Nisab"
> **Agent:** *Fetches current gold price and calculates threshold*

### CLI Reference

If you need to run it manually or debug:

#### Prayer Times
```bash
# Get today's schedule
python3 src/main.py prayer --today

# Sync reminders to OpenClaw cron
python3 src/main.py prayer --sync
```

### Fasting
```bash
# Check Imsak/Iftar times
python3 src/main.py fasting --today
```

### Zakat
```bash
# Check current Nisab thresholds
python3 src/main.py zakat --nisab --currency IDR
```

## License

MIT
