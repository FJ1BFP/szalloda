from szoba import Szoba


class Ketagyas_Szoba(Szoba):
    def __init__(self, ar, szoba_szam, agyak_szama):
        super().__init__(ar, szoba_szam)
        self.agyak_szama = agyak_szama

    def __str__(self):
        return f'A szoba ára {self.ar} a szoba száma {self.szoba_szam} az ágyak száma {self.agyak_szama}'