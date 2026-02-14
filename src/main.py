import argparse
import sys
import os

# Add current directory to path so imports work
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from prayer import handle_prayer_command
from fasting import handle_fasting_command
from zakat import handle_zakat_command
from scheduler import handle_sync_command
from islamic_calendar import handle_calendar_command

def main():
    parser = argparse.ArgumentParser(description="Islamic Companion CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    # Prayer
    p_parser = subparsers.add_parser('prayer')
    p_parser.add_argument('--today', action='store_true', help="Show today's prayer times")
    p_parser.add_argument('--sync', action='store_true', help="Sync schedule to cron")
    
    # Fasting
    f_parser = subparsers.add_parser('fasting')
    f_parser.add_argument('--today', action='store_true', help="Show fasting times")
    
    # Zakat
    z_parser = subparsers.add_parser('zakat')
    z_parser.add_argument('--nisab', action='store_true', help="Show Zakat Nisab")
    z_parser.add_argument('--currency', type=str, help="Currency code (e.g., IDR)")
    
    # Calendar
    cal_parser = subparsers.add_parser('calendar')
    cal_parser.add_argument('--city', type=str, help="City name")
    cal_parser.add_argument('--country', type=str, default="Indonesia", help="Country name (default: Indonesia)")
    cal_parser.add_argument('--month', type=int, help="Month (1-12)")
    cal_parser.add_argument('--year', type=int, help="Year (e.g., 2026)")

    # Config
    c_parser = subparsers.add_parser('config')
    c_parser.add_argument('--set-loc', nargs=2, metavar=('LAT', 'LONG'), type=float, help="Set latitude and longitude")
    c_parser.add_argument('--name', type=str, help="Location name")

    args = parser.parse_args()
    
    if args.command == 'prayer':
        if args.sync:
            handle_sync_command(args)
        elif args.today:
            handle_prayer_command(args)
        else:
            p_parser.print_help()
    elif args.command == 'fasting':
        if args.today:
            handle_fasting_command(args)
        else:
            f_parser.print_help()
    elif args.command == 'zakat':
        if args.nisab:
            handle_zakat_command(args)
        else:
            z_parser.print_help()
    elif args.command == 'calendar':
        handle_calendar_command(args)
    elif args.command == 'config':
        if args.set_loc:
            from api import load_config, CONFIG_PATH
            import json
            config = load_config()
            config['location']['latitude'] = args.set_loc[0]
            config['location']['longitude'] = args.set_loc[1]
            if args.name:
                config['location']['name'] = args.name
            
            with open(CONFIG_PATH, 'w') as f:
                json.dump(config, f, indent=2)
            print(f"Location updated to {args.name or 'custom coordinates'}: {args.set_loc}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
