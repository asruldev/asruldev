# 📌 Variabel & Tipe Data dalam Pemrograman

## 🔹 Apa itu Variabel?
Variabel adalah tempat menyimpan nilai/data dalam program. Setiap variabel memiliki **nama** dan dapat menyimpan berbagai jenis **data**.

### Contoh:
```python
nama = "Asrul"  # Variabel dengan nilai string
umur = 25        # Variabel dengan nilai angka
is_online = True # Variabel dengan nilai boolean
```

## 🔹 Tipe Data dalam Pemrograman
Tipe data menentukan jenis nilai yang bisa disimpan dalam variabel. Berikut beberapa tipe data umum:

### 1️⃣ **Tipe Data Primitif** (Sederhana)
| Tipe Data  | Deskripsi |
|------------|------------|
| **String**  | Teks, ditulis dalam tanda kutip (`"` atau `'`) |
| **Integer**  | Angka bulat |
| **Float**  | Angka desimal |
| **Boolean** | Hanya `True` atau `False` |
| **NoneType** | Nilai kosong/tidak ada (`None`) |

#### Contoh:
```python
teks = "Halo!"    # String
angka = 42       # Integer
angka_desimal = 3.14  # Float
is_active = False # Boolean
kosong = None    # NoneType
```

### 2️⃣ **Tipe Data Kompleks** (Referensi)
| Tipe Data | Deskripsi |
|-----------|------------|
| **List**  | Kumpulan data dalam satu variabel |
| **Dictionary** | Struktur data dengan pasangan kunci-nilai |

#### Contoh:
```python
hobi = ["Membaca", "Ngoding", "Olahraga"] # List

orang = {  # Dictionary
  "nama": "Asrul",
  "umur": 25,
  "pekerjaan": "Developer"
}
```

## 🎯 Kesimpulan
- Variabel adalah wadah untuk menyimpan data.
- Setiap variabel memiliki **tipe data** yang menentukan jenis nilai yang dapat disimpan.
- Ada **tipe primitif** (string, integer, float, boolean, NoneType) dan **tipe kompleks** (list, dictionary).

🔗 **Tips**: Gunakan `snake_case` untuk penamaan variabel di Python! 🚀

---

## 🎯 Latihan
Coba buat variabel dengan tipe data berbeda dan cetak hasilnya!

### Soal 1:
Buat variabel berikut:
- `nama` dengan nilai nama Anda
- `usia` dengan umur Anda
- `tinggi` dengan tinggi badan Anda (gunakan float)
- `is_student` dengan nilai `True` jika Anda masih belajar

Cetak semua variabel tersebut.

#### 💡 Contoh Output yang Diharapkan:
```python
Nama: Asrul
Usia: 25 tahun
Tinggi: 170.5 cm
Mahasiswa: True
```

### Soal 2:
Buat list berisi 3 makanan favorit Anda dan dictionary berisi informasi tentang diri Anda.

**Selamat mencoba! 🚀**
