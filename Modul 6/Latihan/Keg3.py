from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan Pillow
image_path = r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Images\Drone.jpg"  # Ganti path sesuai lokasi gambar
image = Image.open(image_path)

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
brightness_factor = 0.5
contrast_factor = 1.2

brightness_enhancer = ImageEnhance.Brightness(image)
brightened_image = brightness_enhancer.enhance(brightness_factor)

contrast_enhancer = ImageEnhance.Contrast(brightened_image)
final_image = contrast_enhancer.enhance(contrast_factor)

# TODO 3: Simpan gambar hasil edit
save_path = r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Hasil\percobaan_tiga.jpg"
final_image.save(save_path)

# TODO 4: Tampilkan
final_image.show()
