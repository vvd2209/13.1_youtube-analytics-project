# -*- coding: utf-8 -*-
from googleapiclient.discovery import build

import os

api_key: str = os.getenv('YT_API_KEY')

class Video:
    """
    Класс для видео с ютуб-канала
    """
    youtube = build('youtube', 'v3', developerKey=api_key)

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с YouTube API"""
        return cls.youtube
    def __init__(self, video_id: str):
        """
        Экземпляр инициализируется по id видео. Дальше все данные будут подтягиваться по API.
        """
        self.__video_id = video_id #id видео
        self.video_response = (
            self.get_service().videos().list(id=self.__video_id, part='snippet,statistics').execute())
        self.video_title: str = self.video_response['items'][0]['snippet']['title'] #название видео
        self.video_url: str = f"https://youtu.be/{self.__video_id}" #ссылка на видео
        self.view_count: int = self.video_response['items'][0]['statistics']['viewCount'] #количество просмотров
        self.like_count: int = self.video_response['items'][0]['statistics']['likeCount'] #количество лайков

    def __str__(self):
        """Возвращает название видео"""
        return self.video_title

class PLVideo(Video):
    """
    Класс для плейлиста видео с ютуб-канала
    """
    def __init__(self, video_id: str, playlist_id: str):
        """
        Создание экземпляра класса PLVideo. Содержит все атрибуты класса `PLVideo` и дополнительно атрибут playlist_id.
        """
        super().__init__(video_id)
        self.playlist_id = playlist_id


