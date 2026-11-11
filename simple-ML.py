import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

data = {
    'jam_belajar_per_hari': [1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10],
    'jumlah_kehadiran': [8, 7, 7, 6, 5, 4, 3, 2, 2, 1, 1, 0, 0, 0],
    'status_kelulusan': ['Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Lulus', 'Lulus', 'Lulus', 'Lulus', 'Lulus', 'Lulus', 'Lulus', 'Lulus']
}
df = pd.DataFrame(data)
print('Data Mahasiswa: \n', df)

X = df[['jam_belajar_per_hari', 'jumlah_kehadiran']]
Y = df['status_kelulusan']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_scaled, Y_train)

Y_pred = model.predict(X_test_scaled)

print('\nMenampilkan Prediksi: ', Y_pred)
print('\nMatrix confusi: \n', confusion_matrix(Y_test, Y_pred))

print('\nClassification report: ', classification_report(Y_test, Y_pred))