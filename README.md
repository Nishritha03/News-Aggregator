# News-Aggregator

This project is a News Aggregator  that scrapes articles from CNN and India Today, categorizes them, and serves them through a RESTful API. The API allows users to retrieve, search, and filter articles based on various criteria. The project also includes a front-end interface for displaying the articles.

## Features

- **Web Scraping**: Scrapes articles from CNN and India Today.
- **Categorization**: Categorizes articles into predefined categories like Politics, Technology, Sports, etc.
- **RESTful API**: Provides endpoints to retrieve all articles, search by ID, and filter by date and category.
- **Front-End Interface**: A simple web interface to display and search articles.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/news-aggregator.git
   cd news-aggregator
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If `requirements.txt` does not exist, manually install the required packages:*

   ```bash
   pip install requests beautifulsoup4 pandas flask flask-restful textblob
   ```

4. **Run the scraper to fetch articles and save them to a CSV file**:

   ```bash
   python webscraping.py
   ```

5. **Run the Flask application**:

   ```bash
   python app.py
   ```

6. **Access the application**:

   Open your browser and go to `http://127.0.0.1:5000/`.


## Front-End Interface

The front-end interface provides a simple way to view, search, and filter articles. Use the search form at the top of the page to filter articles by category or date.

## Testing the API with Postman

1. **Install Postman**: [Download Postman](https://www.postman.com/downloads/)
2. **Import the API collection**: You can import the API collection into Postman to test the endpoints.
3. **Test the Endpoints**: Use the API endpoints described above to test different functionalities.

## Future Enhancements

- Add support for more news sources.
- Implement user authentication and authorization.
- Enhance the front-end with more features and better UI/UX.


## Acknowledgments

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): For parsing HTML.
- [TextBlob](https://textblob.readthedocs.io/en/dev/): For natural language processing.
