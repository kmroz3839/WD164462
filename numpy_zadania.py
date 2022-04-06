import numpy as np

# z1
z1_a = np.arange(4, 4*21, 4)
print(z1_a)

# z2
z2_a = np.array([3.25443, 432.4532, 5.2, 43543.23], dtype='float')
z2_b = z2_a.astype('int32')
print(z2_b)

# z3
def z3_funkcja(n):
    p = 1
    r = np.empty((n, n), dtype='int64')
    for x in range(0, n):
        for y in range(0, n):
            r[x, y] = p
            p *= 2
    return r

print(z3_funkcja(6))

# z4
def z4_funkcja(n, p):
    return np.logspace(1, p, num=p, base=n)

print(z4_funkcja(2,5))

# z5
def z5_funkcja(dl):
    r = np.arange(dl)[::-1]
    return np.diag(r, 2)

print(z5_funkcja(5))


# z6
z6_a = np.chararray((8, 8), unicode=True)
s = "AMOGUS"
for x in range(0, 8):
    for y in range(0, 8):
        z6_a[x, y] = '\u0d9e'
for x in range(0, 6):
    z6_a[1+x, 0] = s[x]
    z6_a[0, 1+x] = s[x]
    z6_a[2+x, 1+x] = s[x]
    z6_a[5-x, 6] = s[x]
print(z6_a)


# z7
def z7_funkcja(n):
    a = np.ones([n])
    r = np.diag(a)
    r *= 2
    for x in range(1,n):
        b = np.diag(a, x)
        b *= 2*(x+1)
        r += b[:-x,:-x]
        b = np.diag(a, -x)
        b *= 2 * (x + 1)
        r += b[:-x,:-x]
    return r

print(z7_funkcja(4))

# z8
def z8_funkcja(tab, kierunek):
    if kierunek == "pionowo" and tab.shape[0] % 2 == 1:
        print("nie da rady")
        return None
    elif kierunek == "poziomo" and tab.shape[1] % 2 == 1:
        print("nie da rady")
        return None
    if kierunek == "pionowo":
        return tab[:,:(tab.shape[1]//2)]
    else:
        return tab[:(tab.shape[0]//2)]

print(z8_funkcja(np.ones([10,6]), "pionowo"))

# z9
def c_arytm(a1, r, n):
    return a1 + r*n

z9_a = []
for x in range(5*5):
    z9_a.append(c_arytm(2, 3, x))
z9_a = np.reshape(z9_a, [5,5])
print(z9_a)
