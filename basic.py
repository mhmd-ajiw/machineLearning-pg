import pandas as pd
from scipy.stats import zscore
import numpy as np

# Find Outlier with Z-Score method
dataBB = {
    'bb':[45, 56, 60, 40, 66, 54, 50, 90]
}
df_bb = pd.DataFrame(dataBB)

df_bb['Zscore'] = zscore(df_bb['bb'])
outliers = df_bb[np.abs(df_bb['Zscore']) > 3]
print(outliers)

# Alasan output terminal kosong bukan karena codenya salah, tapi karena semua nilai data
# masih dalam rentang yang ditentukan. Jadi Z-Score menganggap semua nilai dalam rentang
# -3 sampai 3 itu nomal, jika melebihi atau kurang maka dianggap Outlier.
# 90 disini masih dalam perhitugan makanya nilai output kosong.