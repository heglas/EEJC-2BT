import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Dados
x = np.random.normal(size=100)
y = np.random.normal(size=100)

# Plotando gráfico de dispersão
plt.figure(figsize=(2, 2))
sns.scatterplot(x=x, y=y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfico de Dispersão')
plt.show()
