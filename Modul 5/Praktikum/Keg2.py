import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10), ("Produk B", 30, 25), ("Produk C", 20, 30),
    ("Produk D", 60, 8),  ("Produk E", 40, 15), ("Produk F", 70, 5),
]

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk, jumlah_terjual = zip(*[(harga, jumlah) for _, harga, jumlah in data_transaksi])

# TODO 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.subplot(1, 2, 1)
plt.scatter(harga_produk, jumlah_terjual, label='Jumlah Terjual')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Terjual')
plt.title('Hubungan Harga Produk dan Jumlah Terjual')
plt.legend()

# TODO 3: Hitung total pendapatan untuk setiap produk
pendapatan_produk = list(map(lambda tup: (tup[0], tup[1] * tup[2]), data_transaksi))

# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
produk, pendapatan = zip(*pendapatan_produk)
plt.subplot(1, 2, 2)
plt.bar(produk, pendapatan, color=(0.5, 0.7, 1, 1))
plt.xlabel('Produk')
plt.ylabel('Pendapatan')
plt.title('Pendapatan Produk')

# Tampilkan kedua subplot secara bersamaan
plt.tight_layout()
plt.show()

'''Subplot pertama memberikan gambaran visual tentang bagaimana harga produk berkaitan dengan jumlah produk yang terjual, 
sementara subplot kedua memberikan informasi tentang pendapatan yang dihasilkan oleh setiap produk. Dengan menggunakan plt.tight_layout(), 
tata letak antara kedua subplot disesuaikan untuk memastikan tampilan yang baik dan rapi.'''