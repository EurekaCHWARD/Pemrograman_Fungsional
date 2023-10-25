data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]
integer_values = []

for d in data:
    parts = d.split()
    numbers = list(filter(str.isdigit, parts))
    integer_values.append(numbers)

for values in integer_values:
    print(values)