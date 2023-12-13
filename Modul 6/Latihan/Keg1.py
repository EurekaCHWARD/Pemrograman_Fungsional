from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open(r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Images\lol.png")  # Ganti path sesuai lokasi gambar

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
direktoriFont = r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Font\arial_narrow_7.ttf"  # Ganti path sesuai lokasi font
font_size = 24
font = ImageFont.truetype(direktoriFont, font_size)
text = "Nama: Eureka\nNIM: 345"
text_x = 10
text_y = 10
draw.text((text_x, text_y), text, font=font, fill=255)

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
save_path = r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Hasil\percobaan_satu.jpg"  # Ganti path sesuai lokasi penyimpanan
gambarBW.save(save_path)

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()