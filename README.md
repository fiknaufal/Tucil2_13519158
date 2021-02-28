# Tucil-2-Stima-2021

Program ini dibuat untuk memenuhi tugas Mata Kuliah **IF 2211 Strategi Algoritma** <br />

*Program Studi Teknik Informatika* <br />
*Sekolah Teknik Elektro dan Informatika* <br />
*Institut Teknologi Bandung* <br />

*Semester II Tahun 2020/2021*

## Deskripsi Singkat Algoritma Decrease and Conquer
Algoritma dicrease and conquer merupakan algoritma yang memecah masalah menjadi beberapa upa permasalahan lalu mengeliminasi upa permasalahan yang tidak memiliki potensi penyelesaian di dalamnya. Penjelasan algoritma decrease and conquer akan dipaparkan di bawah ini.
1.	Membaca file text input dan dimasukkan ke dalam array of array of string dengan nama “node_array”.
Misal input seperti ini:
```
C7,C4,C5.
C6,C5,C3.
C5,C3.
C4,C2,C1.
C3.
C2.
C1.
```
Maka akan dihasilkan “node_array” seperti:
```
[[C7,C4,C5],[C6,C5,C3],[C5,C3],[C4,C2,C1],[C3],[C2],[C1]]
```
2.	Melaksanakan algoritma decrease and conquer dengan tahap pertama yaitu membuat array kosong dengan nama “semester” untuk diisi dengan array mata kuliah tiap semesternya.
3.	Membuat array kosong dengan nama “sendiri” dan mencatat mata kuliah yang terdapat dalam array of string dalam “node_array” yang berelemen satu, misal pada keadaan awal, mata kuliah yang dipilih adalah C3, C2, C1.
4.	Menghapus kemunculan mata kuliah yang ada pada array “sendiri” dalam tiap array of array of string di array “node_array”.
5.	Menghapus array of array of string yang kosong pada array “node array”.
6.	Masukkan array of string “sendiri” ke dalam array “semester”.
7.	Ulangi langkah 3-6 sampai “node_array” merupakan array yang kosong.
8.	Tampilkan tiap array of array of string dengan format seperti dibawah.
```
Semester I : C3, C2, C1
Semester II : C5, C4
Semester III : C7, C6
```
Urutan semester merupakan urutan tempat array of array pada array “semester” berada ditambah 1.
