from newsapi import NewsApiClient

from news.NewsParser import NewsParser
from news.NewsApiProvider import NewsApiProvider


class NewsApiAdapter(NewsApiProvider):
    def __init__(self, api_key):
        self.news_parser = NewsParser()
        self.newsapi = NewsApiClient(api_key=api_key)

    def get_news(self, topic=None):
        # if topic is not None:
        #     response = self.newsapi.get_top_headlines(page_size=5, language='en', q=topic)
        # else:
        #     response = self.newsapi.get_top_headlines(page_size=5, language='en')
        #
        # if response:
        #     return self.news_parser.parse_response(response)
        #
        # return 'Something went wrong...'

        return self.news_parser.parse_response(
            {'status': 'ok', 'totalResults': 128, 'articles': [
                {'source': {'id': 'techcrunch', 'name': 'TechCrunch'}, 'author': 'Sarah Perez',
                 'title': 'Netflix begins its password sharing crackdown in the U.S. - TechCrunch',
                 'description': "Netflix's crackdown on password sharing is now beginning to roll out to U.S. subscribers and other global markets, after a delayed launch.",
                 'url': 'https://techcrunch.com/2023/05/23/netflix-begins-its-password-sharing-crackdown-in-the-u-s/',
                 'urlToImage': 'https://techcrunch.com/wp-content/uploads/2023/02/GettyImages-1240099721.jpeg?resize=1200,800',
                 'publishedAt': '2023-05-23T20:26:15Z',
                 'content': 'Netflix’s crackdown on password sharing is now beginning to roll out to U.S. subscribers and other global markets, after a delayed launch. The streamer had originally planned to introduce “paid shari… [+3980 chars]'},
                {'source': {'id': None, 'name': 'Sporting News'}, 'author': None,
                 'title': '古橋亨梧、リーグ年間最優秀選手賞を受賞！セルティック2年目で今季個人タイトル3冠達成 - Goal.com',
                 'description': 'Get all the latest Soccer news, highlights, scores, schedules, standings and more from Sporting News Canada.',
                 'url': 'https://www.sportingnews.com/ca/soccer',
                 'urlToImage': 'https://static.sportingnews.com/1.30.0.9/themes/custom/tsn/logo.jpg',
                 'publishedAt': '2023-05-23T20:20:00Z', 'content': None},
                {'source': {'id': 'associated-press', 'name': 'Associated Press'}, 'author': 'Lindsay Whitehurst',
                 'title': 'Teen accused of deliberately crashing U-Haul truck into security barrier at park near White House - The Associated Press',
                 'description': "WASHINGTON (AP) — A Missouri man rented a U-Haul truck Monday evening and then crashed it into a security barrier across from the White House just a few hours later, authorities said Tuesday.  The box truck's driver smashed into the barrier near the north sid…",
                 'url': 'https://apnews.com/article/white-house-uhaul-truck-crash-lafayette-square-dcd72befb2653d62c4e7c874cc0bfeb5',
                 'urlToImage': 'https://storage.googleapis.com/afs-prod/media/62b888e1a1b6403c84ad1d138e99e52b/3000.jpeg',
                 'publishedAt': '2023-05-23T19:47:02Z',
                 'content': 'WASHINGTON (AP) A Missouri man rented a U-Haul truck Monday evening and then crashed it into a security barrier across from the White House just a few hours later, authorities said Tuesday. \r\nThe box… [+3822 chars]'},
                {'source': {'id': None, 'name': 'Neurosciencenews.com'}, 'author': 'Neuroscience News',
                 'title': 'Reduced Oxygen Intake Linked to Extended Lifespan - Neuroscience News',
                 'description': None, 'url': 'https://neurosciencenews.com/oxygen-reduction-longevity-23320/',
                 'urlToImage': None, 'publishedAt': '2023-05-23T19:15:21Z', 'content': None},
                {'source': {'id': None, 'name': 'ThePrint'}, 'author': 'ANI',
                 'title': 'NASA scientists make observation of a polar cyclone on Uranus - ThePrint',
                 'description': 'Washington [US], May 24 (ANI): National Aeronautics and Space Administration (NASA) has announced that their scientists have evidence of a polar cyclone on Uranus. The announcement was made after examining radio waves emitted from the ice giant. The findings …',
                 'url': 'https://theprint.in/world/nasa-scientists-make-observation-of-a-polar-cyclone-on-uranus/1591115/',
                 'urlToImage': None, 'publishedAt': '2023-05-23T19:13:25Z',
                 'content': 'Washington [US], May 24 (ANI): National Aeronautics and Space Administration (NASA) has announced that their scientists have evidence of a polar cyclone on Uranus. The announcement was made after exa… [+2111 chars]'}]}
        )
