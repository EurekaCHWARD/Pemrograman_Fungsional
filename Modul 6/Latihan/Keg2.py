from PIL import Image

# TODO 0 : Import beberapa library lain yang dibutuhkan

# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin
# disisipkan (overlay)
background_image = Image.open(r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Images\Drone.jpg")  # Ganti nama file sesuai gambar latar belakang
overlay_image = Image.open(r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Images\bob ross.png")  # Ganti nama file sesuai gambar overlay

# TODO 2 : Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert("RGB")

# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method resize()
# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
overlay_image = overlay_image.resize((500, 500))  # Ganti ukuran sesuai kebutuhan
x_center = (background_image.width - overlay_image.width) // 2
y_center = 1

# TODO 4 : Sisipkan gambar overlay ke dalam gambar background menggunakan method paste()
background_image.paste(overlay_image, (x_center, y_center))

# TODO 5 : Simpan gambar hasil edit
save_path = r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Hasil\percobaan_dua.png"  # Ganti nama file dan lokasi penyimpanan hasil edit
background_image.save(save_path)

# TODO 6 : Tampilkan
background_image.show()
