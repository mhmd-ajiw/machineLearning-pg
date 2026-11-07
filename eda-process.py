import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data dump/dataset_performa_mahasiswa.csv')

df['persentase_kehadiran'] = df['persentase_kehadiran'].fillna(df['persentase_kehadiran'].mean())
df['jam_tidur_per_hari'] = df['jam_tidur_per_hari'].fillna(df['jam_tidur_per_hari'].mean())
df['jarak_ke_kampus_km'] = df['jarak_ke_kampus_km'].fillna(df['jarak_ke_kampus_km'].mean())
df_cleaned = df.copy().dropna(subset=['ipk_sebelumnya'])

df_cleaned.drop_duplicates(inplace=True)
