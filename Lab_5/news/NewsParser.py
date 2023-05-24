class NewsParser:
    @staticmethod
    def parse_response(response):
        articles = response['articles']
        result = []

        for article in articles:
            article_data = article['title'] + "\r\n\n" + article['url'] + "\r\nSource: " + article['source']['name']
            result.append(article_data)

        return result
