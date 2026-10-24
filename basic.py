import pandas as pd

# Read files
df_karyawan = pd.read_csv('data dump/data_karyawan.csv')
df_kinerja = pd.read_csv('data dump/data_kinerja.csv')

# Fill missing values
df_karyawan['gaji_per_bulan'] = df_karyawan['gaji_per_bulan'].fillna(df_karyawan.groupby('departemen')['gaji_per_bulan'].transform('median'))
df_kinerja['skor_kinerja'] = df_kinerja['skor_kinerja'].fillna(df_kinerja['skor_kinerja'].mean())

# Merge & Join
df_merged = pd.merge(df_karyawan, df_kinerja, on='id_karyawan', how='left')
df_merged['skor_kinerja'] = df_merged['skor_kinerja'].fillna(0)
df_merged['jumlah_proyek_selesai'] = df_merged['jumlah_proyek_selesai'].fillna(0)

# Manipulation
df_merged['bonus'] = 0
df_merged.loc[df_merged['skor_kinerja'] >= 80, 'bonus'] = df_merged['gaji_per_bulan'] * 0.15

# Grouping & Sort
result = df_merged.groupby('departemen').agg(
    mean_gaji = ('gaji_per_bulan', 'mean'),
    mean_kinerja = ('skor_kinerja', 'mean'),
    total_bonus = ('bonus', 'sum')
).sort_values(by='total_bonus', ascending=False)
print(result.head())

# Save result
df_merged.to_csv('karyawan_final.csv', index=False)
result.to_csv('laporan_departemen.csv', index=False)