import matplotlib.pyplot as plt
import pandas as pd

data = {
    'umur': [16, 18, 20, 25],
    'tb': [160, 170, 165, 168]
}
df = pd.DataFrame(data)

plt.plot(df['umur'], df['tb'])
plt.title('Grafik Data Tinggi Badan')
plt.xlabel('Umur')
plt.ylabel('Tinggi Badan')
plt.grid(True)
plt.show()