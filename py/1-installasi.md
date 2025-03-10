# Instalasi Python & Virtual Environment

## Pengantar
Python adalah bahasa pemrograman yang populer untuk berbagai keperluan, termasuk pengembangan web, data science, dan otomatisasi. Salah satu praktik terbaik dalam menggunakan Python adalah dengan memanfaatkan **Virtual Environment** untuk mengisolasi dependensi proyek. Dokumen ini akan membahas cara menginstal Python dan mengelola lingkungan virtual.

## 1. Instalasi Python

### Windows
1. **Download Python** dari situs resminya: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. **Jalankan Installer** dan pastikan untuk mencentang opsi **"Add Python to PATH"** sebelum mengklik **Install Now**.
3. **Verifikasi Instalasi**
   ```sh
   python --version
   ```

### macOS
1. **Gunakan Homebrew** (jika belum terinstall, instal Homebrew terlebih dahulu: [https://brew.sh/](https://brew.sh/))
   ```sh
   brew install python
   ```
2. **Verifikasi Instalasi**
   ```sh
   python3 --version
   ```

### Linux (Ubuntu/Debian)
1. **Perbarui repository package**
   ```sh
   sudo apt update && sudo apt upgrade
   ```
2. **Instal Python**
   ```sh
   sudo apt install python3 python3-pip
   ```
3. **Verifikasi Instalasi**
   ```sh
   python3 --version
   ```

## 2. Menggunakan Virtual Environment

### Apa itu Virtual Environment?
Virtual Environment atau **venv** adalah fitur di Python yang memungkinkan kita membuat lingkungan yang terisolasi untuk setiap proyek. Dengan ini, kita dapat menginstal dependensi proyek tanpa mempengaruhi sistem Python secara global.

### Membuat Virtual Environment
1. **Buat direktori proyek (opsional)**
   ```sh
   mkdir my_project && cd my_project
   ```
2. **Buat virtual environment**
   ```sh
   python -m venv venv
   ```
   atau untuk macOS/Linux:
   ```sh
   python3 -m venv venv
   ```

### Mengaktifkan Virtual Environment
- **Windows (Command Prompt)**
  ```sh
  venv\Scripts\activate
  ```
- **Windows (PowerShell)**
  ```sh
  venv\Scripts\Activate.ps1
  ```
- **macOS/Linux**
  ```sh
  source venv/bin/activate
  ```

### Menonaktifkan Virtual Environment
Untuk keluar dari virtual environment, cukup jalankan:
```sh
deactivate
```

## 3. Mengelola Paket dengan Pip

### Instalasi Paket
Gunakan `pip` untuk menginstal paket dalam virtual environment:
```sh
pip install nama_paket
```

### Menyimpan Dependensi
Untuk menyimpan daftar paket yang diinstal agar bisa direplikasi di lingkungan lain:
```sh
pip freeze > requirements.txt
```

### Memasang Dependensi dari File
Jika memiliki `requirements.txt`, instal semua dependensi dengan:
```sh
pip install -r requirements.txt
```

## Kesimpulan
Dengan menggunakan Python Virtual Environment, kita dapat mengelola dependensi proyek dengan lebih rapi dan terisolasi. Ini sangat berguna untuk mencegah konflik antar paket dan memastikan proyek berjalan di lingkungan yang stabil.

---
Dengan mengikuti panduan ini, Anda dapat menginstal Python dan menggunakan virtual environment dengan mudah. 🚀

## Latihan
Coba lakukan langkah-langkah berikut:
1. Instal Python sesuai dengan sistem operasi Anda.
2. Buat sebuah direktori proyek dan buat virtual environment di dalamnya.
3. Aktifkan virtual environment dan instal paket `requests`.
4. Simpan daftar dependensi ke dalam file `requirements.txt`.
5. Nonaktifkan virtual environment dan coba aktifkan kembali.

## Soal Pilihan Ganda
**1. Apa fungsi dari Virtual Environment dalam Python?**  
A. Mempercepat eksekusi program  
B. Mengisolasi dependensi proyek  
C. Menambah fitur baru ke Python  
D. Menghapus paket yang tidak diperlukan  
**Jawaban:** B  

**2. Perintah yang digunakan untuk membuat Virtual Environment adalah?**  
A. `python -m create_venv venv`  
B. `python -m venv venv`  
C. `python -m virtual_env venv`  
D. `python -create venv`  
**Jawaban:** B  

**3. Bagaimana cara mengaktifkan Virtual Environment di Windows menggunakan Command Prompt?**  
A. `source venv/bin/activate`  
B. `activate venv`  
C. `venv\Scripts\activate`  
D. `python activate venv`  
**Jawaban:** C  

**4. Apa perintah yang digunakan untuk menonaktifkan Virtual Environment?**  
A. `exit`  
B. `quit`  
C. `deactivate`  
D. `stop venv`  
**Jawaban:** C  

**5. Apa perintah yang digunakan untuk menyimpan daftar dependensi dalam Virtual Environment?**  
A. `pip list > dependencies.txt`  
B. `pip save > requirements.txt`  
C. `pip freeze > requirements.txt`  
D. `pip install -r requirements.txt`  
**Jawaban:** C

