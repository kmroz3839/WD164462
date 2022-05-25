import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.linspace(0,10,100)

y1 = np.sin(x)
y2 = np.cos(x)/2

sns.lineplot(x,y1, color="yellow")
sns.lineplot(x,y2, color="green")

plt.xlim(0,5)
plt.grid(True)
plt.show()