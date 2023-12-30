barangHargaTuple = ("Pensil", 1500, "Buku", 5000, "Penggaris", 2000)

def pisahData(data_tuple):
    namaBarang = []
    hargaBarang = []
    
    for i in range(0, len(data_tuple), 2):
        namaBarang.append(data_tuple[i])
        hargaBarang.append(data_tuple[i + 1])
    return namaBarang, hargaBarang

def dictionary(namaBarang, hargaBarang):
    hasilGabung = {}
    for i in range(len(namaBarang)):
        hasilGabung[namaBarang[i]] = hargaBarang[i]
    return hasilGabung

print("1. ", barangHargaTuple)

namaBarangList, hargaBarangList = pisahData(barangHargaTuple)
print("\n2. ", namaBarangList, hargaBarangList)

hasil_dictionary = dictionary(namaBarangList, hargaBarangList)
print("\n3. ", hasil_dictionary)