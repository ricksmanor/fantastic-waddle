import pandas as pd
from trustpilot_scraper.scraper import scrape_trustpilot_reviews

def main():
    base_url = 'https://uk.trustpilot.com/review/ukstoragecompany.co.uk'
    print("Scraping Trustpilot reviews...")
    reviews = scrape_trustpilot_reviews(base_url)

    if not reviews:
        print("No reviews found.")
        return

    df = pd.DataFrame(reviews)
    df.to_excel("data.xlsx", index=False)
    print(f"Exported {len(df)} reviews to data.xlsx")

if __name__ == "__main__":
    main()
