import requests
from bs4 import BeautifulSoup
import sys
sys.path.append("..")  # Add the parent directory to the system path
from models import EarthquakeCreate  # Import EarthquakeCreate from models.py

# Now you can use EarthquakeCreate


class Scraper:
    def __init__(self, url):
        self.url = url

    def ping(self, url=None):
        if url:
            response = requests.get(url)
        else:
            response = requests.get(self.url)

        # Check the status code of the response
        print(f"Status Code:{response.status_code}")

        return response

    def scrape_and_add(self, lines_to_skip, html_tag):
        response = self.ping()

        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.text, "html.parser")
            content = soup.find(html_tag).text.strip().split('\n')

            # Print content to check if it's what you expect
            print("Content:", content)

            # Find the index where the earthquake data begins
            data_start_index = 0
            for i, line in enumerate(content):
                data_start_index = i + lines_to_skip  # Skip the header lines
                break

            # Loop through each line of content to extract earthquake data
            for line in content[data_start_index:]:
                print("Line:", line)  # Print the content of the line
                data = line.split()
                print("Data:", data)  # Print the result of split operation

                # Create instance of EarthquakeCreate and populate it with scraped data
                if len(data) >= 6:  # Ensure there are enough elements to split
                    earthquake = EarthquakeCreate(
                        date=data[0],
                        time=data[1],
                        latitude=data[2],
                        longitude=data[3],
                        depth=data[4],
                        magnitude=data[5]
                    )
                    EarthquakeCreate(earthquake)
                else:
                    print("Data format incorrect:", line)

        else:
            print("Failed to fetch data. Status Code: ", response.status_code)

    def scrape(self, html_tag=None):
        response = self.ping()

        if response.status_code == 200:

            # Parse HTML content
            soup = BeautifulSoup(response.text, "html.parser")

            if html_tag:
                content = soup.find(html_tag).text
                print(content)
            else:
                content = soup.text
                print(content)

        else:
            print("Failed to fetch data. Status Code: ", response.status_code)


# URL of the webpage to scrape
url = 'http://www.koeri.boun.edu.tr/scripts/lst9.asp'

# Create instance of Scraper and scrape the data
scraper = Scraper(url)
scraper.scrape_and_add(3, "pre")
