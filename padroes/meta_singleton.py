"""Neste exemplo implementei o padrão Singleton como MetaClasse"""
"""Link para mais informações sobre metaclasses: https://pt.wikipedia.org/wiki/Metaclasse"""


class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
