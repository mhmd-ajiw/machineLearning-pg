import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# KMeans method
data = {'Nilai': [34, 56, 44, 67, 12, 90, 100, 72, 68]}
df = pd.DataFrame(data)

X = df[['Nilai']].values
kmeans = KMeans(n_clusters=2, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

centroids = kmeans.cluster_centers_
df['Jarak'] = [np.linalg.norm(x - centroids[c]) for x, c in zip(X, df['Cluster'])]
print(df)

# jadi methode ini menetukan nilai tengah(acak) atau K
# kemudian menyuruh nilai lainnya untuk mendekat dengan K (yang nilainya mirip)
# setelah bergerombol semua, menentukan nilai tengah lagi (centroids) sampai benar benar stabil
# dengan perhitungan Mean