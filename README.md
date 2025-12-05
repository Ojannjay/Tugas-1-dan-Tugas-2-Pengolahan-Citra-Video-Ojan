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

1. [Deskripsi Singkat](#deskripsi-singkat)
2. [Tugas 1 – Smoothing, Blurring & Sharpening](#tugas-1--smoothing-blurring--sharpening)
   - [Fitur Utama Tugas 1](#fitur-utama-tugas-1)
   - [Kontrol Keyboard Tugas 1](#kontrol-keyboard-tugas-1)
3. [Tugas 2 – Deteksi Warna HSV](#tugas-2--deteksi-warna-hsv)
   - [Kenapa HSV?](#kenapa-hsv)
   - [Fitur Utama Tugas 2](#fitur-utama-tugas-2)
   - [Kontrol Keyboard Tugas 2](#kontrol-keyboard-tugas-2)
4. [Instalasi & Persiapan](#instalasi--persiapan)
5. [Cara Menjalankan Program](#cara-menjalankan-program)
6. [Konsep Teoretis Singkat](#konsep-teoretis-singkat)
   - [Konvolusi & Kernel dalam Image Processing](#konvolusi--kernel-dalam-image-processing)
   - [Average Blur (Mean Filter)](#average-blur-mean-filter)
   - [Gaussian Blur](#gaussian-blur)
   - [Sharpening (High-Pass Filter)](#sharpening-high-pass-filter)
   - [Ruang Warna BGR vs HSV](#ruang-warna-bgr-vs-hsv)
   - [Operasi Morfologi](#operasi-morfologi)
   - [Kontur](#kontur)
7. [Troubleshooting](#troubleshooting)
8. [Struktur Project](#struktur-project)
9. [Catatan untuk Dosen](#catatan-untuk-dosen)
10. [Informasi Pengembang](#informasi-pengembang)


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

### 🔹 Tugas 2 – Deteksi Warna HSV

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
# Contoh (HTTPS)
```bash
git clone https://github.com/Ojannjay/Tugas-1-dan-Tugas-2-Pengolahan-Citra-Video-Ojan.git
```
```bash
cd Tugas-1-dan-Tugas-2-Pengolahan-Citra-Video-Ojan
```
### 2. Install Dependencies


Menggunakan `requirements.txt`:

```bash
pip install -r requirements.txt
```
Atau install manual (kalau mau simple):
``` bash
pip install opencv-python numpy
```
### 3. Verifikasi Instalansi
Cek apakah OpenCV sudah terpasang dengan benar:
```bash
python -c "import cv2; print('OpenCV Version:', cv2.__version__)"
```
Kalau tidak error dan versi muncul, berarti siap dipakai. ✅

## 🎮 Cara Menjalankan Program

> Jalankan semua perintah dari folder repo setelah proses clone & install selesai.

### Menjalankan Tugas 1 – Smoothing, Blurring & Sharpening

``` bash
python tugas1_blur.py
```

Tips penggunaan:
1. Program akan membuka webcam secara otomatis.
2. Tekan tombol 1–4 untuk mencoba berbagai filter.
3. Tekan 0 untuk kembali ke mode normal (tanpa filter).
4. Tekan q untuk menutup program.

#### Menjalankan Tugas 2 (Deteksi Warna HSV) 🌈
``` bash
python tugas2_HSV.py
```
Kontrol Keyboard Utama:

- **1** → Deteksi objek merah 🔴  
- **2** → Deteksi objek hijau 🟢  
- **3** → Deteksi objek biru 🔵  
- **4** → Deteksi objek kuning 🟡  
- **0** → Mode visualisasi channel HSV (untuk lihat H, S, V secara terpisah)  
- **[** → Perkecil ukuran tampilan jendela mask  
- **]** → Perbesar ukuran tampilan jendela mask  
- **Q** atau **q** → Keluar dari program  

Untuk hasil optimal:

- Gunakan objek dengan warna solid dan pekat.  
- Pastikan pencahayaan cukup (tidak terlalu gelap atau “over-exposure”).  
- Hindari background dengan warna yang sama persis dengan objek.  


## Konsep Teoritis

### 1. Konvolusi & Kernel dalam Image Processing

Secara umum:

$$
G(x, y) = \sum_i \sum_j f(x+i, y+j) \cdot h(i, j)
$$

- $f(x, y)$ : piksel input  
- $h(i, j)$ : kernel / filter  
- $G(x, y)$ : piksel output

### 2. Average Blur (Mean Filter)

Kernel berisi nilai konstan, misalnya 3×3:

$$
K = \frac{1}{9}
\begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}
$$

### 3. Gaussian Blur

Menggunakan distribusi Gaussian 2D:

$$
G(x, y) = \frac{1}{2 \pi \sigma^2} \, e^{-\frac{x^2 + y^2}{2\sigma^2}}
$$

- Piksel di tengah memiliki bobot paling besar.  
- Semakin besar $\sigma$ atau ukuran kernel → semakin blur hasilnya.  
- Lebih natural dan lebih baik menjaga tepi dibanding mean filter.  

---

### 4. Sharpening (High-Pass Filter)

Intinya: **menonjolkan perubahan intensitas (tepi)**.

Dilakukan dengan mengurangi versi blur dari citra asli atau menggunakan kernel seperti:

$$
K =
\begin{bmatrix}
0 & -1 & 0 \\
-1 & 5 & -1 \\
0 & -1 & 0
\end{bmatrix}
$$

- Cocok untuk menajamkan detail setelah proses blur.

### 5. Ruang Warna BGR vs HSV

BGR (Blue, Green, Red)
-Sangat sensitif terhadap perubahan pencahayaan.
-Sulit memisahkan warna dan kecerahan.
-Threshold warna bisa berubah-ubah kalau lighting berubah.

HSV (Hue, Saturation, Value)
-Hue: warna murni (0–179 di OpenCV).
-Saturation: seberapa pekat warna.
-Value: kecerahan.

Keuntungan HSV:
-Mudah mengambil range warna tertentu (contoh: semua piksel dengan Hue sekitar merah).
- Lebih stabil terhadap perubahan lighting moderat.

### 6. Operasi Morfologi

- Bekerja pada citra biner (hitam-putih).

- **Erosion (pengikisan)**
  - Menghapus piksel putih tipis  
  - Mengecilkan objek  
  - Menghilangkan noise kecil  

- **Dilation (peleburan / pelebaran)**
  - Menumbuhkan piksel putih  
  - Memperbesar objek  
  - Menutup gap kecil  

- **Opening = Erosion → Dilation**
  - Menghapus noise kecil tapi menjaga bentuk objek besar  

- **Closing = Dilation → Erosion**
  - Menutup lubang kecil di dalam objek  


### 7. Kontur
Kontur = kurva yang menghubungkan titik-titik di boundary objek dengan intensitas yang sama.
OpenCV:
contours, hierarchy = cv2.findContours(
    mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

Properti penting:
Area: cv2.contourArea(contour)
Perimeter: cv2.arcLength(contour, True)
Bounding Box: cv2.boundingRect(contour)

Di tugas ini, kontur dipakai untuk:
-Menentukan area objek berwarna.
-Menggambar bounding box di sekitar objek.
-Menampilkan teks “MERAH (Area: xxxx)” dsb.

### 🛠 Troubleshooting

**Problem: Webcam tidak terbuka / error `can't grab frame`**

**Solusi:**

- Pastikan tidak ada aplikasi lain yang memakai kamera (Zoom, Meet, OBS, dll).
- Coba ganti index kamera:

cap = cv2.VideoCapture(0)  # coba ganti 1, 2, dst

Cek di pengaturan Windows apakah aplikasi Python diizinkan akses kamera.

Kalau mau nambah problem lain (warna tidak terdeteksi, frame lag, dll) tinggal lanjut di bawahnya dengan pola yang sama:

**Problem: Warna tidak terdeteksi**

**Solusi:**
- Periksa pencahayaan ruangan.
- Gunakan objek dengan warna lebih pekat.
- Sesuaikan kembali rentang HSV di kode.

## 📁 Struktur Project
``` text
Tugas-1-dan-Tugas-2-Pengolahan-Citra-Video-Ojan/
├── tugas1_blur.py     # Implementasi Tugas 1 (smoothing, blurring, sharpen)
├── tugas2_HSV.py      # Implementasi Tugas 2 (deteksi warna HSV + mask)
├── requirements.txt   # Daftar dependencies Python
└── README.md          # Dokumentasi project (file ini)

```
## 📋 Catatan untuk Dosen

### Tugas 1
- ✅ Implementasi Average Blur dengan 2 ukuran kernel (5×5 dan 9×9)
- ✅ Implementasi Gaussian Blur (custom kernel + `cv2.filter2D`)
- ✅ Implementasi Sharpening filter (high-pass)
- ✅ Switching filter secara real-time via keyboard
- ✅ Visual overlay nama mode filter di layar webcam

### Tugas 2
- ✅ Konversi BGR → HSV
- ✅ Thresholding warna untuk 4 warna (merah, hijau, biru, kuning)
- ✅ Operasi morfologi (Opening & Closing) untuk membersihkan mask
- ✅ Deteksi kontur, bounding box, dan label area objek
- ✅ Mode visualisasi HSV / mask untuk pembelajaran
- ✅ Fitur tambahan: ukuran jendela mask dapat diubah dengan tombol `[` dan `]`

## 👨‍💻 Informasi Pengembang

- **Nama**: Nur Rahman Fauzan (Ojan)
- **Mata kuliah**: Pengolahan Citra Video
- **Topik**: Implementasi smoothing, blurring, sharpening, dan deteksi warna HSV berbasis webcam
- **Teknologi**: Python, OpenCV, NumPy
- **Tahun**: 2025
- **Catatan**: Project ini dibuat untuk keperluan akademis (tapi kalau mau coba-coba silakan aja 😄)

