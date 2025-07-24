# main.py
import json
import time
from scraper_manager import ScraperManager

def load_urls():


    return [
        "https://www.betfair.com/betting/football/vietnamese-u21/viettel-u21-v-tay-ninh-u21/e-34545523"
    ]


    # with open('league_standing_url.json', 'r') as file:
    #     data = json.load(file)
    # return data.get("thefishy", [])

    # with open('odds_urls.json', 'r') as file:
    #     data = json.load(file)
    # return data.get("oddsportal", [])

def main():
    start_time = time.time()
    urls = load_urls()  # Load URLs from the JSON file
    
    # scraper_manager = ScraperManager(scraper_name='oddsportal')  # Specify scraper to run
    # scraper_manager = ScraperManager(scraper_name='thefishy')  # Specify scraper to run
    scraper_manager = ScraperManager(scraper_name='betfair')  # Specify scraper to run
    
    for url in urls:
        scraper_manager.run_scraper(url)

    end_time = time.time()  # End timing
    total_time = end_time - start_time
    print(f"\n⏱️ Script completed in {total_time:.2f} seconds.")

if __name__ == '__main__':
    main()
