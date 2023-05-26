from abc import ABC, abstractmethod


class TelegramApiInterface(ABC):
    @abstractmethod
    def add_command(self, name, implementation):
        pass

    @abstractmethod
    def process_update(self, update):
        pass
