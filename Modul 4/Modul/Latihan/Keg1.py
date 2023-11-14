# Higher Order Function (HOF)
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

hasil_hof = perkalian(5)(3)
print(hasil_hof)

# Currying
def perkalian_currying(a):
    return lambda b: a * b

hasil_currying = perkalian_currying(5)(3)
print(hasil_currying)
