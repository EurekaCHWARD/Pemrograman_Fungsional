import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from functools import reduce

# Data mahasiswa
data_mahasiswa = [
    {"nama": "Mahasiswa 1", "tinggi": 170, "umur": 20},
    {"nama": "Mahasiswa 2", "tinggi": 165, "umur": 22},
    {"nama": "Mahasiswa 3", "tinggi": 175, "umur": 21},
    {"nama": "Mahasiswa 4", "tinggi": 190, "umur": 23},
    {"nama": "Mahasiswa 5", "tinggi": 185, "umur": 18}, 
    # Tambahkan data mahasiswa lainnya sesuai kebutuhan
]

# Pure Function untuk mencari rata-rata
def hitung_rata_rata(data, key):
    total = reduce(lambda x, y: x + y[key], data, 0)
    return total / len(data)

# Inner Function
def tampilkan_grafik(tinggi, umur, rata_tinggi):
    plt.bar(range(len(tinggi)), tinggi, tick_label=[f'Mahasiswa {i+1}' for i in range(len(tinggi))])
    plt.axhline(y=rata_tinggi, color='r', linestyle='--', label=f'Rata-rata: {rata_tinggi:.2f}')
    plt.xlabel('Mahasiswa')
    plt.ylabel('Tinggi Badan (cm)')
    plt.title('Grafik Tinggi Badan Mahasiswa')
    plt.show()

# Decorator untuk mengukur waktu eksekusi
def measure_execution_time(func):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Waktu eksekusi {func.__name__}: {end_time - start_time} detik")
        return result

    return wrapper

# GUI menggunakan Tkinter
class MahasiswaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Mahasiswa")

        # Variabel untuk menyimpan hasil
        self.rata_tinggi = tk.StringVar()
        self.rata_umur = tk.StringVar()

        # Frame Utama
        frame_utama = ttk.Frame(self.root, padding="10")
        frame_utama.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Button dan Label
        btn_hitung = ttk.Button(frame_utama, text="Hitung Rata-rata", command=self.hitung_dan_tampilkan)
        btn_hitung.grid(row=0, column=0, columnspan=2)

        lbl_rata_tinggi = ttk.Label(frame_utama, text="Rata-rata Tinggi Badan:")
        lbl_rata_tinggi.grid(row=1, column=0, sticky=tk.E)

        lbl_rata_umur = ttk.Label(frame_utama, text="Rata-rata Umur:")
        lbl_rata_umur.grid(row=2, column=0, sticky=tk.E)

        # Entry untuk menampilkan hasil
        entry_rata_tinggi = ttk.Entry(frame_utama, textvariable=self.rata_tinggi, state="readonly")
        entry_rata_tinggi.grid(row=1, column=1)

        entry_rata_umur = ttk.Entry(frame_utama, textvariable=self.rata_umur, state="readonly")
        entry_rata_umur.grid(row=2, column=1)

    # High Order Function dan Closure
    @measure_execution_time
    def hitung_dan_tampilkan(self):
        tinggi = [mahasiswa["tinggi"] for mahasiswa in data_mahasiswa]
        umur = [mahasiswa["umur"] for mahasiswa in data_mahasiswa]

        # Menggunakan Pure Function
        rata_tinggi = hitung_rata_rata(data_mahasiswa, "tinggi")
        rata_umur = hitung_rata_rata(data_mahasiswa, "umur")

        # Menyimpan hasil ke dalam variabel yang dapat diakses oleh inner function
        self.rata_tinggi.set(f"{rata_tinggi:.2f} cm")
        self.rata_umur.set(f"{rata_umur:.2f} tahun")

        # Memanggil inner function untuk menampilkan grafik
        tampilkan_grafik(tinggi, umur, rata_tinggi)

# Menjalankan program
if __name__ == "__main__":
    root = tk.Tk()
    app = MahasiswaGUI(root)
    root.mainloop()
