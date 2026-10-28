import pandas as pd
from sklearn.ensemble import IsolationForest
from scipy.stats import zscore

# Find Outlier with Isolation Forest method
data = {'Nilai': [34, 56, 44, 67, 12, 90, 100, 72, 68]}
df = pd.DataFrame(data)

df['Z-Score'] = zscore(df['Nilai'])

model = IsolationForest(contamination=0.2, random_state=42)
df['Outlier_IF'] = model.fit_predict(df[['Nilai']])
print(df)

# metode ini intinya menganggap nilai yang terlalu jauh rentannya sebagai Outlier
# misalkan ada gerombolan yang nilainya berdekatan, maka outlier adalah nilai
# yang jauh dari gerombolan tersebut.