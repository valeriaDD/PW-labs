from abc import ABC, abstractmethod


class TelegramApiProvider(ABC):
    @abstractmethod
    def add_command(self, name, implementation):
        pass

    @abstractmethod
    def start(self):
        pass
