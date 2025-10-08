import argparse
from cleaner import clean_data
from db_handler import upload_to_mysql
from exporter import export_csv

def main():
    parser = argparse.ArgumentParser(description="Data Cleaning CLI Tool")
    parser.add_argument('--input', required=True, help="Path to input CSV file")
    parser.add_argument('--output', required=False, help="Path to save cleaned CSV")
    parser.add_argument('--upload', action='store_true', help="Upload cleaned data to MySQL")
    
    args = parser.parse_args()
    
    df = clean_data(args.input)
    if args.upload:
        upload_to_mysql(df, table_name='cleaned_data')
    if args.output:
        export_csv(df, args.output)

if __name__ == "__main__":
    main()
