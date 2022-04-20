import numpy as np
import pandas as pd

#z1
zad1_df = pd.read_excel('imiona.xlsx')

#z2
#a)
print(zad1_df[zad1_df['Liczba'] > 1000])
#b)
print(zad1_df[zad1_df['Imie'] == "KAMIL"])
#c)
print(zad1_df['Liczba'].sum())
#d)
print(zad1_df[(zad1_df['Rok'] >= 2000) & (zad1_df['Rok'] <= 2005)])
#e)
print(zad1_df.groupby('Plec').sum()['Liczba'])
#f)
z1f_a = zad1_df['Rok'].unique()
for x in z1f_a:
    print(str(x)+": ")
    for y in ['M', 'K']:
        print(zad1_df[(zad1_df['Rok' == x] & (zad1_df['Plec' == y]))].idxmax())