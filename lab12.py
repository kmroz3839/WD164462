import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# sns.set(rc={'figure.figsize':(8,8)})

# sns.lineplot(x=[1,2,3,4], y=[1,4,6,9],
#             label='linia nr 1', color='red', marker='o', linestyle=':')

# sns.lineplot(x=[1,2,3,4], y=[2,5,10,17],
#             label='linia nr 2', color='green', marker='^', linestyle=':')

# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('Wykres liniowy')
# plt.show()


# s = pd.Series(np.random.randn(1000))
# s = s.cumsum()
# sns.set()
# wykres = sns.relplot(kind='line', data=s, label='linia')
# wykres.fig.set_size_inches(8,6)
# wykres.fig.suptitle('Wykres liniowy losowych danych')
# wykres.set_xlabels('indeksy')
# wykres.set_ylabels('wartości')
# wykres.add_legend()
# plt.show()


# sns.set()
# df = pd.read_csv('iris.csv', header=0, sep=',', decimal='.')
# wykres = sns.lineplot(data=df, x=df.index, y='sepal_length', hue='class', palette=['red', 'green', 'blue'])
# wykres.set_xlabel('indeksy')
# wykres.set_title('Wykres liniowy danych z Iris dataset')
# wykres.legend(title='Rodzaj kwiatu')
# plt.show()


sns.set()
data = {'a': np.arange(10),
        'c': np.random.randint(0, 50, 10),
        'd': np.random.randn(10)}
data['b'] = data['a'] + 10 * np.random.randn(10)
data['d'] = np.abs(data['d']) * 100

df = pd.DataFrame(data)
plot = sns.relplot(data=df, x='a', y='b', hue='c', palette='bright', size='d', legend=True)
plot.fig.set_size_inches(6,6)
plot.set(xticks=data['a'])
plt.show()