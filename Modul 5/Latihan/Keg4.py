import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

# Menambahkan variasi warna dan ukuran marker
colors = ['red', 'green', 'blue', 'purple', 'orange']
sizes = [20, 50, 100, 150, 200]

plt.scatter(x, y, c=colors, s=sizes, alpha=0.7, edgecolors='black', linewidth=1.5, label='Data Points')

# Menambahkan judul dan label sumbu
plt.title('Scatter Plot dengan Variasi')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

# Menambahkan keterangan (legend)
plt.legend()

plt.show()