# z1
z1_f = open("l4z1.txt", "w")
z1r = [x * 2 for x in range(0, 31)]
z1_f.write(str(z1r))
z1_f.close()

# z2
z2_f = open("l4z1.txt", "r")
print(z2_f.read())
z2_f.close()

# z3
with open("l4z3.txt", "w") as z3_f:
    z3_f.write("linia 1\n")
    z3_f.write("linia 2\n")
    z3_f.write("linia 3\n")


# z4
class NaZakupy:

    def __init__(self, n, i, j, c):
        self.nazwa_produktu = n
        self.ilosc = i
        self.jednostka_miary = j
        self.cena_jed = c

    def wyświetl_produkt(self):
        print(
            self.nazwa_produktu + ": " + str(self.ilosc) + " " + self.jednostka_miary + " [" + str(self.cena_jed) + "]")

    def ile_produktu(self):
        return str(self.ilosc) + " " + self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed


# z5
class CiagArytm:
    def __init__(self):
        self.a1 = None
        self.r = None
        self.n = None
        self.elementy = [] #???????????
                           # o co chodzi w zadaniu ?????

    def pobierz_parametry(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n

    def policz_sume(self):
        a = 0
        for x in self.elementy:
            a += x
        return a        #????????????

    def pobierz_elementy(self, elementy):
        self.elementy = elementy # co ja dokładnie mam z nimi zrobić?


#z6
class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz(self, x, y):
        self.x += x*self.krok
        self.y += y*self.krok

    def idz_w_gore(self, ile_krokow):
        self.idz(0,ile_krokow)

    def idz_w_dol(self, ile_krokow):
        self.idz(0, -ile_krokow)

    def idz_w_lewo(self, ile_krokow):
        self.idz(-ile_krokow, 0)

    def idz_w_prawo(self, ile_krokow):
        self.idz(ile_krokow, 0)

    def pokaz_gdzie_jestes(self):
        print(str(self.x) + ", " + str(self.y))

z6 = Robaczek(0,0,1)
z6.idz_w_gore(1)
z6.idz_w_lewo(1)
z6.idz_w_prawo(2)
z6.idz_w_dol(3)
z6.pokaz_gdzie_jestes()