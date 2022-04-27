import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('imiona.xlsx', header=0)

#z1
z1_a = df.groupby('Rok').agg({'Liczba': ['sum']})
z1_a.plot(kind='line', xlabel='Rok', ylabel='Liczba')
plt.show()

#z2
z2_a = df.groupby('Plec').agg({'Liczba': ['sum']})
z2_a.plot(kind='bar', xlabel='Plec', ylabel='Liczba')
plt.show()

#z3
z3_a = df.groupby('Plec').agg({'Liczba': ['sum']})
z3_a.plot(kind='pie', xlabel='Plec', subplots=True, autopct='%.2f%%')
plt.show()

#z4
z4_df = pd.read_csv('zamowienia.csv', sep=';', header=0)
z4_a = z4_df.groupby('Sprzedawca').agg({'Utarg': ['count']})
z4_a.plot(kind='bar', xlabel='Sprzedawca', ylabel='Ilosc zamowien')
plt.show()