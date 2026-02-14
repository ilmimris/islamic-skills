import argparse
import sys
from .prayer import handle_prayer_command
from .fasting import handle_fasting_command
from .zakat import handle_zakat_command
from .scheduler import handle_sync_command

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
    
    # Config
    c_parser = subparsers.add_parser('config')
    c_parser.add_argument('--set-loc', nargs=2, metavar=('LAT', 'LONG'), help="Set latitude and longitude")

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
    elif args.command == 'config':
        # Placeholder for config logic if needed later
        print("Config update not implemented in this version. Edit config.json directly.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
