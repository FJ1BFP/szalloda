class Szalloda:

    def __init__(self, nev, szobak):
        self.nev = nev
        self.szobak = szobak

    def __str__(self):
        return f'A szalloda neve {self.nev} a szobak szama {len(self.szobak)}'

    def printszobak(self):

        for i in range(0, len(self.szobak)):
            print(self.szobak[i])