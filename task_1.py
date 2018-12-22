import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('02_Data_test.csv', delimiter=';')
print(list(data))
print(len(list(data)))
for a in range(len(list(data))):
    plt.figure(figsize=(13, 4))
    plt.subplot(1, 2, 1)
    sns.boxplot(data[list(data)[a]])
    plt.show()

# correlation = data.corr(method='pearson')
# plt.figure(figsize=(10, 10))
# sns.heatmap(correlation, vmax=.8, square=True, cmap='YlGnBu', annot=True)
# plt.show()
#

