import random

def tebak_angka():
    angka_rahasia = random.randint(1, 10)  # Angka rahasia antara 1 hingga 100
    tebakan = 0
    jumlah_tebakan = 0
    
    print("Halo! Mari bermain Tebak Angka.")
    print("Saya memiliki angka antara 1 hingga 10. Coba tebak ya!")

    while tebakan != angka_rahasia:
        tebakan = int(input("Masukkan tebakan Anda: "))
        jumlah_tebakan += 1
        
        if tebakan < angka_rahasia:
            print("Tebakan Anda terlalu rendah. Coba lagi!")
        elif tebakan > angka_rahasia:
            print("Tebakan Anda terlalu tinggi. Coba lagi!")
        else:
            print(f"Selamat! jawabannya adalah {tebakan} anda mengisi {jumlah_tebakan} kali tebakan.")
            break

tebak_angka()
