import matplotlib.pyplot as plt
import pandas as pd

data = {
    'umur': [16, 18, 20, 25, 14, 31, 50],
    'tb': [160, 170, 165, 168, 153, 159, 171]
}
df = pd.DataFrame(data)

plt.scatter(df['umur'], df['tb'])
plt.title('Scatter Plot')
plt.xlabel('Umur')
plt.ylabel('Tinggi Badan')
plt.grid(True)
plt.show()