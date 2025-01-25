#Zichong Meng

import pandas as pd
import matplotlib.pyplot as plt

#read in data
data = pd.read_csv('data/plant_detail.csv')

#histograms
plants = ['succulent', 'baby bamboo', 'money tree']
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
for i, plant in enumerate(plants):
    subset = data[data['plant-name'] == plant]
    axes[0, i].hist(subset['leaf-width-cm'], color='blue', label='')
    axes[0, i].set_title(f'{plant}')
    axes[0, i].set_xlabel('Leaf Width (cm)')
    axes[0, i].set_ylabel('Count')
    axes[0, i].legend()
    axes[1, i].hist(subset['leaf-length-cm'], color='blue', label='')
    axes[1, i].set_title(f'{plant}')
    axes[1, i].set_xlabel('Leaf Length (cm)')
    axes[1, i].set_ylabel('Count')
    axes[1, i].legend()
plt.tight_layout()
plt.show()

#boxplot
plt.figure(figsize=(10, 5))
data.boxplot(column='leaf-length-cm', by='plant-name')
plt.title('Plant Leaf Length')
plt.suptitle('')
plt.xlabel('')
plt.ylabel('Leaf Length (cm)')
plt.show()
plt.figure(figsize=(10, 5))
data.boxplot(column='leaf-width-cm', by='plant-name')
plt.title('Plant Leaf Width')
plt.suptitle('')
plt.xlabel('')
plt.ylabel('Leaf Width (cm)')
plt.show()

#scatterplot
plt.figure(figsize=(10, 5))
for plant in plants:
    subset = data[data['plant-name'] == plant]
    plt.scatter(subset['leaf-length-cm'], subset['leaf-width-cm'], label=plant)
plt.xlabel('Leaf Width (cm)')
plt.ylabel('Leaf Length (cm)')
plt.title('Leaf Length vs Width')
plt.legend(title='')
plt.show()
