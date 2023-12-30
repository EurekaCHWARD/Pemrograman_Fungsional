klasifikasiAngka = lambda x: "Positif" if x > 0 else ("Negatif" if x < 0 else "Nol")
    
def pencarianAngka(list_angka, find):
    for num in list_angka:
        if num == find:
            return "Found"
        return "Not Found"
    
hasilKlasifikasi = klasifikasiAngka(5)
print(hasilKlasifikasi)

hasilPencarian = pencarianAngka([4, 2, 0], 69)
print(hasilPencarian)