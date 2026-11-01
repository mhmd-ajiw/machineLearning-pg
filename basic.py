import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import StandardScaler

df_pelanggan = pd.read_csv('data dump/data_pelanggan_kotor.csv')
df_transaksi = pd.read_csv('data dump/data_transaksi_kotor.csv')

# Mengatasi data duplikat & penggabungan
df_transaksi = df_transaksi.drop_duplicates(subset=['id_transaksi'])
# EVAL: tambahkan 'subnet' supaya hanya menghapus kolom tertentu bukan keseluruhan dataset.

df_merge = pd.merge(df_pelanggan, df_transaksi, on='id_pelanggan', how='inner')

# Standarisasi & missing values
df_merge['kota'] = df_merge['kota'].str.strip().str.title()
df_merge['nama_produk'] = df_merge['nama_produk'].str.strip().str.lower()
df_merge['harga'] = df_merge['harga'].fillna(df_merge.groupby('kategori')['harga'].transform('median'))

# Penanganan outlier
Q1 = df_merge['jumlah_beli'].quantile(0.25)
Q3 = df_merge['jumlah_beli'].quantile(0.75)
IQR = Q3 - Q1

batas_bawah = Q1 - 1.5 * IQR
batas_atas = Q3 + 1.5 * IQR
# outlier_IQR = df_merge[(df_merge['jumlah_beli'] < batas_bawah) | (df_merge['jumlah_beli'] > batas_atas)]
# EVAL: tidak diperlukan, karena setelah ini melakukan 'clip'

df_merge['jumlah_beli'] = df_merge['jumlah_beli'].clip(lower=batas_bawah, upper=batas_atas)

z_score = zscore(df_merge['harga'])
non_outlier = np.abs(z_score) <= 3
df_clean = df_merge[non_outlier].copy()

# Transform logaritmik
df_clean['log_total_belanja'] = np.log1p(df_clean['total_belanja_tahunan'])
# EVAL: lebih baik gunakan 'np.log1p()' untuk menghindari -inf pada data, jika isi nilai tersebut 0.

# Encoding
skala = {'Bronze': 1, 'Silver': 2, 'Gold': 3}
df_clean['status_member (Encoded)'] = df_clean['status_member'].map(skala)
df_encoded = pd.get_dummies(df_clean, columns=['kategori'], dtype=int)

# Normalisasi/Standardisasi
scaler = StandardScaler()
df_encoded[['harga', 'jumlah_beli']] = scaler.fit_transform(df_encoded[['harga', 'jumlah_beli']])

print(df_encoded.head())