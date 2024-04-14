# E-commerce Product Data Aggregator

This project is a web scraping tool developed in Python to extract product data from various e-commerce websites. The tool allows you to aggregate product information such as pricing, descriptions, availability, and more into a structured CSV format for analysis and other purposes.

## Usage

### Prerequisites
- Python 3.x installed

### Getting Started
1. Clone the repository to your local machine:
  ```sh
  git clone https://github.com/your-username/e-comm-scraper.git
  cd e-comm-scraper
  ```
2. Install the required dependencies:
  ```.sh
  pip install -r requirements.txt
  ```
3. Run the scraper to extract search results:
  ```.sh
  PYTHONPATH=. amazoncom/search.py shoes
  ```
> Replace "shoes" with your desired search query. The scraped data will be saved to a `csv` file in the same folder
