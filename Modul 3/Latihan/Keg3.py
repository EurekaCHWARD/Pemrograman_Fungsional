random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Filter untuk memisahkan nilai float, int, dan string
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_int_to_units_tens_hundreds(number):
    if isinstance(number, int):
        units = number % 10
        tens = (number // 10) % 10
        hundreds = (number // 100) % 10
        return {'ratusan': hundreds, 'puluhan': tens, 'satuan': units}
    return None

int_mapped = list(map(map_int_to_units_tens_hundreds, int_values))

# Output
print("Data Float:", float_values)
print("Data Int:")
for value in int_mapped:
    print(value)
print("Data String:", [s for s in string_values if s.isalpha()])