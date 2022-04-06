#import sys, math

#ta funkcja printuje wersję
#print(sys.version)

#a = 123
#b = 23

#d = (2+7j)
#print(type(d))

#print(d)

#h = 7
#i = 2

#i **= 2
#print(i)

#print("wynik %(z1)d - %(z2)d = %(z3)d" %{'z1': a, 'z2': b, 'z3': a-b})
#print("wynik {0:d} - {1:d} = {2:d}".format(a,b,a-b))
#jak to możliwe /// /? / ? ?/ ?/ ?? ? ?/ s

#print("wpisz liczbe a: ", end="")
#a = int(input())
#print("wpisz liczbe b: ", end="")
#b = int(input())

#if a > b:
#    print("a jest wieksze od b")
#elif b > a:
#    print("b jest wieksze od a")
#else:
#    print("a i b sa rowne")

#lista = [4,6,7,8,9,8]

#n = int(input("podaj liczbe: "))
#licznik = 0

#while licznik < len(lista):
#    if int(n) - lista[licznik] == 0:
#        print("liczba" + str(n) + " + " + str(lista[licznik]) + " = 0")
#        break
#    else:
#        licznik += 1
#else:
#    print("zadna z wartosci nie dala odpowiedniego wyniku")



#try:
#    a = 23
#    b = 0
#    wynik = a / b
#    print(wynik)
#except ZeroDivisionError:
#    print("pamiętaj cholero")
#    print("nie można dzielić przez zero")


#lista.extend(range(3, 43))

#słownik = {0:'a'}

#for x in lista:
    #print(x)


#lista2 = [x**2 for x in range(0,500) if x % 2 == 0]

#lista3 = [x for x in lista2 if x >= 16]

#for x in lista2:
#    print(x)

lista4 = [(a,b) for a in range(0,10) for b in range(0,20)]

print(lista4)


def row_kwadratowe(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("brak rozwiazan")
        return -1
    elif delta == 0:
        return -b/(2*a)
    else:
        return ((-b + (delta**(1/2))) / 2*a, (-b - (delta**(1/2))) / 2*a)

def parzysta(a):
    return a % 2 == 0

print(row_kwadratowe(1,4,1))

print(parzysta(4))