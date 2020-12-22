# Scraper

Web scraping tool. Scraping the first 5 pages of reviews of **McKaig Chevrolet Buick** from [Dealer Rater](https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685)  
Scraper Tool prints the 3 most positive reviews from the five pages of reviews.

### How the most positive reviews are found?

A very simple logic was applied to determine the most positive reviews. First, only reviews with five stars rating are collected and then those reviews are sorted by the length of the endorsements texts. Satisfied customers with positive reviews tend to write more. Obviously, in real scenarios, those endorsements could be assessed by AI tools. So, for the sake of simplicity, **the considered most positive reviews are those with 5 stars rating and more text**

**

## Requirements

Python version 3.9.0 - _See [https://www.python.org/downloads](https://www.python.org/downloads)_

pip3 - The Python Package Installer. Version 20.3.4 - _See [https://pip.pypa.io/en/stable/](https://pip.pypa.io/en/stable/)_

## Dependencies

Requests: <span>$ pip3 install requests</span>

BeautifulSoup: <span>pip3 install beautifulsoup4</span>

## Usage

### Run

<span>python3 scraper.py</span>

### Test

<span>python3 -m unnittest</span> to run all tests

<span>python3 -m unnittest 'test_file_name'</span> to run a specific unit test

## Logs

File <span>logs.txt</span> stores the logs of this application. In order to change the file path of logs file, the value of FILE_PATH variable needs to be changed in the <span>Logger.py</span> class**