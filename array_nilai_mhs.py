mahasiswa = {
    "10121001": "Asep",
    "10121002": "Budi",
    "10121003": "Cecep"
}

nilai = {
    "10121001": [50, 70, 40, 80],
    "10121002": [78, 78, 80, 65],
    "10121003": [87, 88, 67, 69]
}

max_rata = 0
nama_terbaik = ""

for nim, n in nilai.items():
    rata = sum(n) / len(n)
    if rata > max_rata:
        max_rata = rata
        nama_terbaik = mahasiswa[nim]

total_mk = [0, 0, 0, 0]
jumlah_mahasiswa = len(nilai)

for n in nilai.values():
    for i in range(4):
        total_mk[i] += n[i]

min_rata = float('inf')
mk_terkecil = ""

for i in range(4):
    rata = total_mk[i] / jumlah_mahasiswa
    if rata < min_rata:
        min_rata = rata
        mk_terkecil = f"MK{i+1}"

print(f"Mahasiswa Terpintar : {nama_terbaik} ({max_rata:.2f})")
print(f"Mata Kuliah Nilai Terkecil : {mk_terkecil} ({min_rata:.2f})")