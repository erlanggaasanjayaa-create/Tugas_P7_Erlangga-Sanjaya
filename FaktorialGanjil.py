def pangkat (a, b):
    if b == 0:
        return 1
    else:
        return a * pangkat(a, b - 1)

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

def hitung_deret(n, i=1):
    if i > n:
        return 0
    
    pembilang = fibo(2*i - 1)
    penyebut = fibo(2*i)
    
    term = pembilang / penyebut
    
    if i % 2 == 0:
        return -term + hitung_deret(n, i + 1)
    else:
        return term + hitung_deret(n, i + 1)

while True:
    print("\n Nim Ganjil")
    print("1. A pangkat B")
    print("2. Hitung 1 - 2/3 + 5/8 - 13/21 + ...")
    print("0. Keluar")
    
    pilihan = int(input("Masukkan : "))
    
    if pilihan == 1:
        bil = int(input("Masukkan Bilangan Bulat : "))
        pangkat_input = int(input("Masukkan Pangkat yang Anda Inginkan : "))

        for j in range(1, pangkat_input + 1):
            print(f"hasil {bil} pangkat {j} adalah {pangkat(bil, j)}")
            
    elif pilihan == 2:
        n_deret = int(input("Masukkan jumlah N : "))
        hasil = hitung_deret(n_deret)
        print(f"{hasil:.6f}")
        
    elif pilihan == 0:
        print("Alhamdulillah kelar cuy!")
        break
    else:
        print("Pilihan yang Anda pilih tidak valid!")