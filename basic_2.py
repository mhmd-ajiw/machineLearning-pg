import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Nama' : ['Dito', 'Rina', 'Joko', 'Dika', 'Ririn', 'Susi', 'Jean', 'Rio', 'Josi', 'Asyo'],
    'Minuman Fav': ['Kopi', 'Teh', 'Susu', 'Susu', 'Teh', 'Kopi', 'Susu', 'Teh', 'Susu', 'Kopi']
} 
df = pd.DataFrame(data)

# Frekuensi Abs
freks_abs = df['Minuman Fav'].value_counts()
print("Frekuensi Absolut: ")
print(freks_abs, '\n')

# Frekuensi Relatif
freks_rel = df['Minuman Fav'].value_counts(normalize=True)*100
print('Frekuensi Relatif (%): ')
print(freks_rel,round(2), '\n')

# Modus 
modus = df['Minuman Fav'].mode()[0]
print('Modus: ', modus, '\n')

# Visual - Diagram Batang
freks_abs.plot(kind='bar', color='skyblue')
plt.title('Frekuensi Minuman Favorit')
plt.xlabel('Jenis Minuman')
plt.ylabel('Jumlah Responden')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Visual - Diagram Lingkaran
freks_rel.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99'])
plt.title('Persentase Minuman Favorit')
plt.ylabel('')
plt.tight_layout()
plt.show()
