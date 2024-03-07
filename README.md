
# Job Scraper for REED with Scrapy

Welcome to Job Scraper! This project is designed to scrape job listings from reed  using Scrapy, a powerful web crawling and scraping framework for Python.




## Installation Guide

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd jobscraper_scrapy
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```







## Usage

Once you've installed the dependencies, you can run the Scrapy spiders to start scraping job listings. To do this, execute the following command from the project directory:
```bash
  spider crawl <spider_name>
```


Replace `<spider_name>` with the name of the spider you want to run. You can find the available spiders in the `spiders` directory.

## Different Output Formats

By default, scraped data will be saved in JSON format. However, you can specify a different output file format using the `-o` option. For example, to save the scraped data in CSV format, you can use the following command:
```bash
scrapy crawl <spider_name> -o output.csv
```
Supported output formats include JSON, CSV, XML, and JSON Lines. 
