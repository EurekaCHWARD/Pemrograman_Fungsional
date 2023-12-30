def hitungPangkat(exponent):
    def pangkat(base):
        return base ** exponent
    return pangkat

pangkatDua = hitungPangkat(2)
pangkatTiga = hitungPangkat(3)

hasilPangkatDua = pangkatDua(4)
hasilPangkatTiga = pangkatTiga(3)

print(f"4 pangkat 2 adalah {hasilPangkatDua}")
print(f"3 pangkat 3 adalah {hasilPangkatTiga}")