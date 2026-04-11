while True:
    print("\n=== OPERASI MATRIKS ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")
    pilih = input("Pilih menu: ")

    if pilih == "0":
        print("Keluar.")
        break

    baris = int(input("Masukkan baris: "))
    kolom = int(input("Masukkan kolom: "))

    print("Input matriks A:")
    A = []
    for i in range(baris):
        baris_data = []
        for j in range(kolom):
            angka = int(input(f"  [{i}][{j}] = "))
            baris_data.append(angka)
        A.append(baris_data)

    print("Input matriks B:")
    B = []
    for i in range(baris):
        baris_data = []
        for j in range(kolom):
            angka = int(input(f"  [{i}][{j}] = "))
            baris_data.append(angka)
        B.append(baris_data)

    C = []

    if pilih == "1":
        print("\n--- Proses Penjumlahan ---")
        for i in range(baris):
            baris_c = []
            for j in range(kolom):
                hasil = A[i][j] + B[i][j]
                print(f"  A[{i}][{j}] + B[{i}][{j}] = {A[i][j]} + {B[i][j]} = {hasil}")
                baris_c.append(hasil)
            C.append(baris_c)
        print("\nHasil Penjumlahan:")

    elif pilih == "2":
        print("\n--- Proses Pengurangan ---")
        for i in range(baris):
            baris_c = []
            for j in range(kolom):
                hasil = A[i][j] - B[i][j]
                print(f"  A[{i}][{j}] - B[{i}][{j}] = {A[i][j]} - {B[i][j]} = {hasil}")
                baris_c.append(hasil)
            C.append(baris_c)
        print("\nHasil Pengurangan:")

    elif pilih == "3":
        print("\n--- Proses Perkalian ---")
        for i in range(baris):
            baris_c = []
            for j in range(baris):
                total = 0
                for k in range(kolom):
                    print(f"  A[{i}][{k}] * B[{k}][{j}] = {A[i][k]} * {B[k][j]} = {A[i][k] * B[k][j]}")
                    total += A[i][k] * B[k][j]
                print(f"  Total C[{i}][{j}] = {total}")
                baris_c.append(total)
            C.append(baris_c)
        print("\nHasil Perkalian:")

    for baris_hasil in C:
        print(baris_hasil)