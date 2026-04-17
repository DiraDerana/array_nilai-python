def pangkat_rekursif(a, b):
    """Menghitung a pangkat b secara rekursif"""
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * pangkat_rekursif(a, b - 1)

def hitung_deret(n):
    """
    Menghitung deret: 1 - 2/3 + 5/8 - 13/21 + ...
    Pola: pembilang dan penyebut mengikuti pola Fibonacci-like
    """
    if n == 0:
        return 0
    
    hasil = 1  
    
    fib_pembilang = [1, 2]  
    fib_penyebut = [1, 3]   
    
    tanda = -1
    for i in range(1, n):
        pembilang = fib_pembilang[-1]
        penyebut = fib_penyebut[-1]
        
        hasil += tanda * (pembilang / penyebut)
        
        # Update fibonacci
        fib_pembilang.append(fib_pembilang[-1] + fib_pembilang[-2])
        fib_penyebut.append(fib_penyebut[-1] + fib_penyebut[-2])
        
        tanda *= -1
    
    return hasil

def main():
    while True:
        print("\nNim Ganjil")
        print("1. A pangkat B")
        print("2. Hitung 1 - 2/3 + 5/8 - 13/21 + ...")
        print("0. keluar")
        
        pilihan = input("Masukkan :")
        
        if pilihan == "1":
            a = int(input("\nmasukan suatu bilangan bulat :"))
            b = int(input("masukan pangkat yang diinginkan : "))
            
            for i in range(1, b + 1):
                hasil = pangkat_rekursif(a, i)
                print(f"hasil {a} pangkat {i} adalah {hasil}")
        
        elif pilihan == "2":
            n = int(input("\nMasukkan jumlah N : "))
            hasil = hitung_deret(n)
            print(hasil)
        
        elif pilihan == "0":
            print("Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()