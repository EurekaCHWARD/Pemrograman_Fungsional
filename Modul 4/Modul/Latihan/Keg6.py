def point(x, y):
    return x, y

def line_equation_of(p, M):
    x1, y1 = p

    def calculate_intercept(x1, y1, M):
        return y1 - M * x1

    C = calculate_intercept(x1, y1, M)

    return f"y = {M:.2f}x + {C:.2f}"

# Titik (3, 4) dan gradien 5
p = point(3, 4)
M = 5

# Persamaan garis yang melalui titik (3, 4) dan bergradien 5
equation = line_equation_of(p, M)
print("Persamaan garis yang melalui titik (3, 4) dan bergradien 5:")
print(equation)
