import argparse
from modules import social_media, domain_info, email_lookup, phone_lookup, data_breach
from reports import report_generator

def main():
    parser = argparse.ArgumentParser(description='OSINT Tool')
    parser.add_argument('--target', required=True, help='Target for OSINT investigation')
    parser.add_argument('--report', required=True, help='Output report file')
    args = parser.parse_args()

    data = {
        'social_media': social_media.gather_info(args.target),
        'domain_info': domain_info.lookup(args.target),
        'email_lookup': email_lookup.lookup(args.target),
        'phone_lookup': phone_lookup.lookup(args.target),
        'data_breach': data_breach.get_breaches(args.target)
    }

    report_generator.generate_report(args.report, data)

if __name__ == "__main__":
    main()
