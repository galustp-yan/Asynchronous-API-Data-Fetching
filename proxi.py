import requests
import csv
import time
import aiohttp
import asyncio

def read_csv_file(csv_file_path):
    """
    Read data from a CSV file and return a list of rows.

    Args:
        csv_file_path (str): The path to the CSV file.

    Returns:
        list: A list of rows read from the CSV file.
    """
    rows = []
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = [row[0] for row in csv_reader]
    return rows

def construct_api_urls(data_rows):
    """
    Construct API URLs based on the data rows.

    Args:
        data_rows (list): A list of data rows.

    Returns:
        list: A list of constructed API URLs.
    """
    urls = []
    for row in data_rows:
        words = row.split()
        api_url = "https://www.wildberries.ru/catalog/0/search.aspx?search="
        for index, word in enumerate(words):
            api_url += word if index == len(words) - 1 else word + "%20"
        urls.append(api_url)
    return urls

async def fetch_data(url):
    """
    Asynchronously fetch data from a given URL.

    Args:
        url (str): The URL to fetch data from.
    """
    global count
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            count += 1
            print(count)

async def main():
    """
    The main asynchronous function to execute tasks concurrently.
    """
    global urls

    # Create a list of tasks for each URL
    tasks = [fetch_data(url) for url in urls]

    # Execute the tasks concurrently
    await asyncio.gather(*tasks)

def main_process(csv_file_path):
    """
    The main process to read CSV file, construct API URLs, and fetch data asynchronously.

    Args:
        csv_file_path (str): The path to the CSV file.
    """
    global count
    start_time = time.time()

    # Read data from CSV file
    data_rows = read_csv_file(csv_file_path)

    # Construct API URLs
    urls = construct_api_urls(data_rows)

    # Initialize count
    count = 0

    # Run the asynchronous main function
    asyncio.run(main())

    # Record the ending time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the elapsed time
    print(f"Elapsed Time: {elapsed_time} seconds")

if __name__ == "__main__":
    csv_file_path = 'requests.csv'
    main_process(csv_file_path)
