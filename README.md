# Deployment Aplikasi Estimasi Harga Daging Ayam dengan Model Regresi Linier Berganda

![image](https://user-images.githubusercontent.com/70785427/135196237-6b11d2a8-40d9-4e63-80d2-db9c985b6212.png)

## Deskripsi singkat

Repository ini berisi semua file yang dibutuhkan untuk melakukan deployment aplikasi estimasi harga daging ayam berbasis model Regresi Linier Berganda . 
Dataset yang digunakan adalah data timeseries, harga kebutuhan pokok masyarakat (Kepokmas) di Jawa Tengah, yang tersedia di https://data.go.id/pemerintah-provinsi-jawa-tengah?q=kepokmas. Di antara puluhan komoditas pangan yang terdaftar di dataset, harga daging ayam menjadi fokus penerapan model karena harga dimaksud bersifat sangat fluktuatif.
Model ini mengestimasi harga ayam di Kota Semarang besok hari, dengan mempelajari data di lima pasar di Jawa Tengah.

## Sekilas mengenai model

Harga daging ayam di kota Semarang BESOK, diwakili variabel y, diestimasi dengan harga daging ayam HARI INI di lima pasar yang masing-masing diwakili dengan variabelx1, x2, x3, x4 dan x5, atau:

y = a + bx1 + cx2 + dx3 + ex4 + fx5

dimana, a adalah nilai intereception dari model, dan b, c, d, e, dan f adalah koefisien regresi untu tiap variabel x1 sd. x5


## URL, Folder, file, dan kegunaannya

-  URL dari aplikasi estimasi ini: http://prediksi-harga-daging-ayam.herokuapp.com/
-  Hosting aplikasi dilakukan di Heroku dengan semua file dan folder diletakkan di Github ini
-  Folder dan isinya:
-   /
    -   app.py --> Berisi konfigurasi route untuk API
    -   model_LR_ayam.pkl --> Model Regresi Linier yang sudah di-training, disimpan dengan librari pickle
    -   request.py --> Berisi percobaan pemanggilan API dengan payload data JSON
    -   requirements.txt --> Berisi daftar dependency/package Python yang diperlukan untuk menjalankan API dan model Regresi Linier
-   templates/
    -   index.html --> Berisi template halaman pertama dari aplikasi web yang dirender dengan app.py. 
    -   Nilai variabel xi (harga di pasar) yang diinput dari index.html dibaca dan diproses oleh app.py.
    -   Estimasi harga dilakukan di app.py
    -   Hasil dari app.py berupa estimasi harga ditampilkan kembali di index.html

## Cara menjalankan API pada komputer Anda

### Menjalankan API

1. Pastikan Anda sudah menginstall Anaconda. 
2. Buka terminal/command prompt/power shell Anaconda
3. Buat virtual environment dengan perintah "conda create -n <nama-environment> python=3.9" (sesuaikan dengan versi python anda)
4. Aktifkan virtual environment dengan "conda activate <nama-environment>"
5. Install semua dependency/package Python dengan "pip install -r requirements.txt"
6. Jalankan API menggunakan perintah "python app.py"

### Akses melalui Website

    Setelah API berjalan:
1. Anda akan diberikan URL untuk membuka website berupa `localhost:5000/` atau `127.0.0.1:5000/`
2. Buka URL dengan browser, coba masukkan harga daging di lima pasar, kemudian klik _Prediksi Sekarang_
3. Anda akan diberikan harga yang diestimasi pada sisi kanan halaman web
