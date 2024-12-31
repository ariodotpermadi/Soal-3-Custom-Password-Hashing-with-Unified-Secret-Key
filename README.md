Penjelasan Keamanan dan Alasan Penggunaan PBKDF2

Cara Kerja PBKDF2:
PBKDF2 adalah algoritma key derivation function berbasis password.
Password asli dikombinasikan dengan salt untuk mencegah serangan rainbow table.
Fungsi ini menjalankan iterasi hashing berkali-kali untuk menambah kompleksitas komputasi, sehingga memperlambat serangan brute force.
Hasil akhirnya adalah hash yang sulit dibalik.

Mengapa PBKDF2 Dipilih:
Kuat terhadap brute force attacks: Karena iterasi tinggi, serangan brute force membutuhkan waktu lebih lama.
Dukungan luas: PBKDF2 adalah algoritma yang sudah terstandar dan didukung oleh berbagai pustaka kriptografi.
Mudah digunakan: Algoritma ini memungkinkan kombinasi salt, password, dan kunci tambahan seperti SECRET_KEY.
Keamanan Tambahan dengan Custom Hasher:
Dengan menambahkan SECRET_KEY pada proses hashing, kita meningkatkan keamanan sehingga hash menjadi unik untuk setiap proyek, meskipun password yang digunakan sama.
