# Asynchronous API Data Fetching (parsing)

This Python script demonstrates how to asynchronously fetch data from multiple APIs using the aiohttp library.

## Description

This script reads data from a CSV file containing search queries, constructs API URLs based on the search queries, and asynchronously fetches data from the corresponding APIs using aiohttp.

## Features

- Reads data from a CSV file.
- Constructs API URLs based on the data.
- Asynchronously fetches data from the APIs.
- Measures and prints the elapsed time for data fetching.

## Requirements

- Python 3.7 or higher
- aiohttp library

## Usage

1. Prepare a CSV file (`requests.csv`) containing search queries, with each query in a separate row.
2. Run the script.
3. The script will asynchronously fetch data from the APIs corresponding to the search queries.
4. The elapsed time for data fetching will be printed at the end.

## Example

Suppose `requests.csv` contains the following search queries:


Running the script will asynchronously fetch data from the following API URLs:

- `https://www.wildberries.ru/catalog/0/search.aspx?search=black%20dress`
- `https://www.wildberries.ru/catalog/0/search.aspx?search=blue%20shoes`
- `https://www.wildberries.ru/catalog/0/search.aspx?search=red%20shirt`

## Author

[Galust Petrosyan]

## License

This project is licensed under the [MIT License](LICENSE).
