# Plant-Clinic : A Web Application for Plant Diseases Classification and Recommendation with Convolutional Neural Network

# Accuracy Model Mencapai 94%

![Poster Tubes DTI](https://github.com/ds-dti/DS02_03_Plant-Clinic/blob/master/Poster-1.png)

Web Application ini merupakan sebuah hasil dari project akhir yang kami selesaikan pada Digital Talent Incubator (DTI) 2020 yang ditujukan untuk membantu para petani bahkan masyarakat umum yang ingin bercocok tanam namun masih ragu apa yang harus dilakukan jika tanaman tersebut terkena sebuah penyakit.

Berikut adalah Anggota dari Tim Plant-Clinic:
- Muhammad Apriandito (Mentor)
- Muhamad Irfan Fadhullah
- Ryandhika Fauzan M
- Amalia Ristantya
- Garry Putranto A

## Latar Belakang
Indonesia merupakan negara yang diberkahi dengan kondisi alam yang sangat subur. Tentunya, kondisi alam ini dimanfaatkan oleh banyak orang untuk bercocok tanam, baik bertani ataupun berkebun. Ada yang menjadikannya sebagai pekerjaan utama, dan ada pula yang menjadikannya sebagai hobi, terutama di tengah pandemi COVID-19. Himbauan pemerintah untuk beraktivitas #DiRumahSaja meningkatkan aktivitas bercocok tanam baik sekedar untuk mempercantik halaman rumah ataupun untuk mendapatkan sumber buah dan sayuran yang terjamin kualitasnya.
Sebagai tech enthusiasts, fenomena ini sangat menarik bagi kami. Mengawinkan sektor pertanian dengan teknologi selalu menjadi sebuah peluang yang terbuka untuk berbakti pada negeri. Kami tidak menyetujui pandangan bahwa sektor pertanian dan perkebunan merupakan sektor yang digiati oleh masyarakat kelas ekonomi menengah ke bawah saja, kami yakin bahwa dengan teknologi yang tepat, hasil pertanian pun akan semakin baik kualitasnya, semakin besar kuantitasnya, dan semakin luar biasa dampaknya bagi perekonomian negara. Sebuah jalan bagi kami yang ingin berbakti pada negeri kami yang tercinta.
Karena itu, sebagai pegiat data science, kami mencoba berkontemplasi, bisa tidak ya, mengolah dan memanfaatkan data yang tersedia untuk menghasilkan produk yang dapat digunakan untuk mendukung aktivitas bercocok tanam? Ternyata, bisa! Memperkenalkan produk karya kami, Plant Clinic. 

## Konsep
Plant Clinic merupakan sebuah web app yang dapat mendeteksi penyakit pada tanaman. Dengan fitur image recognition, jika kita mengunggah foto tanaman kita ke website ini, komputer dapat mendeteksi apakah tanaman kita sehat atau sakit. Kemudian, seandainya sakit, tentu akan timbul pertanyaan, penyakit apakah yang menyerang tanaman ini? Apa penyebabnya? Bagaimana cara menanganinya? Kemudian, bagaimana cara mencegahnya sehingga tidak menyerang lagi di masa depan? Semuanya dapat ditemukan di website ini. Sejauh ini, tanaman yang bisa dideteksi penyakitnya adalah apel, ceri, jagung, anggur, persik, paprika, kentang, stroberi, dan tomat. Tentu saja, kami senantiasa mengumpulkan informasi tentang tanaman lainnya, karena semakin banyak jenis tanaman yang dapat terdeteksi, dan semakin banyak data, tentu saja hasil kerja produk kami akan semakin baik.

## Tujuan
Pengembangan produk ini mendukung usaha pemerintah Indonesia dalam mencapai Sustainable Development Goals atau SDG yang diharapkan akan tercapai seluruhnya pada tahun 2030. Secara langsung, proyek ini mendukung pencapaian Tujuan ke-15 yaitu Ekosistem Daratan, dan secara tidak langsung, proyek ini mendukung pencapaian Tujuan ke-2 (Tanpa Kelaparan), Tujuan ke-8 (Pekerjaan Layak dan Pertumbuhan Ekonomi), serta Tujuan ke-12 (Konsumsi dan Produksi yang Bertanggung Jawab). Kami menyadari bahwa mencapai ke-17 tujuan SDG ini mungkin terlihat sangat sulit untuk tercapai. Namun, kami percaya, jika setiap kalangan masyarakat berusaha sesuai dengan keahlian mereka masing-masing, mencapai ke-17 tujuan tersebut bukanlah hal yang mustahil. Ini adalah kontribusi kami, Kontribusi Data Scientist untuk UN Sustainable Development Goals 2030.

## Arsitektur Model Plant-Clinic
Model yang ada dibalik Plant-Clinic menggunakan arsitektur Convolutional Neural Network (CNN). CNN adalah salah satu jenis arsitektur neural network yang biasa digunakan pada data image yang merupakan basis dari model yang Plant-Clinic. Kemampuan utama CNN adalah arsitektur yang mampu mengenali informasi prediktif suatu objek (gambar, teks, potongan suara, dan sebagainya) walaupun objek tersebut dapat diposisikan dimana saja pada input. Kontribusi CNN di feature extraction layer adalah pada convolution dan pooling layer. Convolution bekerja dengan prinsip sliding window dan weight sharing (mengurangi kompleksitas perhitungan). Pooling layer digunakan untuk merangkum informasi yang dihasilkan oleh suatu convolution (mengurangi dimensi). Sedangkan vektor hasil dari beberapa operasi convolution dan pooling pada multilayer perceptron dikenal sebagai fully-connected layer yang digunakan untuk melakukan suatu pekerjaan (misal klasifikasi).<br>
Sumber : https://machinelearning.mipa.ugm.ac.id/2018/06/25/fully-connected-layer-cnn-dan-implementasinya/

Dengan gambaran arsitektur seperti dibawah ini:
<p align="center">
  <img width="320" height="853" src="https://github.com/ds-dti/DS02_03_Plant-Clinic/blob/master/gambar/Arsitektur%20Model%20Plant%20Clinic.jpeg">
</p>

## Cara Penggunaan
Berikut cara menggunakan aplikasi Plant-Clinic.

#### Kunjungi halaman berikut ini
```bash
https://plant-clinic.herokuapp.com/
```
#### Lalu pilih gambar dan klik tombol Prediksi
![landing Page Tubes DTI](https://github.com/ds-dti/DS02_03_Plant-Clinic/blob/master/gambar/Halman%20Awal.png)
#### Setelah itu akan muncul halaman yang berisi informasi dari kondisi tanaman anda
![landing Page Tubes DTI](https://github.com/ds-dti/DS02_03_Plant-Clinic/blob/master/gambar/Hasil%20Prediksi.png)
#### Jenis Tanaman (Update)
Berikut ini merupakan jenis tanaman yang bisa kami kenali, untuk kedepannya tidak menutup kemungkinan akan terus bertambah
```bash
Apel, Tomat, Anggur, Jagung, Kentang, Paprika, Persik, Strawberry, Lada, Jeruk, Cherry, Labu
```

#### Kalian juga bisa melihat cara pemakaian pada link YouTube berikut ini
```
https://www.youtube.com/watch?v=hh9JLaMtqvE&feature=emb_title
```

## Install di Local
Jika anda ingin menambahkan atau menginstall aplikasi ini di local, anda bisa melakukan clone repository github Plant-CLinic
```
git clone https://github.com/ds-dti/DS02_03_Plant-Clinic.git
cd DS02_03_Plant-Clinic
```
Lalu install dependensi library nya
```
pip install -r requirements.txt
```

Lalu Run Aplikasi
```
python app.py
```


