from database import init_db
from gmail_scraper import scrape_gmail
from export_csv import export_csv
from export_excel import export_excel


def main():

    print("Initializing database...")
    init_db()

    print("Scraping Gmail...")
    scrape_gmail()

    export_csv()

    export_excel()

    print("System completed")


if __name__ == "__main__":
    main()