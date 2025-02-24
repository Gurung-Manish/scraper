from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Function to fetch the page content using Selenium (for dynamic content)
def get_fishy_page_content_selenium(url):
    options = Options()
    options.headless = True  # Run Chrome in headless mode (without UI)
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(5)  # Wait for the page to load (adjust this sleep if needed)

    page_content = driver.page_source
    driver.quit()  # Close the browser after fetching the page

    return page_content

def parse_fishy_league_standing_data(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    standings_data = []

    # Find the rows of the table excluding the header row
    rows = soup.find_all('tr', class_='cats2')
    
    for row in rows:
        cols = row.find_all('td')

        if len(cols) >= 19:  # Ensure there are enough columns
            position = cols[0].text.strip()
            team_name = cols[1].find('a').text.strip()  # Extract team name from anchor tag
            played = cols[2].text.strip()
            wins = cols[13].text.strip()
            draws = cols[14].text.strip()
            losses = cols[15].text.strip()
            goals_for = cols[6].text.strip()
            goals_against = cols[7].text.strip()
            goal_difference = cols[18].text.strip()
            points = cols[19].text.strip()

            standings_data.append({
                'Position': position,
                'Team': team_name,
                'Played': played,
                'Wins': wins,
                'Draws': draws,
                'Losses': losses,
                'Goals For': goals_for,
                'Goals Against': goals_against,
                'Goal Difference': goal_difference,
                'Points': points
            })

    return standings_data
