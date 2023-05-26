from newsapi import NewsApiClient

from services.news.NewsParser import NewsParser
from services.news.NewsApiProvider import NewsApiProvider


class NewsApiAdapter(NewsApiProvider):
    def __init__(self, api_key):
        self.news_parser = NewsParser()
        self.newsapi = NewsApiClient(api_key=api_key)

    def get_news(self, topic=None):
        response = self.newsapi.get_top_headlines(page_size=5, language="en", q=topic)
        print(response)

        if response['status'] != 'ok':
            raise Exception("Something went wrong...")

        if response['totalResults'] == 0:
            raise FileNotFoundError("No results found...")

        return self.news_parser.parse_response(response)

