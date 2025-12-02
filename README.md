# 🎥 Tugas 1 & Tugas 2 – Pengolahan Citra Video

Repo ini berisi implementasi dua tugas mata kuliah **Pengolahan Citra Video**:

- **Tugas 1:** Smoothing, Blurring, dan Sharpening dari webcam  
- **Tugas 2:** Deteksi objek berdasarkan warna menggunakan ruang warna **HSV**

Dibuat dengan fokus ke:
- Real-time processing dari webcam
- Kode yang rapi dan mudah dibaca
- Kontrol keyboard yang jelas dan enak dipakai saat demo

---

## 📚 Daftar Isi

1. [Deskripsi Singkat](#-deskripsi-singkat)
2. [Tugas 1 – Smoothing, Blurring & Sharpening](#-tugas-1--smoothing-blurring--sharpening)
   - [Fitur Tugas 1](#fitur-utama-tugas-1)
   - [Kontrol Keyboard Tugas 1](#kontrol-keyboard-tugas-1)
3. [Tugas 2 – Deteksi Warna HSV](#-tugas-2--deteksi-warna-hsv)
   - [Kenapa HSV?](#kenapa-hsv)
   - [Fitur Tugas 2](#fitur-utama-tugas-2)
   - [Kontrol Keyboard Tugas 2](#kontrol-keyboard-tugas-2)
4. [Instalasi & Persiapan](#-instalasi--persiapan)
5. [Cara Menjalankan Program](#-cara-menjalankan-program)
6. [Konsep Teoretis Singkat](#-konsep-teoretis-singkat)
7. [Troubleshooting](#-troubleshooting)
8. [Struktur Project](#-struktur-project)
9. [Catatan & Lisensi](#-catatan--lisensi)

---

## 📝 Deskripsi Singkat

Project ini memanfaatkan **OpenCV** dan **NumPy** untuk:

- Mengaplikasikan berbagai **filter spasial** (average blur, Gaussian blur, sharpening) pada video dari webcam secara real-time.
- Mendeteksi objek berwarna (**merah, hijau, biru, kuning**) menggunakan ruang warna **HSV**, kemudian:
  - Membuat **mask biner**
  - Membersihkan noise dengan **operasi morfologi**
  - Menggambar **bounding box** dan area kontur pada objek yang terdeteksi
  - Menampilkan **preview mask** yang bisa di-*resize* dengan keyboard

Semua interaksi user dilakukan via **keyboard** sehingga mudah untuk dipresentasikan di kelas/lab.

---

## 🔹 Tugas 1 – Smoothing, Blurring & Sharpening

File utama: **`tugas1_blur.py`**

Tugas 1 fokus ke implementasi beberapa jenis **spatial filtering** untuk smoothing dan sharpening citra video dari webcam.

### Fitur Utama Tugas 1

- 🔁 **Mode Normal** – menampilkan video asli tanpa filter
- 🧊 **Average Blur 5×5** – smoothing sederhana dengan kernel 5×5
- 🧊 **Average Blur 9×9** – smoothing lebih kuat dengan kernel 9×9
- 🌫 **Gaussian Blur (custom)**  
  - Kernel Gaussian dibuat dengan `cv2.getGaussianKernel()`  
  - Di-*expand* ke 2D dan diaplikasikan dengan `cv2.filter2D()`  
  - Menunjukkan pemahaman operasi konvolusi, bukan sekadar `cv2.GaussianBlur`
- ✨ **Sharpening Filter** – menajamkan detail dengan kernel high-pass
- 🧾 **HUD di layar**:
  - Menampilkan **nama filter aktif**
  - Menampilkan **bantuan kontrol** di bagian bawah frame

### Kontrol Keyboard Tugas 1

| Tombol | Fungsi                                      |
|--------|---------------------------------------------|
| `0`    | Mode normal (tanpa filter)                 |
| `1`    | Average Blur 5×5                           |
| `2`    | Average Blur 9×9                           |
| `3`    | Gaussian Blur (custom kernel)              |
| `4`    | Sharpen (penajaman)                        |
| `q`    | Keluar dari program                        |

---

## 🔹 Tugas 2 – Deteksi Warna HSV

File utama: **`tugas2_HSV.py`**

Tugas 2 mengimplementasikan sistem deteksi objek berdasarkan **warna** dengan memanfaatkan ruang warna **HSV**.

### Kenapa HSV?

Ruang warna **BGR/RGB** cukup sensitif terhadap perubahan intensitas cahaya; nilai warna dan kecerahan bercampur, sehingga thresholding jadi sulit dan tidak konsisten.

Ruang warna **HSV (Hue, Saturation, Value)** memisahkan:

- **H (Hue)** → jenis warnanya (merah, hijau, biru, kuning, dll)
- **S (Saturation)** → seberapa pekat warnanya
- **V (Value)** → seberapa terang warnanya

Ini membuat **deteksi warna lebih stabil** saat kondisi pencahayaan berubah.

### Fitur Utama Tugas 2

- 🔄 **Switch warna real-time**:
  - Merah
  - Hijau
  - Biru
  - Kuning
- 🎯 **Color thresholding** dengan `cv2.inRange()` pada ruang HSV
- 🧹 **Operasi morfologi (opsional di kode)**:
  - Opening / closing untuk menghilangkan noise kecil dan menutup lubang
- 📦 **Deteksi kontur & bounding box**:
  - Menggunakan `cv2.findContours()`
  - Menggambar **bounding box** untuk tiap objek yang terdeteksi
  - Menampilkan **label warna + luas area** di atas objek
- 🪟 **Jendela Mask terpisah yang bisa di-*resize***:
  - Menampilkan hasil mask biner (putih = objek, hitam = background)
  - Ukuran mask **bisa diperbesar/diperkecil** dengan keyboard:
    - `[` → perkecil skala mask
    - `]` → perbesar skala mask
- 👀 **Mode “tidak ada deteksi”**:
  - Mematikan semua thresholding dan hanya menampilkan video biasa
  - Berguna untuk membandingkan sebelum/sesudah deteksi

### Kontrol Keyboard Tugas 2

| Tombol | Fungsi                                   |
|--------|------------------------------------------|
| `1`    | Deteksi warna **merah**                 |
| `2`    | Deteksi warna **hijau**                 |
| `3`    | Deteksi warna **biru**                  |
| `4`    | Deteksi warna **kuning**                |
| `0`    | Mode **tanpa deteksi** (normal)         |
| `[`    | Perkecil ukuran tampilan jendela mask   |
| `]`    | Perbesar ukuran tampilan jendela mask   |
| `q`    | Keluar dari program                     |

---

## 🚀 Instalasi & Persiapan

### Prasyarat

- Python **3.7 atau lebih baru**
- `pip` sudah terinstall
- Webcam (built-in laptop atau USB)
- Sistem operasi: Windows / Linux / macOS

### 1. Clone / Download Repo

```bash
# Contoh (HTTPS)
git clone https://github.com/Ojannjay/Tugas-1-dan-Tugas-2-Pengolahan-Citra-Video-Ojan.git

cd Tugas-1-dan-Tugas-2-Pengolahan-Citra-Video-Ojan
