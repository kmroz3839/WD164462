from re import X
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#zadanie 1
x = np.arange(1, 20, 1)
plt.plot(x, 1/x, 'g>:')


#zadanie 2 
plt.legend(['f(x) = 1/x'], loc='upper right')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Wykres funkcji f(x) dla x [1, 20]")

plt.ylim(0, 1)
plt.xlim(0,20)

plt.show()

#zadanie 3
x = np.arange(0,30,0.1)
plt.plot(x, np.sin(x), "b:")
plt.plot(x, np.cos(x), "r:")

plt.xlabel('x')
plt.ylabel('f(x)')

plt.legend(['sin(x)', 'cos(x)'], loc='upper right')
plt.xlim(0,30)
plt.ylim(2,-2)

plt.show()

#zadanie 4
df = pd.read_csv('iris.csv', header=0)
z4px = df['sepal_length']
z4py = df['sepal_width']
plt.scatter(z4px, z4py, c=np.random.randint(0, 50, 150), s=np.abs(z4px-z4py))
plt.show()

#zadanie 5
df = pd.read_excel('imiona.xlsx', header=0)

z5_a = df.groupby('Plec').agg({'Liczba': ['count']})
z5_a.plot(kind='bar', xlabel='Plec', ylabel='Liczba')
plt.show()

z5_k = df[df['Plec'] == 'K']
z5_m = df[df['Plec'] == 'M']
z5_b = z5_k.groupby('Rok').agg({'Liczba': ['sum']})
plt.plot(z5_b, 'r-')
z5_c = z5_m.groupby('Rok').agg({'Liczba': ['sum']})
plt.plot(z5_c, 'b-')
plt.legend(['K', 'M'], loc='upper right')
z5_q = df['Rok'].sort_values().unique()
print(z5_q[-1])
plt.xticks(np.arange(z5_q[0], z5_q[-1]+1, 1))
plt.xlim(z5_q[0], z5_q[-1])
plt.xlabel('Rok')
plt.ylabel('Liczba')

plt.show()

#z5_c = z5_m.groupby('Rok').agg({'Liczba': ['count']})
z5_c = z5_m.groupby('Rok').sum()

#print(z5_c)
#z5_d = z5_c[z5_c.keys()[0]]
#print(z5_c)
#z5_c.plot(kind='bar', xlabel='Rok', ylabel='Liczba')
#print(z5_c)
plt.bar(data=z5_m, x='Rok', height='Liczba')
#plt.bar(data=z5_c, x='Rok', height=z5_c.keys()[0], color='blue')
plt.xticks(np.arange(z5_q[0], z5_q[-1]+1, 1))
plt.show()

#zadanie 6
df = pd.read_csv('zamowienia.csv', sep=';', header=0)
#z6_a = df.groupby('Sprzedawca').agg({'Utarg': ['count']})
z6_a = df.groupby('Sprzedawca')['Utarg'].count()
print(len(z6_a))
plt.pie(z6_a, labels=z6_a.index, autopct='%.2f%%', explode=np.arange(0,0.7,0.7/len(z6_a)), shadow=True)
#z6_a.plot(kind='pie', xlabel='Sprzedawca', subplots=True, autopct='%.2f%%', explode=[0.1, 0, 0])


plt.show()