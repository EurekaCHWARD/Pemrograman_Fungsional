import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([5, 9, 4, 8])  # Garis ketiga

# Membuat plot untuk garis y1, y2, dan y3 dengan corak garis yang berbeda
plt.plot(y1, label='Garis 1', linestyle='-', color='blue')  # Garis solid biru
plt.plot(y2, label='Garis 2', linestyle='--', color='green')  # Garis putus-putus hijau
plt.plot(y3, label='Garis 3', linestyle=':', color='red')  # Garis titik-titik merah

# Menambahkan judul dan label sumbu
plt.title('Plot Tiga Garis')
plt.xlabel('Indeks Data')
plt.ylabel('Nilai y')

# Menambahkan keterangan (legend)
plt.legend()

plt.show()