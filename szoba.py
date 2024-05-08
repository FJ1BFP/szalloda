from abc import ABC


class Szoba(ABC):

    def __init__(self, ar, szoba_szam):
        self.ar = ar
        self.szoba_szam = szoba_szam

    def __str__(self):
        return f'A szoba ára {self.ar} a szoba száma {self.szoba_szam}'