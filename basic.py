import pandas as pd
import numpy as np
from scipy.stats import zscore

df_pelanggan = pd.read_csv('data dump/data_pelanggan_kotor.csv')
df_transaksi = pd.read_csv('data dump/data_transaksi_kotor.csv')

# Mengatasi data duplikat & penggabungan
df_transaksi['id_transaksi'] = df_transaksi['id_transaksi'].drop_duplicates()
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
outlier_IQR = df_merge[(df_merge['jumlah_beli'] < batas_bawah) | (df_merge['jumlah_beli'] > batas_atas)]
df_merge['jumlah_beli'] = df_merge['jumlah_beli'].clip(lower=batas_bawah, upper=batas_atas)

z_score = zscore(df_merge['harga'])
non_outlier = np.abs(z_score) <= 3
df_clean = df_merge[non_outlier]

print(df_clean)