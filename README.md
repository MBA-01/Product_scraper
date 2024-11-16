# E-commerce Product Scraper

## Description
This project is a web scraping tool designed to extract product information from e-commerce websites. It works by first fetching product links from a website's sitemap and then scraping detailed product information including titles, prices, descriptions, and images from each product page.

## Features
- Extracts product links from website sitemaps using robots.txt
- Scrapes product details including:
  - Product titles
  - Prices (with currency detection)
  - Product descriptions
  - Product images
- Saves data in JSON format
- Includes logging for debugging and monitoring
- Handles multiple websites
- UTF-8 encoding support

## Technologies Used
- Python 3.x
- BeautifulSoup4 for HTML parsing
- Requests for HTTP requests
- Pandas for data handling
- XML parsing with ElementTree

## Dependencies

python : """

requirements.txt :
    requests==2.31.0
    beautifulsoup4==4.12.0
    pandas==2.1.0
    logging==0.5.1.2
    urllib3==2.0.7
"""

## Project Structure
  
Product_scraper/    
├── main.py # Main execution script  
├── fetch_product_links.py # Script to fetch product URLs from sitemaps  
├── extract_product_info.py # Script to extract product details  
├── utils/  
│ ├── robots.py # Utilities for robots.txt handling  
│ └── sitemap.py # Utilities for sitemap parsing  
├── config/  
│ └── websites.py # Website configuration  
└── data/ # Directory for storing JSON output files  
  


## Installation
1. Clone the repository:
   bash: """
    git clone (repository-url)
   """

2. Install required dependencies:
   bash: """
    pip install -r requirements.txt
   """

## Usage
Run the scraper by executing the main script with a target website URL:

python main.py "https://example.com" "example.com"



The scraper will:
1. Fetch the sitemap URL from robots.txt
2. Extract product links from the sitemap
3. Scrape product information from each link
4. Save the results in JSON format in the data directory

## Output
The scraper generates two types of JSON files in the data directory:
- `domain_product_data.json`: Contains all product URLs found in the sitemap
- `domain_product_info_details.json`: Contains detailed product information for each URL

## Error Handling
- The scraper includes comprehensive error handling and logging
- Failed requests are logged with appropriate error messages
- Missing data fields are marked as "Not found"

## Limitations
- Requires websites to have a robots.txt file and sitemap
- Website structure must be consistent with common e-commerce patterns
- Rate limiting may be required for large websites

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
