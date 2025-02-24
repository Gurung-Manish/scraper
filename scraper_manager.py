from oddsportal.oddsportal_scraper.oddsportal_scraper import get_page_content_selenium, parse_match_data
from utils import save_to_csv
import re

class ScraperManager:
    def __init__(self, scraper_name):
        self.scraper_name = scraper_name
    
    def run_scraper(self, url):
        if self.scraper_name == 'oddsportal':
            return self._run_oddsportal_scraper(url)
        elif self.scraper_name == 'bet365':
            return self._run_bet365_scraper(url)
        else:
            raise ValueError("Unsupported scraper name")
    
    def _run_oddsportal_scraper(self, url):
        page_content = get_page_content_selenium(url)
        match_data = parse_match_data(page_content)
        
        # Generate a dynamic filename based on the URL (e.g., using the league name)
        filename = self._generate_filename_from_url(url)
        
        save_to_csv(match_data, scraper_name="oddsportal", filename=filename)
    
    def _generate_filename_from_url(self, url):
        # Extract the country and league name from the URL
        match = re.search(r'football/([^/]+)/([^/]+)/', url)
        if match:
            country, league = match.groups()
            # Clean and format the filename
            country = country.replace('-', '_')
            league = league.replace('-', '_')
            filename = f"{country}_{league}_matches.csv"
        else:
            filename = "unknown_league_matches.csv"

        return filename
    
  
