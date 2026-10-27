import pandas as pd
import matplotlib.pyplot as plt

# Boxplot method for find Outlier
data_tb = {
    'tinggi badan': [90, 160, 157, 170, 163, 153, 175, 166, 200, 280]
}
df_tb = pd.DataFrame(data_tb)

plt.boxplot(df_tb['tinggi badan'])
plt.title("Boxplot Tinggi Badan")
plt.show()