"""
Python script to **asynchronously** download a list of websites
using **multithreading** and display the time it took to complete.
Check the .ipynb file for details.
"""

import concurrent.futures
import threading

import requests
import time


thread_local = threading.local()

# Session object is NOT thread-safe. 
# Each thread requires its own session.

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} bytes from {url}")

def download_all_sites(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(download_site, urls)

if __name__ == "__main__":
    urls = [
        "https://www.linkedin.com/in/sagnik-biswas-7740981b6/",
        "https://github.com/sagnikbiswas"
    ] * 100

    start_time = time.time()
    download_all_sites(urls)
    time_took = time.time() - start_time
    print(f"Downloaded {len(urls)} pages in {time_took} seconds")

        