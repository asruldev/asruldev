# Operasi Dasar dalam Python

## 1. Operasi Aritmatika
Operasi aritmatika adalah operasi dasar matematika yang dapat dilakukan pada angka.

| Operator | Deskripsi        | Contoh          |
|----------|----------------|----------------|
| `+`      | Penjumlahan    | `5 + 3 = 8`    |
| `-`      | Pengurangan    | `5 - 3 = 2`    |
| `*`      | Perkalian      | `5 * 3 = 15`   |
| `/`      | Pembagian      | `5 / 2 = 2.5`  |
| `//`     | Pembagian Bulat| `5 // 2 = 2`   |
| `%`      | Modulus (Sisa) | `5 % 2 = 1`    |
| `**`     | Pangkat        | `5 ** 2 = 25`  |

### Latihan
Coba jalankan kode berikut dan lihat hasilnya:
```python
x = 10
y = 3

print(x + y)  # Penjumlahan
print(x - y)  # Pengurangan
print(x * y)  # Perkalian
print(x / y)  # Pembagian
print(x // y) # Pembagian bulat
print(x % y)  # Modulus
print(x ** y) # Pangkat
```

## 2. Operasi Perbandingan
Operasi perbandingan digunakan untuk membandingkan dua nilai dan menghasilkan nilai boolean (`True` atau `False`).

| Operator | Deskripsi                 | Contoh         |
|----------|-------------------------|---------------|
| `==`     | Sama dengan              | `5 == 5` (True) |
| `!=`     | Tidak sama dengan        | `5 != 3` (True) |
| `>`      | Lebih besar dari         | `5 > 3` (True)  |
| `<`      | Lebih kecil dari         | `5 < 3` (False) |
| `>=`     | Lebih besar atau sama dengan | `5 >= 5` (True) |
| `<=`     | Lebih kecil atau sama dengan | `5 <= 3` (False) |

### Latihan
Coba jalankan kode berikut:
```python
a = 7
b = 5

print(a == b)  # Sama dengan
print(a != b)  # Tidak sama dengan
print(a > b)   # Lebih besar
print(a < b)   # Lebih kecil
print(a >= b)  # Lebih besar atau sama dengan
print(a <= b)  # Lebih kecil atau sama dengan
```

## 3. Operasi Logika
Operasi logika digunakan untuk mengkombinasikan ekspresi boolean.

| Operator | Deskripsi                     | Contoh               |
|----------|-----------------------------|----------------------|
| `and`    | True jika kedua nilai True  | `True and False` (False) |
| `or`     | True jika salah satu nilai True | `True or False` (True) |
| `not`    | Membalik nilai boolean      | `not True` (False)   |

### Latihan
Coba jalankan kode berikut:
```python
p = True
q = False

print(p and q)  # False
print(p or q)   # True
print(not p)    # False
```

## Soal Latihan
1. Hitung hasil dari `8 + 4 * 2 - 10 / 2`
2. Tentukan hasil dari `10 % 3 == 1`
3. Jika `x = 6` dan `y = 8`, apakah `x * 2 >= y`?
4. Tentukan hasil dari `not (5 > 3 and 2 < 4)`

Coba tuliskan kode Python untuk menjawab soal-soal di atas! 🚀

