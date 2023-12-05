import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10  # Misalnya interval ukuran per 10 sentimeter

# TODO 1: Buat Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def group_into_intervals(data, interval_size):
    intervals = {}
    for height in data:
        interval = (height // interval_size) * interval_size
        intervals[interval] = intervals.get(interval, 0) + 1
    return intervals

# TODO 2: Menghitung frekuensi tinggi badan dalam interval
frekuensi_tinggi = group_into_intervals(tinggi_badan, interval_size)

# TODO 3: Visualisasi data dalam bentuk histogram
# Menggunakan bins yang sesuai dengan interval
bins = np.arange(min(tinggi_badan) // interval_size * interval_size,
                 (max(tinggi_badan) // interval_size + 2) * interval_size, interval_size)  # Mengubah menjadi +2
plt.hist(tinggi_badan, bins=bins, edgecolor='black', alpha=0.7, align='mid')  # Align diubah menjadi 'mid'
plt.xlabel('Interval Tinggi Badan (cm)')
plt.ylabel('Frekuensi')
plt.title('Histogram Tinggi Badan')

# TODO 4: Menambahkan kurva pdf pada hasil visualisasi data
mu, std = np.mean(tinggi_badan), np.std(tinggi_badan)
x = np.linspace(min(tinggi_badan), max(tinggi_badan), 100)
pdf = norm.pdf(x, mu, std)

plt.plot(x, pdf * len(tinggi_badan) * interval_size, color='red', label='Kurva PDF')
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Frekuensi')
plt.title('Histogram dan Kurva PDF Tinggi Badan')
plt.legend()

plt.show()
