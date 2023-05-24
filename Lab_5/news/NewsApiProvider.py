from abc import ABC, abstractmethod


class NewsApiProvider(ABC):
    @abstractmethod
    def get_news(self, topic=None):
        pass
