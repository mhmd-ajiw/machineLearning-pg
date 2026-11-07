import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'ID' : range(1, 16),
    'Nama' : ['Ali', 'Adi', 'Susan', 'Eko', 'Rini', 'Riri', 'Sudi', 'Roni', 'Jessica', 'Oki', 'Asie', 'Budi', 'Zoe', 'Sinta', 'Rosi'],
    'Umur': [23, 22, 10, 19, 19, np.nan, 18, 21, 22, np.nan, 26, 23, 18, 21, np.nan],
    'Jenis_kelamin': ['L', 'L', 'P', 'L', 'P', 'P', 'L', 'L', 'P', 'L', 'P', 'L', 'P', 'P', 'P'],
    'Pendapatan': [2000000, 3500000, np.nan, 2550000, 1500000, np.nan, 4000000, 2500000, 3000000, 1500000, 1000000, 3000000, 2000000, 2500000, 4000000]
}
df = pd.DataFrame(data)

print('Data awal: ')
print(df.head())

print('\nCek nilai kosong/hilang:')
print(df.isnull().sum())
print('Jumlah duplikasi:')
print(df.duplicated().sum())

print('\nStatistik deksriptif:')
print(df.describe())

plt.figure(figsize=(6,4))
sns.histplot(df['Umur'], kde=True, bins=10)
plt.title('Distribusi umur')
plt.xlabel('Umur')
plt.ylabel('Frekuensi')
# plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x='Jenis_kelamin', y='Pendapatan', data=df)
plt.title('\nPendapatan berdasarkan jenis kelamin')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Pendapatan')
# plt.show()

plt.figure(figsize=(5,4))
corr = df[['Umur', 'Pendapatan']].corr()
sns.heatmap(corr, annot=True, cmap='YlGnBu')
plt.title('Korelasi umur dan pendapatan')
# plt.show()

print('\nRata-rata pendapatan berdasarkan jenis kelamin:')
print(df.groupby('Jenis_kelamin')['Pendapatan'].mean())

print('\nMenampilkan baris yang ada nilai hilang:')
print(df[df.isnull().any(axis=1)])