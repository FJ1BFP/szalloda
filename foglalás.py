from datetime import date
from szoba import Szoba


class Foglalas:
    fogalasok_lista = []


    def __init__(self, szalloda):
        self.szalloda = szalloda

    def ujfoglalas(self, szoba_szam, vendeg_neve, év, hónap, nap):
        szoba = Szoba(0,0)
        if év != 0 and hónap != 0 and hónap < 13 and nap != 0 and nap < 31:
            foglalas_datum = date(év, hónap, nap)
            for i in range(0, len(self.szalloda.szobak)):
                if self.szalloda.szobak[i].szoba_szam == szoba_szam:
                    szoba = self.szalloda.szobak[i]

            if [szoba, vendeg_neve, foglalas_datum] not in self.fogalasok_lista and foglalas_datum >= date.today():
                self.fogalasok_lista.append([szoba, vendeg_neve, foglalas_datum])
                return szoba.ar

            else:
                print("ez a foglaló már létezik kérem adjon meg egy másik szobát vagy dátumot")
        else:
            print("nem helyes a dátum")



    def lemondas(self, szoba_szam, vendeg_neve, év, hónap, nap):
        szoba_index = -1
        if év != 0 and hónap != 0 and hónap < 13 and nap != 0 and nap < 31:
            foglalas_datum = date(év, hónap, nap)
            for i in range(0, len(self.fogalasok_lista)):
                if szoba_szam == self.fogalasok_lista[i][0].szoba_szam and foglalas_datum == self.fogalasok_lista[i][2] and vendeg_neve == self.fogalasok_lista[i][1]:
                    self.fogalasok_lista.remove(self.fogalasok_lista[i])
                    szoba_index = i
                    #print("lemondás sikeres volt.")
                    szamlalo = 0
                    break
        if szoba_index != -1:
            print("lemondás sikeres volt.")
        else:
            print("lemondás nem volt sikeres")

        #if szamlalo == len(self.fogalasok_lista):
            #print("lemondás nem volt sikeres")
        print(f"foglalások száma: {len(self.fogalasok_lista)}")

    def listazas(self):
        for i in range(0, len(self.fogalasok_lista)):
            foglalas_lista = self.fogalasok_lista[i][2].year, self.fogalasok_lista[i][2].month, self.fogalasok_lista[i][2].day, self.fogalasok_lista[i][0].szoba_szam, self.fogalasok_lista[i][1]
            print(f"dátum: {self.fogalasok_lista[i][2].year}.{self.fogalasok_lista[i][2].month}.{self.fogalasok_lista[i][2].day}, szoba száma: {self.fogalasok_lista[i][0].szoba_szam}, felhasználo neve: {self.fogalasok_lista[i][1]}")