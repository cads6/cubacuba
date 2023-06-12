def konversi_celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def konversi_fahrenheit_ke_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius

def konversi_celcius_ke_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

def konversi_kelvin_ke_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius

def konversi_fahrenheit_ke_kelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return kelvin

def konversi_kelvin_ke_fahrenheit(kelvin):
    fahrenheit = kelvin * 9/5 - 459.67
    return fahrenheit

# Meminta pengguna memasukkan suhu
suhu = float(input("Masukkan suhu: "))
satuan = input("Masukkan satuan suhu (C untuk Celcius, F untuk Fahrenheit, K untuk Kelvin): ")

if satuan == "C" or satuan == "c":
    fahrenheit = konversi_celcius_ke_fahrenheit(suhu)
    kelvin = konversi_celcius_ke_kelvin(suhu)
    print(f"{suhu} derajat Celcius = {fahrenheit} derajat Fahrenheit")
    print(f"{suhu} derajat Celcius = {kelvin} Kelvin")
elif satuan == "F" or satuan == "f":
    celcius = konversi_fahrenheit_ke_celcius(suhu)
    kelvin = konversi_fahrenheit_ke_kelvin(suhu)
    print(f"{suhu} derajat Fahrenheit = {celcius} derajat Celcius")
    print(f"{suhu} derajat Fahrenheit = {kelvin} Kelvin")
elif satuan == "K" or satuan == "k":
    celcius = konversi_kelvin_ke_celcius(suhu)
    fahrenheit = konversi_kelvin_ke_fahrenheit(suhu)
    print(f"{suhu} Kelvin = {celcius} derajat Celcius")
    print(f"{suhu} Kelvin = {fahrenheit} derajat Fahrenheit")
else:
    print("Satuan suhu tidak valid. Mohon masukkan C, F, atau K.")
