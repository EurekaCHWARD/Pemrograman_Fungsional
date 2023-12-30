data = range(10)
filterData = filter(lambda x: x % 2 == 1, data)
mapping = map(lambda y: y * 2, filterData)

hasil = map(lambda y: y * 2, filter(lambda x: x % 2 == 1, range(10)))
print(list(hasil))