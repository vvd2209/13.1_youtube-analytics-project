# -*- coding: utf-8 -*-
import os
from googleapiclient.discovery import build

class APIMixin:
    """
    Миксин, который отдельно отвечает за подключение к API
    """
    __API_KEY = os.getenv('YT_API_KEY')
    @classmethod
    def get_service(cls):
        service = build('youtube', 'v3', developerKey=cls.__API_KEY)
        return service