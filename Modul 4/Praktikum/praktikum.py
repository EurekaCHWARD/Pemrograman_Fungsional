import math

def translasi(tx, ty):
    def decorator(func):
        def transformasi(x, y):
            x_baru, y_baru = func(x + tx, y + ty)
            return x_baru, y_baru
        return transformasi
    return decorator

def dilatasi(sx, sy):
    def decorator(func):
        def transformasi(x, y):
            x_baru, y_baru = func(x * sx, y * sy)
            return x_baru, y_baru
        return transformasi
    return decorator

def rotasi(sudut):
    def decorator(func):
        def transformasi(x, y):
            sudut_rad = math.radians(sudut)
            x_baru, y_baru = func(x * math.cos(sudut_rad) - y * math.sin(sudut_rad),
                                  x * math.sin(sudut_rad) + y * math.cos(sudut_rad))
            return x_baru, y_baru
        return transformasi
    return decorator

# Fungsi untuk input dari pengguna
def input_transformasi():
    tx = float(input("Masukkan nilai translasi tx: "))
    ty = float(input("Masukkan nilai translasi ty: "))
    translasi_func = translasi(tx, ty)

    sx = float(input("Masukkan nilai dilatasi sx: "))
    sy = float(input("Masukkan nilai dilatasi sy: "))
    dilatasi_func = dilatasi(sx, sy)

    sudut = float(input("Masukkan nilai rotasi sudut: "))
    rotasi_func = rotasi(sudut)

    return translasi_func, dilatasi_func, rotasi_func

# Fungsi untuk input titik awal dari pengguna
def input_titik_awal():
    x = float(input("Masukkan nilai x titik awal: "))
    y = float(input("Masukkan nilai y titik awal: "))
    return x, y

# Fungsi untuk input nilai x dan y pada titik A dan B dari pengguna
def input_titik_a():
    x1 = float(input("Masukkan nilai x1 titik A: "))
    y1 = float(input("Masukkan nilai y1 titik A: "))
    return x1, y1

def input_titik_b():
    x2 = float(input("Masukkan nilai x2 titik B: "))
    y2 = float(input("Masukkan nilai y2 titik B: "))
    return x2, y2

# Fungsi untuk input gradien dari pengguna
def input_gradien():
    M = float(input("Masukkan nilai gradien (M): "))
    return M

# Fungsi untuk mendapatkan persamaan garis
def line_equation_of(p, M):
    x1, y1 = p

    def calculate_intercept(x1, y1, M):
        return y1 - M * x1

    C = calculate_intercept(x1, y1, M)

    return f"y = {M:.2f}x + {C:.2f}"

def line_equation_of2(p1, p2):
    def calculate_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    m = calculate_slope(p1, p2)

    def calculate_intercept2(p, m):
        return p[1] - m * p[0]

    c = calculate_intercept2(p1, m)

    return f"y = {m:.2f}x + {c:.2f}"

# Input dari pengguna
p = input_titik_awal()
M = input_gradien()
p1 = input_titik_a()
p2 = input_titik_b()

# Hitung persamaan garis
equation = line_equation_of(p, M)
print(f"Persamaan garis yang melalui titik {p} dan bergradien {M}:\n{equation}")

equation_AB = line_equation_of2(p1, p2)
print(f"Persamaan garis yang melalui titik A {p1} dan B {p2}:\n{equation_AB}")

# Hitung transformasi
translasi_func, dilatasi_func, rotasi_func = input_transformasi()

# Gabungkan transformasi menggunakan decorator
@translasi_func
@dilatasi_func
@rotasi_func
def transformasi(x, y):
    return x, y

# Hitung persamaan garis setelah transformasi
p_transformed = transformasi(*p)
M_transformed = M
equation_transformed = line_equation_of(p_transformed, M_transformed)

a_transformed = transformasi(*p1)
b_transformed = transformasi(*p2)
equation2_transformed = line_equation_of2(a_transformed, b_transformed)

# Output hasil transformasi
print(f"Persamaan garis baru setelah transformasi:\n{equation_transformed}")
print(f"Persamaan garis baru setelah transformasi:\n{equation2_transformed}")
