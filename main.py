from egyágyas_szoba import Egyagyas_Szoba
from foglalás import Foglalas
from kétágyas_szoba import Ketagyas_Szoba
from szálloda import Szalloda

szoba = Egyagyas_Szoba(10000, 1, 1)
szoba2 = Ketagyas_Szoba(20000, 2, 2)
szoba3 = Ketagyas_Szoba(20000, 3, 2)
szobak = (szoba, szoba2, szoba3)
szalloda = Szalloda("hotel", szobak)

foglalas = Foglalas(szalloda)

foglalas.ujfoglalas(1,"test",2025,5,6)
foglalas.ujfoglalas(2,"test",2025,5,6)
foglalas.ujfoglalas(3,"test",2025,5,6)
foglalas.ujfoglalas(1,"test",2025,5,12)
foglalas.ujfoglalas(2,"test",2025,7,6)

def main():
    interfesz = int(input(" kérem adja meg mit szeretne(egyes szoba egy ágyas, kettes és hármas két ágyas :\n 1 gomb: foglalás\n 2 gomb: lemondás\n 3 gomb: foglalások listázása\n 4 gomb: kilépés\n "))
    while True:
        if interfesz == 1:
            szoba_szam = int(input("kérem adja meg a szoba számát "))
            felhasznalo_neve = input("kérem adja meg a felhasználó nevét ")
            év = int(input("kérem adja meg a dátumot év: "))
            hónap = int(input("hónap: "))
            nap = int(input("nap: "))
            szoba_ara = foglalas.ujfoglalas(szoba_szam, felhasznalo_neve, év, hónap, nap)
            if szoba_ara != None:
                print(f"Foglalás sikeres volt.A szoba ára: {szoba_ara}Ft")
            interfesz = int(input(" kérem adja meg mit szeretne:\n 1 gomb: foglalás\n 2 gomb: lemondás\n 3 gomb: foglalások listázása\n 4 gomb: kilépés\n "))
            continue
        if interfesz == 2:
            szoba_szam = int(input("kérem adja meg a szoba számát "))
            felhasznalo_neve = input("kérem adja meg a felhasználó nevét ")
            év = int(input("kérem adja meg a dátumot év: "))
            hónap = int(input("hónap: "))
            nap = int(input("nap: "))
            foglalas.lemondas(szoba_szam, felhasznalo_neve, év, hónap, nap)
            interfesz = int(input(" kérem adja meg mit szeretne:\n 1 gomb: foglalás\n 2 gomb: lemondás\n 3 gomb: foglalások listázása\n 4 gomb: kilépés\n "))
            continue
        if interfesz == 3:
            foglalas.listazas()
            interfesz = int(input(" kérem adja meg mit szeretne:\n 1 gomb: foglalás\n 2 gomb: lemondás\n 3 gomb: foglalások listázása\n 4 gomb: kilépés\n "))
            continue
        if interfesz == 4:
            break
        else:
            print("kérem a megadott parancsokat használja.")
            interfesz = int(input(" kérem adja meg mit szeretne:\n 1 gomb: foglalás\n 2 gomb: lemondás\n 3 gomb: foglalások listázása\n 4 gomb: kilépés\n "))

main()