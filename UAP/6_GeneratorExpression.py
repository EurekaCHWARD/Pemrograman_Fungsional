def count(start = 1, stop = 51):
    for x in range(start, stop):
        if x % 2 != 0:
            print(x, end = " ")
            
count()