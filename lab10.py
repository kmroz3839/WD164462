import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()

#ts.plot()
#plt.show()

df = pd.DataFrame(ts)
print(df)

df['Średnia krocząca'] = df.rolling(window=50).mean()

df.plot()
plt.legend(['Wartości', 'Średnia z n-elementów'])
plt.show()
#---------------------------------------------------------------

##dane = { 'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#        'Populacja': [11190846, 1303171035, 207847528, 38484000],
#        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'] }

#dane2 = pd.DataFrame(dane)

#gr = dane2.groupby('Kontynent').agg({'Populacja': ['sum']})
#print(dane2)
#
#print(gr)
#
#gr.plot(kind='bar', xlabel='Kontynent', ylabel='Populacja', title="populacja kontynentów")
#
#wykres = gr.plot.bar()
#wykres.tick_params(axis='x', rotation=0)
#
#plt.show()
#
#plt.savefig('i_am_in_your_walls.png')

#---------------------------------------------------------------

#df = pd.read_csv('dane.csv', sep=';', header=0, decimal='.')
#print(df)
#
#grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia': ['sum']})
#
#grupa.plot(kind='pie', subplots=True, autopct='%.2f%%', fontsize=20, figsize=(8,8))
#plt.legend(loc='upper left')
#plt.show()