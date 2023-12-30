from functools import reduce

data = [3, 9, 15, 21, 27, 33, 39, 45]

hasil = reduce(lambda x, y: x + y, data)
print(hasil)
