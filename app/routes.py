from flask_restful import Resource
from flask import request, jsonify
import csv
from datetime import datetime


def read_articles_from_csv(file_path):   # Function to read articles from a CSV file
    articles = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                articles.append({
                    'id': row['id'],
                    'title': row['title'],
                    'summary': row['summary'],
                    'publication_date': row['publication_date'],
                    'source': row['source'],
                    'url': row['url'],
                    'category': row['category']
                })
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    return articles


articles = read_articles_from_csv('news_articles.csv') #load the articles from dataset


class ArticleList(Resource):   # retrieving the list of articles with optional filters
    def get(self): 
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        category = request.args.get('category')

        
        filtered_articles = articles #filtering the articles based on the query performance
        if start_date:
            try:
                start_date = datetime.fromisoformat(start_date)
                filtered_articles = [article for article in filtered_articles if datetime.fromisoformat(article['publication_date']) >= start_date]
            except ValueError:
                return {'message': 'Invalid start_date format'}, 400

        if end_date:
            try:
                end_date = datetime.fromisoformat(end_date)
                filtered_articles = [article for article in filtered_articles if datetime.fromisoformat(article['publication_date']) <= end_date]
            except ValueError:
                return {'message': 'Invalid end_date format'}, 400

        if category:
            filtered_articles = [article for article in filtered_articles if article['category'].lower() == category.lower()]

        return jsonify(filtered_articles)   #returns the filtered articles in the json format


class ArticleDetail(Resource):    #retriving the specific article by using id
    def get(self):
        article_id = request.args.get('id')
        if not article_id:
            return {'message': 'No ID provided'}, 400

        article = next((article for article in articles if article['id'] == article_id), None)
        if article is None:
            return {'message': 'Article not found'}, 404

        return jsonify(article)


class ArticleSearch(Resource):   #searching the summary or title of the article using the keyword
    def get(self):
        keyword = request.args.get('keyword')
        if not keyword:
            return {'message': 'No keyword provided'}, 400

        search_results = [article for article in articles if keyword.lower() in article['title'].lower() or keyword.lower() in article['summary'].lower()]
        return jsonify(search_results)

