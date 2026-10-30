import pandas as pd
from sklearn.preprocessing import StandardScaler

# Stadarizarion data
data = {'Number': [3, 56, 20, 15, 9, 10, 10, 71]}
df = pd.DataFrame(data)

scaler = StandardScaler()
df['Nilai Standarisasi'] = scaler.fit_transform(df[['Number']])
print(df)

# mengubah data sehingga memiliki mean 0 dan standar deviasi 1
# digunakan saat data mendekatik distribusi normal
# cocok untuk algoritma Logistic Regression, SVM, dan Linear Regression