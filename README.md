# News-Aggregator

This project is a News Aggregator  that scrapes articles from CNN and India Today, categorizes them, and serves them through a RESTful API. The API allows users to retrieve, search, and filter articles based on various criteria. The project also includes a front-end interface for displaying the articles.

## Features

This project involves web scraping articles from CNN and India Today , followed by categorizing them into predefined categories such as Politics, Technology, and Sports. 
It includes a RESTful API that offers endpoints to retrieve all articles, search by ID, and filter them based on date and category. 
Additionally, there is a simple front-end interface that allows users to display and search through the articles efficiently.

##Note:The WebScraping for this project is done in the Jupyter Notebook
    
    
    ----------------------------------------------------------------------------------------
## Installation

### Setup For webscraping in the jupyter:
1.**Installation**
`!pip install requests bs4  pandas`

### Setup For Backend In the Vscode:
2.**Installation**
`pip install Flask Flask-RESTful Jinja2`

3. **Run the Flask application**:

   ```bash
   python app.py
   ```

6. **Access the application**:

   Open your browser and go to `http://127.0.0.1:5000/`.


## Front-End Interface

The front-end interface provides a simple way to view, search, and filter articles. Use the search form at the top of the page to filter articles by category or date.

## Testing the API with Postman

1. **Install Postman**
2.**defining the routes in the routes.py**
3. **Testing the endpoints through the URL and retriving the data**

## ScreenShots Of API
![image](https://github.com/user-attachments/assets/c1fe83c0-8a8d-478a-9dde-2c98937d6cf2)
![image](https://github.com/user-attachments/assets/7ce5fb5c-c6bd-420d-91d6-310614f0b580)
![image](https://github.com/user-attachments/assets/a131c0c3-109f-449b-953c-6c0b052bdebd)




## Future Enhancements

- Enhance the search Functionality
- Implement user authentication and authorization.
- Enhance the front-end with more features and better UI/UX.


## Acknowledgments

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): For parsing HTML.
- [TextBlob](https://textblob.readthedocs.io/en/dev/): For natural language processing.
