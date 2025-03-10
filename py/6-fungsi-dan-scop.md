# Fungsi & Scope dalam Python

## 1. Pengertian Fungsi
Fungsi adalah blok kode yang dapat digunakan kembali untuk melakukan tugas tertentu. Fungsi membantu dalam membuat kode lebih modular, mudah dibaca, dan mengurangi redundansi.

### Sintaks Dasar Fungsi
```python
# Definisi fungsi
def nama_fungsi(parameter1, parameter2):
    """Dokumentasi fungsi"""
    hasil = parameter1 + parameter2
    return hasil

# Pemanggilan fungsi
hasil_penjumlahan = nama_fungsi(5, 3)
print(hasil_penjumlahan)  # Output: 8
```

## 2. Jenis-Jenis Fungsi
### a. Fungsi Tanpa Parameter
```python
def sapa():
    print("Halo, selamat datang!")

sapa()  # Output: Halo, selamat datang!
```

### b. Fungsi dengan Parameter
```python
def tambah(a, b):
    return a + b

print(tambah(3, 4))  # Output: 7
```

### c. Fungsi dengan Nilai Default
```python
def salam(nama="User"):
    print(f"Halo, {nama}!")

salam()  # Output: Halo, User!
salam("Asrul")  # Output: Halo, Asrul!
```

### d. Fungsi dengan Return
```python
def kuadrat(x):
    return x ** 2

print(kuadrat(5))  # Output: 25
```

## 3. Scope (Lingkup Variabel)
Scope menentukan di mana variabel dapat diakses dalam program. Ada dua jenis utama scope:

### a. Variabel Lokal
Variabel yang dideklarasikan di dalam fungsi dan hanya bisa digunakan dalam fungsi tersebut.
```python
def contoh_lokal():
    x = 10  # Variabel lokal
    print(x)

contoh_lokal()  # Output: 10
print(x)  # Error: NameError: name 'x' is not defined
```

### b. Variabel Global
Variabel yang dideklarasikan di luar fungsi dan bisa diakses dalam dan luar fungsi.
```python
x = 20  # Variabel global

def contoh_global():
    print(x)  # Bisa mengakses variabel global

contoh_global()  # Output: 20
print(x)  # Output: 20
```

### c. Menggunakan `global`
```python
x = 5

def ubah_global():
    global x
    x = 10

ubah_global()
print(x)  # Output: 10
```

## 4. Latihan
### Latihan 1: Buat fungsi untuk menghitung luas persegi panjang
Buat fungsi `luas_persegi_panjang(panjang, lebar)` yang mengembalikan luasnya.
```python
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Uji fungsi
print(luas_persegi_panjang(5, 10))  # Output: 50
```

### Latihan 2: Buat fungsi untuk mengecek bilangan ganjil atau genap
Buat fungsi `cek_ganjil_genap(angka)` yang mencetak "Ganjil" jika angka ganjil dan "Genap" jika angka genap.
```python
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        print("Genap")
    else:
        print("Ganjil")

# Uji fungsi
cek_ganjil_genap(7)  # Output: Ganjil
cek_ganjil_genap(10)  # Output: Genap
```

## 5. Soal Praktik
1. Buat fungsi `faktorial(n)` untuk menghitung faktorial dari `n`.
2. Buat fungsi `pangkat(x, y)` yang menghitung `x` pangkat `y`.
3. Buat fungsi `konversi_suhu(celcius)` yang mengubah suhu dari Celcius ke Fahrenheit `(F = C * 9/5 + 32)`.
