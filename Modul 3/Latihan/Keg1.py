def konversi(minggu=0, hari=0, jam=0, menit=0):
    total_menit = ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit)
    return total_menit

data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]
output_data = []

for d in data:
    parts = d.split()
    minggu = int(parts[0]) if "minggu" in parts else 0
    hari = int(parts[2]) if "hari" in parts else 0
    jam = int(parts[4]) if "jam" in parts else 0
    menit = int(parts[6]) if "menit" in parts else 0

    result = konversi(minggu, hari, jam, menit)
    output_data.append(result)

print("OutputData =", output_data)