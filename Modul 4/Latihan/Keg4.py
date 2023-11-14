import math

def translasi(tx, ty):
    def transformasi(x, y):
        return x + tx, y + ty
    return transformasi

def dilatasi(sx, sy):
    def transformasi(x, y):
        return x * sx, y * sy
    return transformasi

def rotasi(sudut):
    def transformasi(x, y):
        sudut_rad = math.radians(sudut)
        x_baru = x * math.cos(sudut_rad) - y * math.sin(sudut_rad)
        y_baru = x * math.sin(sudut_rad) + y * math.cos(sudut_rad)
        return x_baru, y_baru
    return transformasi

# Contoh kasus
titik_awal = (3, 5)

# Translasi
translasi_func = translasi(2, -1)
titik_setelah_translasi = translasi_func(*titik_awal)
print(f"Koordinat setelah translasi: {titik_setelah_translasi}")

# Dilatasi
dilatasi_func = dilatasi(2, -1)
titik_setelah_dilatasi = dilatasi_func(*titik_awal)
print(f"Koordinat setelah dilatasi: {titik_setelah_dilatasi}")

# Rotasi
rotasi_func = rotasi(30)
titik_setelah_rotasi = rotasi_func(*titik_awal)
print(f"Koordinat setelah rotasi: {titik_setelah_rotasi}")
