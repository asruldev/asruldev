# Struktur Kontrol dalam Python

## 1. Percabangan (if-else)
Percabangan digunakan untuk mengeksekusi kode berdasarkan kondisi tertentu.

### Sintaks:
```python
if kondisi:
    # kode yang akan dieksekusi jika kondisi bernilai True
elif kondisi_lain:
    # kode yang akan dieksekusi jika kondisi_lain bernilai True
else:
    # kode yang akan dieksekusi jika semua kondisi di atas False
```

### Contoh:
```python
angka = 10
if angka > 0:
    print("Angka positif")
elif angka < 0:
    print("Angka negatif")
else:
    print("Angka nol")
```

### Latihan:
Buat program yang meminta pengguna memasukkan sebuah angka, lalu cetak apakah angka tersebut ganjil atau genap.

---

## 2. Perulangan (Loop)
Loop digunakan untuk mengulang eksekusi kode selama kondisi tertentu terpenuhi.

### a) Perulangan `for`
Digunakan untuk mengiterasi elemen dalam sebuah koleksi (list, tuple, string, dll.).

#### Sintaks:
```python
for variabel in iterable:
    # kode yang akan dieksekusi
```

#### Contoh:
```python
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
```

### Latihan:
Buat program yang mencetak angka 1 sampai 10 menggunakan `for` loop.

---

### b) Perulangan `while`
Digunakan untuk mengulang eksekusi kode selama kondisi masih `True`.

#### Sintaks:
```python
while kondisi:
    # kode yang akan dieksekusi
```

#### Contoh:
```python
x = 0
while x < 5:
    print(x)
    x += 1  # Increment x
```

### Latihan:
Buat program yang meminta pengguna memasukkan angka hingga pengguna memasukkan angka 0, lalu program berhenti.

---

## 3. Kontrol Perulangan
- `break`: Menghentikan perulangan sebelum waktunya.
- `continue`: Melewatkan iterasi saat ini dan lanjut ke iterasi berikutnya.

### Contoh `break`:
```python
for i in range(10):
    if i == 5:
        break  # Menghentikan loop saat i == 5
    print(i)
```

### Contoh `continue`:
```python
for i in range(5):
    if i == 2:
        continue  # Lewati iterasi saat i == 2
    print(i)
```

### Latihan:
Buat program yang mencetak angka dari 1 hingga 10, tetapi melewatkan angka 5 dengan `continue`.
