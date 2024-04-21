# E-commerce Product Data Aggregator

This project is a web scraping tool developed in Python to extract product data from various e-commerce websites. The tool allows you to aggregate product information such as pricing, descriptions, availability, and more into a structured CSV format for analysis and other purposes.

## Usage

### Pre-requisites
- Python 3.x installed

- Clone the repository to your local machine:
  ```sh
  git clone https://github.com/your-username/e-comm-scraper.git
  cd e-comm-scraper
  ```
- Install the required dependencies:
  ```.sh
  pip install -r requirements.txt
  ```

### Step 1. Run the script to extract search results:
  ```.sh
  PYTHONPATH=. python bots/amazoncom/search.py shoes
  ```
Replace 'shoes' with your desired search query. The scraped data will be saved to a `csv` file in the same folder

### Step 2. Run the script to extract product details:
  ```.sh
  PYTHONPATH=. python bots/amazoncom/details.py search_results.csv
  ```
Replace 'search_results.csv' with your csv file containing product urls or pass the file generated in previous step

---
> Note: All the file names are concatenated with timestamp to prevent accidental overwriting of data
