import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Function to fetch the page content using requests (for static pages)
def get_page_content_requests(url):
    response = requests.get(url)
    return response.text

# Function to fetch the page content using Selenium (for dynamic content)
def get_page_content_selenium(url):
    options = Options()
    options.headless = True  # Run Chrome in headless mode (without UI)
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(5)  # Wait for the page to load (adjust this sleep if needed)

    page_content = driver.page_source
    driver.quit()  # Close the browser after fetching the page

    return page_content


def parse_match_data(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
   