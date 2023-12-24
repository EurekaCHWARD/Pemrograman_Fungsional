from PIL import Image, ImageEnhance, ImageDraw, ImageFont, ImageFilter

background_image_path = r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Images\umm.jpg"  # Ganti path sesuai lokasi gambar background
overlay_image_path = r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Images\logo_umm.jpg"  # Ganti path sesuai lokasi gambar overlay

background_image = Image.open(background_image_path)
overlay_image = Image.open(overlay_image_path)

background_image = background_image.convert('L')
background_image = background_image.rotate(30)
background_image = background_image.filter(ImageFilter.BLUR)

overlay_width = 500
overlay_height = 500
overlay_image = overlay_image.resize((overlay_width, overlay_height))

brightness_factor = 1.45
contrast_factor = 1.45

brightness_enhancer = ImageEnhance.Brightness(overlay_image)
brightened_overlay = brightness_enhancer.enhance(brightness_factor)

contrast_enhancer = ImageEnhance.Contrast(brightened_overlay)
final_overlay = contrast_enhancer.enhance(contrast_factor)

result_image = Image.new("RGB", background_image.size, (0, 0, 0))

position = (500, 150)
result_image.paste(background_image, (0, 0))
result_image.paste(final_overlay, position)

draw = ImageDraw.Draw(result_image)
font = ImageFont.truetype(r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Font\arial_narrow_7.ttf", size=24)
text = "Informatika JOSSS!"
text_x = (result_image.width) // 2
text_y = (result_image.height) // 2
draw.text((text_x, text_y), text, font=font, fill="red")

save_path = r"D:\Eureka\Semester5\Fungsional\Modul 6\Assets\Hasil\tugas_praktikum_enam.png"
result_image.save(save_path)

result_image.show()
