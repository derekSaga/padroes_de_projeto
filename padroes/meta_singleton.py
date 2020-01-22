"""Neste exemplo implementarei o padrão Singleton como MetaClasse"""
"""Link para mais informações sobre metaclasses: https://pt.wikipedia.org/wiki/Metaclasse"""

class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
