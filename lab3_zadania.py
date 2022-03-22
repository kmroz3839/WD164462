import random

#z1
A = [1-x for x in range(1,11)]

B = [4**x for x in range(0,8)]

C = [x for x in B if x % 2 == 0]


#z2
lista1 = []
for x in range(0,10):
    lista1.append(random.randint(0,300))
lista2 = [x for x in lista1 if x % 2 == 0]


#z4
def trojkat_prostokatny(a, b, c):
    z4l_a = [a,b,c]
    for x in range(0,3):
        if z4l_a[x]**2 + z4l_a[(x+1)%3]**2 == z4l_a[(x+2)%3]**2:
            return True
    return False

#z5
def pole_trapezu(a = 2,b = 2,h = 2):
    return ((a+b)*h)/2

print(pole_trapezu())

#z6
def iloczyn_el_c(a=1, b=4, ile=10):
    r = a
    for x in range(0,10):
        r *= r*(b**x)
    return ret

#z7
# ??????

#z8
def il_c(lista):
    ilosc = len(lista)
    wartosc = 0;
    for x in lista:
        wartosc += lista[x]
    return (ilosc, wartosc) #???

