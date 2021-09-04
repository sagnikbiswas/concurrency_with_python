"""
Python script to **parallelly** download a list of websites
using **multiprocessing** and display the time it took to complete.
Check the .ipynb file for details.
"""

import multiprocessing
import requests
import time

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}: Read {len(response.content)} bytes from {url}")


def download_all_sites(urls):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, urls)

if __name__ == "__main__":
    urls = [
        "https://www.linkedin.com/in/sagnik-biswas-7740981b6/",
        "https://github.com/sagnikbiswas"
    ] * 50

    start_time = time.time()
    download_all_sites(urls)
    time_took = time.time() - start_time
    print(f"Downloaded {len(urls)} in {time_took} seconds")