# INTI JAYA
E-Commerce Web Application for All Your Building Needs

### 🪤 Deployment
Explore the live version of the site here: [INTI JAYA Webpage](http://cleo-excellen-intijaya.pbp.cs.ui.ac.id/)

---
- [Tugas 2: Implementasi MVT pada Django](#pbp-c---tugas-2)
- [Tugas 3: Implementasi Form dan Data Delivery pada Django](#pbp-c---tugas-3)
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
