# INTI JAYA
E-Commerce Web Application for All Your Building Needs

### 🪤 Deployment
Explore the live version of the site here: [INTI JAYA Webpage](http://cleo-excellen-intijaya.pbp.cs.ui.ac.id/)

---

## PBP C - Tugas 2 : Implementasi MVT pada Django

### Cara Pengimplementasian 🐾

1. **Membuat Proyek Django Baru.**
   - Langkah awal adalah menginisialisasi proyek Django dengan menggunakan perintah `django-admin startproject [nama_proyek]`. Perintah ini akan menghasilkan struktur direktori dasar yang diperlukan untuk menjalankan proyek Django saya.

2. **Membuat Aplikasi Bernama "main" pada Proyek.**
   - Setelah proyek Django diinisialisasi, langkah berikutnya saya menambahkan aplikasi bernama "main" dengan menjalankan perintah `python manage.py startapp main`. Aplikasi ini akan menjadi tempat untuk menyimpan semua logika dan fitur yang akan dikembangkan dalam proyek saya.

3. **Melakukan Routing Proyek untuk Menjalankan Aplikasi "main".**
   - Di dalam file `urls.py` proyek, kita tambahkan konfigurasi rute yang mengarahkan permintaan (request) ke aplikasi "main". Langkah ini memastikan bahwa aplikasi "main" terhubung dengan proyek dan dapat diakses melalui URL yang sesuai.

4. **Membuat Model Product pada Aplikasi "main" dengan Atribut.**
   - Di dalam file `models.py` pada aplikasi "main", definisikan model Product yang menggambarkan entitas produk. Model ini akan mencakup atribut wajib seperti `name`, `description`, `price`, dan saya menambahkan `quantity` dan `categories`, yang akan digunakan untuk menyimpan informasi produk ke dalam database.

5. **Membuat Fungsi di views.py untuk Merender Template HTML dengan Nama Aplikasi serta Nama dan Kelas saya.**
   - Di dalam file `views.py`, buatlah sebuah fungsi yang akan merender template HTML. Template ini akan menampilkan informasi seperti nama aplikasi, nama, dan kelas saya, yang akan disediakan oleh fungsi tersebut.

6. **Menambahkan Routing di urls.py Aplikasi "main" untuk Memetakan Fungsi di views.py.**
   - Di file `urls.py` pada aplikasi "main", tambahkan rute baru yang menghubungkan URL dengan fungsi yang telah saya buat di `views.py`. Ini menjadikan pengguna dapat mengakses halaman yang telah dibuat melalui URL yang telah saya tentukan.

7. **Melakukan Deployment ke PWS agar Bisa diakses melalui Internet.**
   - Setelah aplikasi selesai dibuat, lakukan proses deployment ke Pacil Web Service (PWS). Ini mencakup mengunggah proyek ke server PWS agar aplikasi dapat diakses secara online oleh teman-teman saya melalui Internet.

8. **Membuat README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.**
   - Tahap akhir membuat file `README.md` yang berisi deskripsi proyek, langkah-langkah implementasi, serta tautan menuju aplikasi yang sudah di-deploy di PWS. Sertakan juga jawaban untuk pertanyaan yang relevan tentang Django dan fungsionalitasnya untuk menambah pemahaman kita.

### Alur Django 🔍 

![DJANGO FLOW DIAGRAM - Page 1](./images/BaganRequest.png)


- Bagan alur request dalam aplikasi web Django dimulai ketika client (browser) mengirimkan permintaan (request) ke server. Proses pertama adalah **`urls.py`**, memetakan URL yang diminta ke fungsi yang tepat di **`views.py`**. Di **`views.py`**, request diproses, dan bila diperlukan, berinteraksi dengan  **`models.py`** untuk mengambil atau menyimpan data dari database. Setelah pengolahan data di **`views.py`**, template HTML (pada folder templates) dirender dan hasilnya dikirim kembali ke client sebagai respon. Jika kita menarik kesimpulan,  **`urls.py`** mengatur arah request, **`views.py`** menangani logika aplikasi, **`models.py`** mengelola data, dan berkas HTML menampilkan informasi kepada pengguna.

### Fungsi Git 🖇️
- Git adalah alat kontrol versi yang memungkinkan pengembang perangkat lunak untuk melacak setiap perubahan dalam kode secara mendetail. Dengan Git, tim pengembang dapat bekerja bersama dalam satu proyek, mengelola berbagai cabang (branch) untuk fitur baru atau perbaikan bug, serta menggabungkan perubahan (merge) dengan aman. Git juga menyediakan kemampuan untuk kembali ke versi sebelumnya jika terjadi kesalahan, sehingga mengurangi risiko dalam proses pengembangan perangkat lunak. Dengan demikian, Git membantu menjaga konsistensi kode dan meningkatkan efisiensi kerja tim dalam proyek yang kompleks.                                                                                                      

### Mengapa Django yang dijadikan permulaan pembelajaran pengembangan perangkat lunak? 🖌️📚
- Django sering dipilih sebagai framework pembelajaran awal karena mendukung pengembangan cepat (rapid development) dan menerapkan praktik terbaik seperti arsitektur Model-View-Template (MVT). Kesederhanaannya memungkinkan pemula memahami konsep dasar seperti templating, routing, dan manajemen database tanpa harus menghadapi kode yang kompleks. Dokumentasi dan komunitas yang luas mempermudah pemula dalam menemukan solusi serta sumber belajar yang baik.

### Mengapa model pada Django disebut Object-Relational Mapping / ORM ? 💭
- Model Django dikenal sebagai ORM (Object-Relational Mapping) karena memungkinkan pemetaan objek Python ke database relasional. Dengan menggunakan ORM, pengembang dapat mengelola database melalui kode Python tanpa harus menulis kueri SQL secara langsung. ORM menyederhanakan interaksi dengan database, memastikan kode tetap terstruktur dan mudah dipahami, dan mempermudah olah data.