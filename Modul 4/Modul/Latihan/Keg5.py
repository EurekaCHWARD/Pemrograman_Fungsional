def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    def calculate_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    m = calculate_slope(p1, p2)

    def calculate_intercept(p, m):
        return p[1] - m * p[0]

    c = calculate_intercept(p1, m)

    return f"y = {m:.2f}x + {c:.2f}"

# Titik A dan B
A = point(1, 3)
B = point(4, 5)

# Persamaan garis yang melalui titik A dan B
equation_AB = line_equation_of(A, B)
print("Persamaan garis yang melalui titik A dan B:")
print(equation_AB)
