import pandas as pd

# Find a outlier with Quantile method (IQR)
data_tb = {
    'tinggi badan': [160, 157, 170, 163, 153, 175, 166, 200, 280]
}
df_tb = pd.DataFrame(data_tb)

Q1 = df_tb['tinggi badan'].quantile(0.25)
Q3 = df_tb['tinggi badan'].quantile(0.75)
IQR = Q3 - Q1

batas_bawah = Q1 - 1.5 * IQR
batas_atas = Q1 + 1.5 * IQR

outlier = df_tb[(df_tb['tinggi badan'] < batas_bawah) | (df_tb['tinggi badan'] > batas_atas)]
print(f'Data yang ada:\n {df_tb}\n \nOutlier: {outlier}')