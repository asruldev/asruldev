# **Struktur Dasar Python**

Python adalah bahasa pemrograman yang mudah dipahami karena sintaksnya sederhana. Berikut adalah konsep dasar dalam penulisan kode Python.

---

## **1. Syntax Python**

Python menggunakan sintaks yang mudah dibaca. Contoh sederhana untuk mencetak teks:

```python
print("Hello, World!")
```
Kode di atas akan menampilkan:

```
Hello, World!
```

---

## **2. Indentation (Indentasi)**

Python menggunakan indentasi (spasi atau tab) untuk menandai blok kode. Jika tidak menggunakan indentasi yang benar, program akan error.

✅ **Contoh benar:**
```python
if 5 > 2:
    print("Lima lebih besar dari dua")
```

❌ **Contoh salah (akan error):**
```python
if 5 > 2:
print("Lima lebih besar dari dua")  # Tidak ada indentasi
```

Error yang muncul:
```
IndentationError: expected an indented block
```

---

## **3. Variabel dan Tipe Data**

Python tidak memerlukan deklarasi tipe data secara eksplisit.

```python
x = 10         # Integer
y = 3.14       # Float
name = "Asrul" # String
is_python_fun = True # Boolean
```

Kita bisa mengecek tipe data dengan `type()`, contoh:

```python
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(name))  # Output: <class 'str'>
print(type(is_python_fun))  # Output: <class 'bool'>
```

---

## **Latihan: Perbaiki Kode yang Salah**

Coba perbaiki kode berikut yang memiliki kesalahan indentasi:

```python
x = 5
if x > 3:
print("X lebih besar dari 3")
```

✅ **Perbaikan yang benar:**
```python
x = 5
if x > 3:
    print("X lebih besar dari 3")  # Tambahkan indentasi
```

---

## **Soal Pilihan Ganda**

### **1. Apa fungsi dari indentasi dalam Python?**
a) Mempercepat eksekusi program  
b) Membuat kode lebih menarik  
c) Menentukan blok kode dalam Python  
d) Tidak memiliki fungsi apa pun  

**✅ Jawaban:** c) Menentukan blok kode dalam Python  

---

### **2. Apa yang akan terjadi jika kita tidak menggunakan indentasi yang benar dalam Python?**
a) Program tetap berjalan normal  
b) Program akan memberikan hasil yang salah  
c) Python akan memberikan `IndentationError`  
d) Tidak ada yang terjadi  

**✅ Jawaban:** c) Python akan memberikan `IndentationError`  

---

### **3. Manakah pernyataan berikut yang benar tentang variabel di Python?**
a) Harus dideklarasikan dengan tipe data  
b) Harus ditulis dengan huruf kapital  
c) Bisa berubah tipe data saat program berjalan  
d) Tidak bisa diubah setelah dideklarasikan  

**✅ Jawaban:** c) Bisa berubah tipe data saat program berjalan  
