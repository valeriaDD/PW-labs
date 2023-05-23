from flask import Flask
from NewsAPI import NewsAPI
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    news_token = os.environ.get('NEWS_API_TOKEN')
    newsAPI = NewsAPI(news_token)

    return newsAPI.get_news('test')


if __name__ == "__main__":
    app.run()
