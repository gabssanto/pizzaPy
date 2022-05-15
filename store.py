from html.entities import html5
import pathlib

class Store: 
    _instance = None
    counter = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Store, cls).__new__(cls)
        return cls._instance