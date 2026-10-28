import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Encoder data from teks to numerik
data = {
    'Warna': ['Merah', 'Kuning', 'Hijau', 'Biru', 'Merah']
}
df = pd.DataFrame(data)

encoder = LabelEncoder()
df['Encoded'] = encoder.fit_transform(df['Warna'])
print(df)