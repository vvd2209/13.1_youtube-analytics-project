# -*- coding: utf-8 -*-
import json
from src.APIMixin import APIMixin

def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

class Channel(APIMixin):
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = Channel.youtube.channels().list(id=self.__channel_id, part='snippet, statistics').execute()
        self.title = self.channel.get('items')[0].get('snippet').get('title')
        self.description = self.channel.get('items')[0].get('snippet').get('description')
        self.url = 'https://www.youtube.com/' + self.channel.get('items')[0].get('snippet').get('customUrl')
        self.subscriberCount = int(self.channel.get('items')[0].get('statistics').get('subscriberCount'))
        self.video_count = self.channel.get('items')[0].get('statistics').get('videoCount')
        self.viewCount = self.channel.get('items')[0].get('statistics').get('viewCount')

    def __str__(self):
        """ Возвращает название и ссылку на канал"""
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        """Складывает количество подписчиков двух каналов"""
        return self.subscriberCount + other.subscriberCount

    def __sub__(self, other):
        """Вычитает количество подписчиков двух каналов"""
        return self.subscriberCount - other.subscriberCount

    def __gt__(self, other):
        """Сравнивает, где больше подписчиков двух каналов"""
        return self.subscriberCount > other.subscriberCount

    def __ge__(self, other):
        """Сравнивает, где больше или равно подписчиков двух каналов"""
        return self.subscriberCount >= other.subscriberCount

    def __lt__(self, other):
        """Сравнивает, где меньше подписчиков двух каналов"""
        return self.subscriberCount < other.subscriberCount

    def __le__(self, other):
        """Сравнивает, где меньше или равно подписчиков двух каналов"""
        return self.subscriberCount <= other.subscriberCount


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        printj(channel)

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube


    def to_json(self, filename):
        """Сохраняет в файл значения атрибутов экземпляра `Channel`. Два способа реализации"""
        # Способ 1
        # data = self.__dict__
        # with open(filename, 'w', encoding='utf-8') as f:
        #     f.write(json.dumps(data, ensure_ascii=False))

        # Способ 2
        data = {
            'ID Chanel': self.__channel_id,
            'Name': self.title,
            'Description': self.description,
            'URL': self.url,
            'Count of subscriber': self.subscriberCount,
            'Count of video': self.video_count,
            'Count of view': self.viewCount,
        }
        with open(filename, 'w', encoding='utf-8') as f:
             f.write(json.dumps(data))