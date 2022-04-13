import numpy as np
import random

#z1
z1_a = np.array([2,3,1])
z1_b = np.array([3,2,1])

print(z1_a*z1_b)

#z2
z2_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
z2_b = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])

def zn_najnizsze(a):
    i = 0
    for x in a:
        print("dla rzędu " + str(i) + ": " + str(min(x)))
        i += 1
    for x in range(0,len(a[0])):
        print("dla kolumny " + str(x) + ": " + str(min(a[:,x])))

zn_najnizsze(z2_a)
zn_najnizsze(z2_b)

#z3
z3_b = np.array([z1_b]).T
print(z1_a*z3_b)

#z4
z4_a = np.array([[4],[7],[23]])
z4_b = np.array([[231.23], [76.7655], [87.46345]])
print(z4_a*z4_b)

#z5
z5_1 = [[23, 43], [75,345], [453,36]]
z5_a = np.sin(z5_1)
print(z5_a)

#z6
z6_1 = [[345, 89], [418,761], [729,727]]
z6_b = np.cos(z6_1)
print(z6_b)

#z7
print(z5_a+z6_b)

#z8
z8_a = np.ones((3,3))
for x in range(0,len(z8_a)):
    for y in range(0,len(z8_a[x])):
        z8_a[x,y] = random.randint(0,50)

for x in z8_a:
    print(x)

#z9
z9_a = np.ones((3,3))
for x in range(0,len(z9_a)):
    for y in range(0,len(z9_a[x])):
        z9_a[x,y] = random.randint(0,50)

for x in z9_a.flat:
    print(x)

#z10
z10_a = np.ones((9,9))
for x in range(0,len(z10_a)):
    for y in range(0,len(z10_a[x])):
        z10_a[x,y] = random.randint(0,50)

print(z10_a.reshape(3,27))

#z11
z11_a = np.ones(12)
for x in range(0,len(z11_a)):
    z11_a[x] = random.randint(0,50)

z11_b34 = z11_a.reshape((3,4))
z11_c43 = z11_a.reshape((4,3))
z11_d26 = z11_a.reshape((2,6))

print(z11_b34.flat.copy())
print(z11_c43.flat.copy())
print(z11_d26.flat.copy())