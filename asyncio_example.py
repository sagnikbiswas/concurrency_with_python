"""
Python script to **asynchronously** download a list of websites
using **asyncio** and display the time it took to complete.
Check the .ipynb file for details.
"""

import asyncio
import time
import aiohttp

async def download_site(session, url):
    async with session.get(url) as response:
        length = response.content_length or "Some"

        # content_length is read from http header if its present
        # otherwise None is returned

        print(f"Read {length} bytes from {url}")

async def download_all_sites(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    urls = [
        "https://www.linkedin.com/in/sagnik-biswas-7740981b6/",
        "https://github.com/sagnikbiswas"
    ] * 100

    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(urls))
    # asyncio.run is causing RuntimeError('Event loop is closed') in Win10
    time_took = time.time() - start_time
    print(f"Downloaded {len(urls)} pages in {time_took} seconds")