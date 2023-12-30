total = 0

def tambahAngka(angka, total = 0):
    return total + angka

total1 = tambahAngka(6)
print(total1)

total2 = tambahAngka(9, total1)
print(total2)