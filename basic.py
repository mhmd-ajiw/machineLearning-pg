import pandas as pd
from scipy.stats import zscore
import numpy as np

dataBB = {
    'bb':[45, 56, 60, 40, 66, 54, 50, 90]
}
df_bb = pd.DataFrame(dataBB)

df_bb['Zscore'] = zscore(df_bb['bb'])
outliers = df_bb[np.abs(df_bb['Zscore']) > 3]
print(outliers)