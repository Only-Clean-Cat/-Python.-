import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt

series_example = pd.Series([4,7,-5,3])
print(series_example)
print('_' * 50)
city = {'Город': ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург'],
        'Год основания': [1147, 1703, 1893, 1723],
        'Население(млн)': [11.9, 4.9, 1.5, 1.4]}
df = pd.DataFrame(city)
print(df)
print('_' * 50)
res = requests.get('https://skillbox.ru')
print(res)
print('_' * 50)
response = requests.get('https://api.github.com')
print(response.content)
print('_' * 50)
a = np.array([1,2,3])
a1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)
a2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a)
print('_' * 50)
print(a1)
print('_' * 50)
print(a2)
print('_' * 50)
a = np.zeros((2,2))
print(a)
print('_' * 50)
x = [1,2,3,4,5]
y = [25,32,34,20,25]
plt.plot(x,y)
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.title('График № 1')
plt.plot(x,y, color='green', marker='o', markersize=7)
print(plt.show())
print('_' * 50)
