#kandilli_scraper.py

import requests
from bs4 import BeautifulSoup
from database import EarthquakeCreate

# URL of the webpage to scrape
url = 'http://www.koeri.boun.edu.tr/scripts/lst9.asp'

# Make an HTTP request to the webpage
response = requests.get(url)

# Check the status code of the response
print("Status Code:", response.status_code)

# Print the response headers
print("Response Headers:", response.headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("pre")

    print(content)

else:
    print(response.status_code)


