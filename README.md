# INTI JAYA
E-Commerce Web Application for All Your Building Needs

### 🪤 Deployment
Explore the live version of the site here: [INTI JAYA Webpage](http://cleo-excellen-intijaya.pbp.cs.ui.ac.id/)

---
- [Tugas 2: Implementasi MVT pada Django](#pbp-c---tugas-2)
- [Tugas 3: Implementasi Form dan Data Delivery pada Django](#pbp-c---tugas-3)
- [Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django](#pbp-c---tugas-4)
---
## PBP C - Tugas 2

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

---
## PBP C - Tugas 3

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
- Data delivery adalah komponen penting yang memungkinkan berbagai elemen platform berkomunikasi secara lancar, aman, dan tepat waktu. Ini memastikan data mengalir dengan baik antara server, klien, dan antarmuka pengguna. Tanpa data delivery, elemen-elemen platform akan terisolasi dan tidak dapat berfungsi optimal. Selain itu, mekanisme ini juga mendukung skalabilitas dan kemampuan platform beradaptasi dengan kebutuhan yang berubah serta menangani lonjakan lalu lintas data.

---
### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
- Menurut saya, jika melihat format pertukaran data yang sering digunakan, JSON lebih unggul dibandingkan XML. Berikut beberapa alasan mengapa saya memilih JSON yang lebih populer:

1. Kesederhanaan: Sintaks JSON lebih sederhana karena tidak memerlukan tag pembuka dan penutup seperti XML. Struktur JSON juga sangat mirip dengan objek dan array dalam JavaScript, sehingga lebih mudah digunakan.
2. Ukuran File: JSON menghasilkan file yang lebih kecil karena tidak perlu menggunakan tag penutup, membuatnya lebih efisien dalam hal penyimpanan dan pengiriman data.
3. Kecepatan Parsing: JSON bisa diparse menjadi objek JavaScript dengan sangat cepat, memberikan performa yang lebih baik dalam aplikasi web.
4. Struktur Data Fleksibel: JSON mendukung tipe data seperti array dan objek bersarang (nested objects) dengan lebih alami dibandingkan XML.
5. Popularitas dalam API: Banyak API modern menggunakan JSON karena lebih mudah diimplementasikan, terutama untuk pengembangan aplikasi web dan mobile.

---
### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
- Method `is_valid()` pada form Django memiliki peran penting dalam memvalidasi data yang dimasukkan oleh pengguna. Fungsinya adalah untuk memeriksa apakah data yang dikirim melalui form telah memenuhi semua aturan validasi, seperti apakah field yang wajib sudah diisi, format data sudah benar, atau apakah data sesuai dengan batasan yang telah ditetapkan. Jika data valid, method ini akan mengembalikan `True`, sementara jika ada kesalahan, akan mengembalikan `False` dan Django akan mengisi dictionary `form.errors` dengan pesan kesalahan yang sesuai untuk setiap field yang tidak valid. Selain itu, `is_valid()` membantu mencegah data yang tidak valid atau berbahaya masuk ke dalam sistem, melindungi aplikasi dari potensi bug dan ancaman keamanan. Singkatnya, method ini akan memvalidasi data yang dikirim oleh pengguna sesuai aturan yang telah ditentukan di form. Jika data valid, maka dapat diproses lebih lanjut (misalnya, disimpan ke database). Jika tidak valid, method akan mengembalikan `False` dan menampilkan pesan error. Tanpa `is_valid()`, kita tidak dapat menjamin bahwa data yang diterima aman dan sesuai, yang bisa mengakibatkan masalah pada aplikasi.

---
###  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
- csrf_token digunakan untuk melindungi aplikasi Django dari serangan Cross-Site Request Forgery (CSRF). Serangan CSRF terjadi ketika penyerang membuat permintaan berbahaya ke server menggunakan kredensial pengguna yang sudah terautentikasi, tanpa sepengetahuan pengguna. Dengan adanya csrf_token, server dapat memverifikasi bahwa permintaan yang dibuat berasal dari situs yang sah dan bukan dari sumber eksternal berbahaya. Jika kita tidak menyertakan csrf_token dalam form Django, penyerang dapat membuat situs atau skrip berbahaya yang mengirimkan permintaan ke aplikasi Django dengan memanfaatkan kredensial pengguna yang sedang login. Permintaan palsu tersebut akan tampak sah karena dikirim dari browser pengguna yang terautentikasi, dan tanpa csrf_token, server tidak dapat membedakan mana permintaan asli dan mana yang palsu. Hal ini memungkinkan penyerang untuk mengubah data sensitif, mencuri informasi pribadi, atau melakukan transaksi yang tidak sah.

###  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
#### 1. Membuat Input Form untuk Menambahkan Objek Model

**Langkah-langkah**:
1. `base.html` untuk menjadi page utama 
    ```python
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {% block meta %} {% endblock meta %}
        </head>
        <body>
            {% block content %} {% endblock content %}
        </body>
    </html>
    ```
 2. Menambahkan `BASE_DIR` di dalam `settings.py` agar project dapat mengenali file HTML yang akan digunakan sebagai template utama.
    ```python
    'DIRS': [BASE_DIR / 'templates'],

3. Menambahkan atribut `id` pada model product
    ```python
    import uuid
   from django.db import models

   # Create your models here.
   class ProductEntry(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      name = models.CharField(max_length=255)
      price = models.IntegerField()
      description = models.TextField()
      quantity = models.IntegerField()
      categories = models.CharField(max_length=255)

      def __str__(self):
         return self.name
         ```
4. Membuat `forms.py` untuk mendeklarasikan atribut-atribut dari model yang membutuhkan input dari user
    ```python
    from django.forms import ModelForm
   from main.models import ProductEntry

   class ProductEntryForm(ModelForm):
      class Meta:
         Model = ProductEntry
         fields = ['name', 'price', 'description', 'quantity', 'categories']
    ```
5. Membuat method `show_main` untuk menampilkan di `main.html`
    ```python
    def show_main(request):
    products = ProductEntry.objects.all()

    context = {
        'npm': '2306244886',
        'nama': 'Cleo Excellen Iskandar',
        'kelas': 'PBP C',
        'shop_name':'INTI JAYA',  
        'product_entry' : products
    }

    return render(request, "main.html", context)
    ```
6. Membuat method `create_name_entry` untuk mengambil input user sesuai dengan `forms.py`
    ```python
    def create_name_entry(request):
        form = ProductEntryForm(request.POST or None)
        if form.is_valid() and request.method == 'POST':
            form.save()
            return redirect('main:show_main')
        context={'form':form}
        return render(request,'create_name_entry.html',context)
    ```
7. Membuat `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` untuk menampilkan response back dari input user
    ```python
    def show_xml(request):
        data = ProductEntry.objects.all()
        return HttpResponse(serializers.serialize("xml",data),content_type='application/xml')

    def show_json(request):
        data = ProductEntry.objects.all()
        return HttpResponse(serializers.serialize("json",data),content_type='application/json')

    def show_xml_by_id(request, id):
        data = ProductEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = ProductEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

8. Melakukan routing di dari method yang sudah dibuat di `urls.py`
   ```python
   from django.urls import path
   from main.views import show_main,create_name_entry,show_xml,show_json,show_xml_by_id,show_json_by_id

   app_name = 'main'

   urlpatterns = [
      path('', show_main, name='show_main'),
      path('create-name-entry', create_name_entry, name='create_name_entry'),
      path('xml/',show_xml,name='show_xml'),
      path('json/',show_json,name='show_json'),
      path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
      path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
   ]
9.  Membuat `create_name_entry.html` untuk tampilan ketika web ingin meminta input dari pengguna.
      ```python
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add Product Entry</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product Entry" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```
10. Membuat `main.html` untuk menampilkan product dari hasil input pengguna
      ```python
         {% extends 'base.html' %}
         {% block content %}
         <!DOCTYPE html>
         <html>
         <head>
            <title>Main Page</title>
         </head>
         <body>
            <h1>{{ shop_name }} by {{ nama }}</h1>
            <p>NPM: {{ npm }}</p>
            <p>Class: {{ kelas }}</p> 

            {% if not product_entry %}
            <p>Belum ada data produk.</p>
            {% else %}
            <table>
               <tr>
               <th>Product Name</th>
               <th>Price</th>
               <th>Description</th>
               <th>Quantity</th>
               <th>Categories</th>
               </tr>

            {% for product in product_entry %}
                  <tr>
                  <td>{{ product.name }}</td>
                  <td>{{ product.price }}</td>
                  <td>{{ product.description }}</td>
                  <td>{{ product.quantity }}</td>
                  <td>{{ product.categories }}</td>
                  </tr>
            {% endfor %}
            </table>
               {% endif %}
               <br />
               <a href="{% url 'main:create_name_entry' %}">
                  <button>Add New Product Entry</button>
               </a>
         </body>
      </html>
      {% endblock content %}

# Screenshot Postman
## XML
![XML](./images/xml.png)
## JSON 
![JSON](./images/json.png)
## XML by Id
![XML by Id](./images/xmlbyid.png)
## JSON by Id
![JSON by Id](./images/jsonbyid.png)

## PBP C - Tugas 4

### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
- Perbedaan antara HttpResponseRedirect() dan redirect() terletak pada cara dan fleksibilitas penggunaannya untuk melakukan redirect ke URL
- **`HttpResponseRedirect()`**:
    - kelas bawaan Django yang mengembalikan respon HTTP 302 untuk melakukan redirect ke URL yang ditentukan.
    - Cocok digunakan jika ingin memiliki kontrol lebih terhadap respon sebelum mengembalikannya
    - Contoh: Mengarah ke URL yang berada di luar domain situs, seperti Google
    ```python
    from django.http import HttpResponseRedirect

    def my_view(request):
        return HttpResponseRedirect('https://www.google.com')

    ```
- **`redirect()`**:
  - Merupakan fungsi shortcut dari Django yang secara internal menggunakan HttpResponseRedirect()
  - `Lebih praktis dan fleksibel karena bisa menerima berbagai jenis parameter seperti URL, named URL patterns, atau bahkan instance model.
  - Contoh:
    ```python
    from django.shortcuts import redirect
    
    def my_view(request):
        return redirect('url-name')
    ```
**Perbedaan Utama**: redirect() adalah pilihan yang lebih sederhana dan fleksibel dibandingkan HttpResponseRedirect(), terutama dalam hal menerima berbagai jenis parameter. Sebaliknya, HttpResponseRedirect() lebih cocok digunakan saat diperlukan kontrol lebih terhadap respons yang dikirimkan.

### 2. Menghubungkan model Product dengan User.

**Langkah-langkah**:

1. Membuka models.py pada subdirektori main dan tambahkan kode dibawah untuk mengimpor model:
    ```python
    from django.contrib.auth.models import User
    ```
2. Menambahkan potongan kode berikut pada model ProductEntry yang sudah dibuat
    ```python
    class ProductEntry(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```
    - Menghubungkan satu product entry dengan satu user dengan relationship, yaitu sebuah product entry akan terasosiasi dengan seorang user
3. Pada views.py pada subdirektori main, saya mengubah fungsi create_name_entry dengan kode di bawah
    ```python
    def create_name_entry(request):
        form = ProductEntryForm(request.POST or None)
        if form.is_valid() and request.method == 'POST':
            name_entry = form.save(commit=False)
            name_entry.user = request.user
            name_entry.save()
            return redirect('main:show_main')
        context={'form':form}
        return render(request,'create_name_entry.html',context)
    ```
    - Parameter commit=False berguna untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database. kita mengisi field user dengan objek User dari return value request.user yang sedang terotorisasi untuk menandakan bahwa objek tersebut dimiliki oleh pengguna yang sedang login.

4. Mengubah value dari products dan context pada fungsi show_main
    ```python
    def show_main(request):
        products = ProductEntry.objects.filter(user=request.user)
        context = {
            'nama': request.user.username,
         ...
        }
    ```
5. Menyimpan semua perubahan, dan melakukan migrasi model dengan python manage.py makemigrations.
6. Pilih 1 untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada database. Lalu Ketik angka 1 lagi untuk menetapkan user dengan ID 1 pada model yang sudah ada.
![DEFAULTVALUE](./images/defaultvalue.png)
7. Melakukan python manage.py migrate untuk mengaplikasikan migrasi yang dilakukan.
8. Mempersiapkan aplikasi web untuk environtment production dengan mambahkan sebuah *import os* pada settings.py yang ada pada subdirektori intijaya
9. Mengganti variabel DEBUG dari berkas settings.py.
    ```python
    PRODUCTION = os.getenv("PRODUCTION", False)
    DEBUG = not PRODUCTION
    ```

### 3.  Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

- **`Authentication`**:
    - Proses untuk memverifikasi identitas pengguna. Ini adalah langkah untuk memastikan bahwa seseorang atau entitas adalah siapa yang mereka klaim.
    - Contoh:
        Memasukkan username dan password saat login ke akun dan memasukkan kode OTP (One-Time Password) yang dikirim ke ponsel.
    - Jika dengan analogi ini seperti saat kita menunjukkan KTP ke petugas pintu masuk gedung untuk membuktikan bahwa kamu adalah orang yang berhak masuk.
    - Proses saat pengguna login yaitu, Pengguna memasukkan kredensial mereka. Lalu sistem memeriksa kredensial pada data yang tersimpan. Jika cocok, pengguna dinyatakan berhasil terotentikasi, dan sistem biasanya membuat sesi atau memberikan token untuk pengguna.
    - Django menyediakan authenticate() dan login() yang memverifikasi username dan password pengguna. Jika valid, sesi baru dibuat untuk pengguna tersebut
    ```python
    from django.contrib.auth import authenticate, login

        def my_login_view(request):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Create a session for the user
                return redirect('home')
            else:
                return HttpResponse('Invalid login')
    ```

- **`Authorization`**:
    - Proses untuk menentukan hak atau izin yang dimiliki pengguna setelah mereka terautentikasi. Ini memastikan bahwa pengguna hanya dapat mengakses sumber daya atau data yang diizinkan untuk mereka.
    - Contoh:
        Setelah login ke aplikasi, seorang admin dapat menambah atau menghapus pengguna, tetapi pengguna biasa hanya dapat melihat profil mereka sendiri.
    - Jika dengan analogi ini seperti setelah menunjukkan KTP dan diizinkan masuk ke gedung (autentikasi), kita hanya boleh masuk ke area tertentu, misalnya ruang lobby, bukan ke ruang admin.
    - Proses saat pengguna login yaitu Setelah terotentikasi, sistem memeriksa peran atau izin pengguna. Berdasarkan peran tersebut, sistem menentukan tindakan apa saja yang boleh diakses oleh pengguna tersebut.
    - Django menggunakan sistem izin (permissions) dan grup (groups) untuk mengatur otorisasi. Django juga menyediakan decorator @login_required untuk memastikan bahwa pengguna harus login untuk mengakses halaman tertentu, serta @permission_required untuk memastikan pengguna memiliki izin tertentu.
    ```python
    from django.contrib.auth.decorators import login_required, permission_required
    @login_required
    def dashboard(request):
        return render(request, 'dashboard.html')
    @permission_required('app_name.can_add_post')
    def add_post(request):
        return render(request, 'add_post.html')
    ```

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
- Django mengingat pengguna yang telah login menggunakan sesi (sessions) yang disimpan dalam cookies. Saat pengguna berhasil login, Django membuat sebuah sesi untuk pengguna tersebut. Django menyimpan informasi sesi di server (database, cache, atau file system) dan memberikan sebuah ID sesi unik kepada pengguna tersebut. ID sesi ini dikirimkan ke browser pengguna dalam bentuk cookie yang bernama sessionid. Setiap kali pengguna membuat permintaan (request) baru ke server, browser mengirimkan cookie sessionid tersebut kembali ke server. Django menggunakan ID sesi ini untuk mengambil informasi pengguna yang tersimpan di server, sehingga server bisa mengenali siapa pengguna yang sedang berinteraksi.
- Kegunaan lain dari cookies bisa menjadi Penyimpanan preferensi pengguna, pelacakan, keranjang belanja pada e-commerce, dan isa juga menyimpan token keamanan. 
- Tidak semua cookies aman digunakan. Cookies yang tidak dikelola dengan baik dapat rentan terhadap ancaman seperti Cross-Site Scripting (XSS) dan Cross-Site Request Forgery (CSRF). Oleh karena itu, untuk meningkatkan keamanan cookies, penting untuk mengatur cookies dengan atribut HttpOnly agar tidak dapat diakses oleh JavaScript, dan menggunakan atribut Secure agar cookies hanya dikirim melalui koneksi HTTPS.





















