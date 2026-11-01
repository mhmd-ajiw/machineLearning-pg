import matplotlib.pyplot as plt

label = ['Kebutuhan\nSehari-hari', 'Investasi', 'Hiburan', 'Other']
nilai = [40, 30, 20, 10]

plt.pie(nilai, labels=label, autopct='%0.0f%%', startangle=90)
plt.title('Alokasi Keuangan')
plt.axis('equal')
plt.show()