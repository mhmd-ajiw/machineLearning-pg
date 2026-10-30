import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Normalization data
data = {'Number': [3, 56, 20, 15, 9, 10, 10, 71]}
df = pd.DataFrame(data)

scaler = MinMaxScaler()
df['Hasil Normalisasi'] = scaler.fit_transform(df[['Number']])
print(df)

# berguna untuk mengubah skala fitur data, biasanya 0 sampai 1
# digunakan saat data tidak memiliki distribusi normal
# menggunakan algoritma sensitif (KNN atau Neutral Networks)