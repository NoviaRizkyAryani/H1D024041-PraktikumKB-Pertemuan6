# Jaringan Syaraf Tiruan - Praktikum KB (Pertemuan 6)

Repositori ini berisi implementasi dari algoritma Jaringan Syaraf Tiruan (JST) dasar menggunakan bahasa pemrograman Python. Terdapat dua jenis algoritma yang diimplementasikan: **Perceptron** dan **Backpropagation**, yang masing-masing digunakan untuk menyelesaikan masalah gerbang logika sederhana dengan representasi nilai Bipolar.

---

## Struktur Direktori

Berikut adalah penjelasan mengenai file-file yang ada pada folder ini:

### 1. Perceptron (Logika OR)
- **`Perceptron.py`**: Merupakan modul yang memuat kelas `Perceptron`. Modul ini menangani proses pelatihan (*training*) menggunakan aturan *Delta Rule* untuk mengupdate bobot dan bias. File ini juga menyediakan fungsi untuk memvisualisasikan garis pemisah (*decision boundary*) pada setiap iterasi (*epoch*).
- **`Perceptron_or.py`**: Merupakan script utama (*runner*) untuk menjalankan model Perceptron guna memecahkan masalah gerbang logika **OR** menggunakan nilai Bipolar (1 dan -1). Script ini mengatur *learning rate* (`alpha`) dan maksimal epoch.
- **`Hasil Perceptron.txt`**: File teks ini dihasilkan secara otomatis saat script dijalankan. File ini mencatat detail proses pelatihan setiap epoch, meliputi input, target, hasil prediksi, error, update bobot, update bias, serta *Sum Square Error* (SSE).

### 2. Backpropagation (Logika XOR)
- **`Backpropagation.py`**: Merupakan modul yang memuat kelas `Backpropagation`. Modul ini mengimplementasikan algoritma propagasi balik dengan 2 neuron pada *hidden layer* dan menggunakan fungsi aktivasi *Bipolar Sigmoid* (tanh). File ini juga menampilkan plot penurunan error setiap epoch menggunakan *matplotlib*.
- **`Backpropagation_xor.py`**: Merupakan script utama (*runner*) untuk menjalankan model Backpropagation guna memecahkan masalah gerbang logika **XOR** menggunakan nilai Bipolar. Masalah XOR tidak bisa diselesaikan oleh Perceptron biasa karena datanya tidak dapat dipisahkan secara linear (*non-linearly separable*).
- **`hasilBackpropagation.txt`**: File teks ini dihasilkan secara otomatis dan mencatat seluruh tahapan perhitungan secara detail pada setiap iterasi. Laporan yang dicatat mencakup:
  - Inisialisasi awal (input, target, bobot awal, bias awal, parameter *learning rate*, dan max epoch).
  - Tahapan *Forward Propagation* (operasi input ke hidden, aktivasi hidden, operasi hidden ke output, aktivasi output).
  - Tahapan *Backward Propagation* (perhitungan error, *delta* output, *error* hidden, *delta* hidden).
  - Pembaruan (*update*) bobot dan bias secara mendetail setiap iterasi datanya.
  - Nilai *Sum Square Error* (SSE) tiap epoch, serta kesimpulan alasan berhentinya proses pelatihan dan bobot akhirnya.

---

## Prasyarat
Untuk menjalankan script ini, pastikan telah menginstal beberapa pustaka (*library*) Python berikut:
`pip install numpy matplotlib`

## Cara Menjalankan
- Untuk Perceptron (OR)
  jalankan perintah berikut di terminal:
  `python Perceptron_or.py` (Grafik akan muncul. Tutup jendela grafik agar pelatihan dapat lanjut ke epoch berikutnya)
- Untuk Backpropagation (XOR)
  jalankan perintah berikut di terminal:
  `python Backpropagation_xor.py` (Setelah proses pelatihan selesai, periksa tahapan perhitungannya di hasilBackpropagation.txt dan grafik penurunan error akan ditampilkan)

Kedua algoritma akan berhenti melakukan iterasi secara otomatis apabila target error (atau SSE = 0 untuk kasus Perceptron) telah tercapai, atau jika epoch telah mencapai batas maksimum yang ditentukan pada script runner.
  
  
