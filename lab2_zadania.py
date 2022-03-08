import sys

#z1
lista_z1 = ["skoki narciarskie", "łyżwiarstwo", "piłka nożna"]
lista_z1.reverse()
lista_z1.append("koszykówka")

#z2
skroty = {}
skroty["np"] = "na przykład"
skroty["itp"] = "i tym podobne"
skroty["itd"] = "i tak dalej"

#z3
slownik_z3 = {}
slownik_z3["2009"] = "Call of Duty: Modern Warfare 2"
slownik_z3["2010"] = "Call of Duty: Black Ops"
slownik_z3["2011"] = "Call of Duty: Modern Warfare 3"
slownik_z3["2012"] = "Call of Duty: Black Ops II"
slownik_z3["2013"] = "Call of Duty: Ghosts"
slownik_z3["2014"] = "Call of Duty: Advanced Warfare"
slownik_z3["2015"] = "Call of Duty: Black Ops III"
slownik_z3["2016"] = "Call of Duty: Infinite Warfare"
slownik_z3["2017"] = "Call of Duty: WWII"
slownik_z3["2018"] = "Call of Duty: Black Ops 4"
slownik_z3["2019"] = "Call of Duty: Modern Warfare [2019]"
slownik_z3["2020"] = "Call of Duty: Black Ops Cold War"
slownik_z3["2021"] = "Call of Duty: Vanguard"

print(len(slownik_z3))

#z4
z4_a = input()

r = 0
for x in z4_a:
    if x == 'a':
        r += 1

print("litera a wystapila " + str(r) + " razy")


#z5
z5_la = int(sys.stdin.readline())
z5_lb = int(sys.stdin.readline())
z5_lc = int(sys.stdin.readline())

sys.stdout.write(str(z5_la ** z5_lb + z5_lc))

#z6
z6_a = int(input())
z6_b = int(input())
z6_c = int(input())
z6_z = [z6_a, z6_b, z6_c]

najmn = z6_a
najw = z6_a
for x in z6_z:
    if x < najmn:
        najmn = x
    if x > najw:
        najw = x

print("Najwieksza: " + str(najw) + ", najmniejsza: " + str(najmn))

#z7
z7_l = [3, 4, 5, 6.768, 4.345, 5.463, 3, 5]
for x in range(0, len(z7_l)):
    z7_l[x] **= 2


#z8
z8_l = []
for x in range(0,10):
    a = int(input())
    if a % 2 == 0:
        z8_l.append(a)


#z9
try:
    z9_a = float(input())
    if z9_a < 0:
        raise ValueError
    print(z9_a ** (1/2))
except ValueError:
    print("błąd")
