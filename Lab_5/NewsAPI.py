from newsapi import NewsApiClient
import os


class NewsAPI:
    def __init__(self, api_key):
        self.newsapi = NewsApiClient(api_key=api_key)

    def get_news(self, topic):
        # response = self.newsapi.get_top_headlines(page_size=5, q=topic)
        # articles = response['articles']
        # result = []
        #
        # for article in articles:
        #     article_data = {
        #         'url': article['url'],
        #         'title': article['title'],
        #         'author': article['author']
        #     }
        #     result.append(article_data)
        #
        # return result
        return [{"author":"Matias Grez","title":"Carmelo Anthony, 10-time NBA All-Star and one of basketball\u2019s greatest scorers, announces retirement - CNN","url":"https://www.cnn.com/2023/05/22/sport/carmelo-anthony-announces-retirement-spt-intl/index.html"},{"author":"HT News Desk","title":"Army deployed as fresh violence erupts in Manipur, houses set on fire in Imphal - Hindustan Times","url":"https://www.hindustantimes.com/india-news/fresh-manipur-violence-abandoned-houses-set-on-fire-in-imphal-curfew-army-101684755288846.html"},{"author":"South China Morning Post","title":"Protests over nukes as G7 leaders talk Ukraine and China in Hiroshima - South China Morning Post","url":"https://news.google.com/rss/articles/CCAiC3A0WTVVUnUzQ2NvmAEB?oc=5"},{"author":"By  WALLA! HEALTH","title":"These daily habits can impact your gut health - The Jerusalem Post","url":"https://www.jpost.com/health-and-wellness/article-743704"}]
