import pandas as pd

data = {
   'kota': ['Magelang', 'magelang', 'semarang', 'SEMARANG']
}
df = pd.DataFrame(data)
print(f'Ini data yang belum diolah:\n{df}')

df_olahan = df['kota'].str.lower()
print('\n', df_olahan)