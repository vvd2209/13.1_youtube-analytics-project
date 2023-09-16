# -*- coding: utf-8 -*-
from src.APIMixin import APIMixin

class Video(APIMixin):
    """
    Класс для видео с ютуб-канала
    """
    def __init__(self, video_id: str):
        """
        Экземпляр инициализируется по id видео. Дальше все данные будут подтягиваться по API.
        """
        try:
            self.__video_id = video_id #id видео
            self.video_response = (
                self.get_service().videos().list(id=self.__video_id, part='snippet,statistics').execute())
            self.title: str = self.video_response['items'][0]['snippet']['title'] #название видео
            self.url: str = f"https://youtu.be/{self.__video_id}" #ссылка на видео
            self.view_count: int = self.video_response['items'][0]['statistics']['viewCount'] #количество просмотров
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount'] #количество лайков
        except:
            """
            Если пользователь передал id, с которым невозможно получить данные о видео по API, 
            то у экземпляра инициализируется только свойство 'video_id', а остальные поля принимают значение 'None'
            """
            self.__video_id = video_id
            self.title: str = None
            self.url: str = None
            self.view_count: int = None
            self.like_count: int = None
    def __str__(self):
        """Возвращает название видео"""
        return self.title

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


