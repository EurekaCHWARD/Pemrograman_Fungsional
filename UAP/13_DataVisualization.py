import matplotlib.pyplot as plt

data = [
    ('Bus', 5, 200),
    ('Trem', 8, 150),
    ('Kereta', 12, 300),
    ('Minibus', 6, 180),
    ('Tram', 9, 220)
]

# TODO 2: Pisahkan Data masing-masing (dapat menggunakan pemetaan)
jenisKendaraan, penggunaanEnergi, biayaOperasional = zip(*data)

plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.bar(jenisKendaraan, penggunaanEnergi)
plt.title('penggunaan_energi')
plt.xlabel('jenis_kendaraan')
plt.ylabel('penggunaan_energi')

plt.subplot(1, 3, 2)
plt.bar(jenisKendaraan, biayaOperasional)
plt.title('biaya_operasional')
plt.xlabel('jenis_kendaraan')
plt.ylabel('biaya_operasional')

plt.subplot(1, 3, 3)
plt.scatter(penggunaanEnergi, biayaOperasional)
for i, kendaraan in enumerate(jenisKendaraan):
    plt.annotate(kendaraan, (penggunaanEnergi[i], biayaOperasional[i]))

# Menambahkan legenda
plt.legend()

# Tampilkan plot
plt.tight_layout()
plt. show()