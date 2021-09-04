"""
Python script to **synchronously** download a list of websites 
and display the time it took to complete.
Check the .ipynb file for details.
"""

import requests
import time

def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} bytes from {url}")

# Using Session to maintain a session with the site and speed things up

def download_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            download_site(url, session)

if __name__ == "__main__":
    urls = [
        "https://www.linkedin.com/in/sagnik-biswas-7740981b6/",
        "https://github.com/sagnikbiswas"
    ] * 100

    start_time = time.time()
    download_all_sites(urls)
    time_took = time.time() - start_time
    print(f"Downloaded {len(urls)} pages in {time_took} seconds")
