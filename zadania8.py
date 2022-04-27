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
    #print(str(x)+": ")
    for y in ['M', 'K']:
        #print(y + ": ")
        print(zad1_df[(zad1_df['Rok'] == x) & (zad1_df['Plec'] == y)].sort_values('Liczba').tail(1))
#g)
print("-----------------------------")
for y in ['M', 'K']:
    #print(y + ": ")
    print(zad1_df[(zad1_df['Plec'] == y)].sort_values('Liczba').tail(1))

#z3
zad3_df = pd.read_csv('zamowienia.csv', sep=';', header=0)
#a)
print(zad3_df['Sprzedawca'].unique())
#b)
print(zad3_df.sort_values('Utarg', ascending=False).head(5))
#c)
print(zad3_df.groupby('Kraj').agg({'Utarg': ['sum']}))
#d)
print(zad3_df[(zad3_df['Kraj'] == 'Polska') & (zad3_df['Data zamowienia'].str.contains('2005'))]['Utarg'].sum())
#e)
print(zad3_df[(zad3_df['Data zamowienia'].str.contains('2004'))]['Utarg'].mean())
#f)
zad3_df[(zad3_df['Data zamowienia'].str.contains('2004'))].to_csv('zamowienia_2004.csv', sep=';', index=False)
zad3_df[(zad3_df['Data zamowienia'].str.contains('2005'))].to_csv('zamowienia_2005.csv', sep=';', index=False)