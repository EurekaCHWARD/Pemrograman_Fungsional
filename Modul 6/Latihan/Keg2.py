from PIL import Image

# TODO 0 : Import beberapa library lain yang dibutuhkan

# TODO 1 : Buka gambar latar belakang (background) dan gambar yang ingin
# disisipkan (overlay)
background_image = Image.open(r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Images\Drone2.jpg")  # Ganti path sesuai lokasi background image
overlay_image = Image.open(r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Images\bob ross.png")  # Ganti path sesuai lokasi overlay image

# TODO 2 : Konversi overlay image ke mode RGBA (memastikan ada channel alpha)
overlay_image = overlay_image.convert("RGBA")

# TODO 3 : (optional) Perkecil ukuran gambar overlay menggunakan method
# resize()
# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_top_right = background_image.width - overlay_image.width
y_top_right = 0  # Assuming you want the top right corner

# TODO 4 : Buat gambar baru dengan mode RGBA (transparent)
result_image = Image.new("RGBA", background_image.size, (0, 0, 0, 0))

# Paste background onto the result image
result_image.paste(background_image, (0, 0))

# Paste overlay onto the result image with alpha channel
result_image.paste(overlay_image, (x_top_right, y_top_right), overlay_image)

# TODO 5 : Simpan gambar hasil edit
save_path = r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Hasil\percobaan_dua.png"
result_image.save(save_path)  # Ganti path sesuai lokasi penyimpanan hasil edit

# TODO 6 : Tampilkan
result_image.show()
