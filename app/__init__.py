from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource
import csv
from datetime import datetime

def create_app():
    app = Flask(__name__)
    api = Api(app)
    
    from .routes import ArticleList, ArticleDetail, ArticleSearch

    # Defining API routes
    api.add_resource(ArticleList, '/articles')
    api.add_resource(ArticleDetail, '/articlesid')
    api.add_resource(ArticleSearch, '/search')

    @app.route('/')
    def home():
        # Renders the home.html template when accessing the root URL
        return render_template('home.html')

    return app

