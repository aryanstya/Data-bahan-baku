# Data-Bahan-Baku

Proyek aplikasi saya akan mendata jumlah data bahan baku di suatu restoran dengan variabel:
name = nama bahan
amount = jumlah bahan
description = deskripsi bahan

## Tautan Deploy

[Aplikasi di Adaptable](https://data-bahan-baku.adaptable.app)

## Pertanyaan Tugas 2

1. **Mengapa Kita Menggunakan Virtual Environment?**
   Virtual Environment adalah alat yang berguna untuk mengisolasi dan mengatur lingkungan pengembangan Python. Dengan menggunakan Virtual Environment, kita dapat secara efektif mengelola dependensi proyek Anda secara terpisah, sehingga menghindari kemungkinan konflik antar-package yang dapat terjadi ketika berbagai proyek Python berbagi lingkungan yang sama.

2. **Apa Itu MVC, MVT, MVVM, dan Perbedaannya?**
   - MVC (Model-View-Controller): Paradigma desain yang memisahkan aplikasi menjadi tiga komponen utama: Model (representasi data), View (tampilan pengguna), dan Controller (logika bisnis).
   - MVT (Model-View-Template): Konsep yang digunakan oleh Django, mirip dengan MVC tetapi menggantikan "Controller" dengan "Template" yang mengatur bagaimana data dari Model ditampilkan di View.
   - MVVM (Model-View-ViewModel): Paradigma desain yang digunakan dalam pengembangan aplikasi berbasis web dengan JavaScript, yang memisahkan Model, View, dan ViewModel yang mengelola logika tampilan.

3. **Bagan Request Client ke Web Aplikasi Django:**
   ```
   +-------------------------+
   | URLs.py                 |
   |   - Menghubungkan URL   |
   |     dengan View         |
   +-------------------------+
              |
              v
   +-------------------------+
   | Views.py                |
   |   - Memproses permintaan|
   |     dari client         |
   +-------------------------+
              |
              v
   +-------------------------+
   | Models.py               |
   |   - Mendefinisikan data |
   |     dan struktur        |
   +-------------------------+
              |
              v
   +-------------------------+
   | Template HTML           |
   |   - Menampilkan data    |
   |     ke client           |
   +-------------------------+

   
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

   Untuk mengimplementasikan checklist di atas, berikut adalah langkah-langkahnya secara singkat:

      1. **Membuat Proyek Django Baru:**
         - Buka terminal dan navigasikan ke direktori tempat Anda ingin membuat proyek Django.
         - Jalankan perintah `django-admin startproject nama_proyek` untuk membuat proyek baru. Gantilah "nama_proyek" dengan nama yang Anda inginkan.
      
      2. **Membuat Aplikasi "main":**
         - Dalam direktori proyek, jalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru dengan nama "main".
      
      3. **Melakukan Routing pada Proyek:**
         - Di dalam file `urls.py` proyek (nama_proyek/urls.py), tambahkan routing untuk aplikasi "main" dengan menggunakan `include`.
      
      4. **Membuat Model "Item":**
         - Di dalam aplikasi "main" (main/models.py), definisikan model "Item" dengan atribut yang sesuai seperti "name," "amount," dan "description" dengan tipe data yang sesuai.
      
      5. **Membuat Fungsi pada views.py:**
         - Di dalam aplikasi "main" (main/views.py), buat sebuah fungsi view yang mengembalikan data yang ingin ditampilkan dalam template HTML. Contohnya:
      
         ```python
         from django.shortcuts import render
      
         def my_view(request):
             nama_aplikasi = "Aplikasi Saya"
             nama_kelas = "Kelas Saya"
             return render(request, 'template.html', {'nama_aplikasi': nama_aplikasi, 'nama_kelas': nama_kelas})
         ```
      
      6. **Membuat Template HTML:**
         - Buat template HTML (misalnya, "template.html") yang akan digunakan untuk menampilkan data dari fungsi view. Anda dapat menggunakan variabel yang dikirim dari view dalam template ini.
      
      7. **Membuat Routing pada urls.py Aplikasi "main":**
         - Di dalam aplikasi "main" (main/urls.py), buat routing untuk mengaitkan URL dengan fungsi view yang telah Anda buat.
      
      8. **Melakukan Deployment ke Adaptable:**
         - Untuk melakukan deployment, Anda perlu memilih platform hosting atau server. Setelah itu, ikuti panduan hosting Django atau platform yang Anda pilih untuk mengunggah proyek Anda dan mengatur konfigurasi yang diperlukan.
      
      9. **Mengakses Aplikasi:**
         - Setelah berhasil dideploy, aplikasi Anda dapat diakses melalui internet menggunakan alamat yang diberikan oleh platform hosting atau server yang Anda pilih.
      




## Pertanyaan Tugas 3

1. **Perbedaan antara Form POST dan Form GET dalam Django?**

 Form POST: Dalam metode POST, data yang dikirimkan ke server disertakan dalam badan permintaan HTTP. Ini lebih aman dan cocok untuk mengirim data yang sensitif atau data yang memiliki panjang yang lebih besar, seperti saat       
            mengirimkan   formulir pengisian data. Data POST tidak tampil di URL dan tidak memiliki batasan panjang yang ketat.
            
  Form GET: Dalam metode GET, data yang dikirimkan ke server disertakan dalam URL sebagai parameter. Ini cocok untuk permintaan yang bersifat idempoten dan hanya digunakan untuk mengambil data (tidak digunakan untuk mengubah data). Data             dalam metode GET dapat dilihat di URL dan memiliki batasan panjang yang terbatas.
    
    
2. **Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data**

    XML (Extensible Markup Language): Digunakan untuk mengatur dan menyimpan data dalam format yang dapat disesuaikan dengan struktur hierarki. Biasanya digunakan dalam pengiriman data seperti sitemap, RSS feed, atau konfigurasi. Memiliki sintaksis yang lebih berat dibandingkan JSON dan HTML.

JSON (JavaScript Object Notation): Digunakan untuk pertukaran data antara aplikasi. Format data yang ringan dan mudah dibaca oleh manusia. Cocok untuk komunikasi antara aplikasi web modern karena kemampuannya dalam merepresentasikan objek dan array.

HTML (Hypertext Markup Language): Digunakan untuk menggambarkan struktur dan tampilan halaman web. Tidak seperti XML dan JSON, HTML lebih fokus pada tampilan dan interaksi pengguna.


3. **Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern**

      JSON digunakan secara luas dalam pertukaran data karena ringan dan mudah dibaca oleh manusia
    Formatnya mendukung tipe data seperti objek dan array, yang cocok untuk representasi data yang lebih kompleks.
    Dukungan yang kuat untuk bahasa pemrograman, termasuk JavaScript, membuatnya ideal untuk komunikasi antara server dan aplikasi web klien.
    JSON juga sering digunakan dalam API REST karena sederhana, dapat diurai dengan mudah, dan kompatibel dengan berbagai bahasa pemrograman.

4. 

   ![Foto HTML](https://github.com/aryanstya/Data-bahan-baku/assets/124659813/00f530ce-7bd2-4a46-94e0-e13dad456add)

   ![Foto XML](https://github.com/aryanstya/Data-bahan-baku/assets/124659813/4bb70ede-12a5-453c-abf0-2971b4a6d253)

   ![Foto XML with ID](https://github.com/aryanstya/Data-bahan-baku/assets/124659813/d42b140e-2f34-4b55-92fe-b058b6bfc488)

   ![Foto JSON](https://github.com/aryanstya/Data-bahan-baku/assets/124659813/4e9a369c-d987-444b-b27c-909b9e8b383f)

   ![Foto JSON With ID](https://github.com/aryanstya/Data-bahan-baku/assets/124659813/a65440c8-b943-4b80-9318-b04c2b4afa12)

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Langkah 1: Membuat Input Form**

   Buka proyek Django Anda dan navigasikan ke aplikasi yang sudah ada.
   
   Buat model Django yang akan digunakan untuk menyimpan objek yang akan ditambahkan. Misalnya, jika Anda ingin menyimpan daftar "Task", buat model Task.
   
   Buat sebuah form Django yang berfungsi untuk menambahkan objek ke dalam model tersebut. Anda dapat menggunakan ModelForm untuk mempermudah pembuatan form berdasarkan model.
   
   Buat tampilan (view) yang akan menampilkan form tersebut sebagai halaman HTML.
   
   Buat template HTML untuk tampilan form dan terapkan form tersebut di dalamnya.

**Langkah 2: Menambahkan 5 Fungsi Views**

   Buat 5 tampilan (views) berbeda, masing-masing untuk melihat objek yang telah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
   
   Tambahkan kode dalam setiap tampilan untuk mengambil objek-objek dari model yang sesuai, kemudian menghasilkan output dalam format yang diminta (HTML, XML, JSON) berdasarkan jenis tampilan.
   
   Untuk tampilan XML dan JSON by ID, pastikan tampilan tersebut menerima parameter ID untuk menentukan objek yang ingin dilihat.

**Langkah 3: Membuat Routing URL**

   Buka file urls.py dalam aplikasi Django Anda.
   
   Tambahkan path atau rute URL untuk setiap tampilan yang Anda buat pada langkah 2. Anda harus menentukan pola URL dan menentukan fungsi tampilan yang akan dipanggil.
   
   Langkah 4: Menjawab Pertanyaan di README.md
   
   Buka file README.md dalam folder root proyek Anda.
   
   Tambahkan bagian yang menjawab pertanyaan-pertanyaan yang tercantum dalam checklist. Anda dapat menggunakan bahasa Markdown untuk mengatur dan menyajikan jawaban Anda secara rapi.


   ## Pertanyaan Tugas 4

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

      **Django UserCreationForm** adalah salah satu dari banyak formulir bawaan yang disediakan oleh Django, sebuah framework pengembangan web berbasis Python. Formulir ini secara khusus digunakan untuk memudahkan proses pembuatan akun pengguna dalam aplikasi web Django. UserCreationForm mengumpulkan informasi yang diperlukan untuk membuat akun pengguna baru, seperti nama pengguna (username), kata sandi (password), dan, jika diinginkan, informasi tambahan seperti alamat email.
      
      **Kelebihan Django UserCreationForm:**
      
      1. **Kemudahan Penggunaan:** UserCreationForm adalah bagian integral dari Django's authentication system. Ini membuatnya sangat mudah untuk digunakan dan diintegrasikan dalam aplikasi Django Anda.
      
      2. **Keamanan Bawaan:** Formulir ini secara otomatis mengatasi banyak masalah keamanan yang terkait dengan pendaftaran pengguna, termasuk enkripsi kata sandi menggunakan algoritma hash yang aman.
      
      3. **Customizable:** Meskipun sederhana, UserCreationForm tetap dapat disesuaikan sesuai kebutuhan. Anda dapat menambahkan atau mengubah bidang-bidang yang ada untuk mengakomodasi informasi       tambahan yang ingin Anda kumpulkan.
      
      **Kekurangan Django UserCreationForm:**
      
      1. **Keterbatasan Kustomisasi:** Meskipun dapat disesuaikan, UserCreationForm biasanya cocok untuk kasus penggunaan pendaftaran dasar. Jika Anda memerlukan alur pendaftaran yang lebih kompleks, seperti verifikasi email atau pendaftaran dengan media sosial, Anda mungkin perlu menulis formulir pendaftaran kustom Anda sendiri.
      
      2. **Tampilan Bawaan yang Sederhana:** Tampilan default dari UserCreationForm cenderung sederhana. Ini berarti Anda mungkin perlu menghabiskan waktu tambahan untuk menyesuaikan tampilan formulir agar sesuai dengan desain dan gaya visual aplikasi Anda.
      
      3. **Memerlukan Penggunaan Django:** UserCreationForm hanya relevan jika Anda menggunakan Django sebagai framework pengembangan web Anda. Ini mungkin menjadi kendala jika Anda mempertimbangkan untuk menggunakan platform lain atau membangun sesuatu yang tidak berbasis Django. 


  
2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?


autentikasi dan otorisasi adalah dua konsep yang sangat penting untuk mengelola akses dan keamanan dalam aplikasi web. Mereka memiliki perbedaan yang signifikan:

**Autentikasi (Authentication):**

   Autentikasi adalah proses memverifikasi identitas pengguna, yaitu memastikan bahwa pengguna adalah orang yang mereka klaim menjadi. Ini adalah tahap awal yang harus dilewati oleh pengguna saat mereka mencoba mengakses aplikasi Anda.
   
   Dalam konteks Django, autentikasi berarti mengidentifikasi pengguna berdasarkan kredensial yang mereka berikan, seperti nama pengguna (username) dan kata sandi (password). Django memiliki built-in fitur autentikasi yang sangat kuat yang dapat mengelola proses ini dengan aman.
   
   Setelah autentikasi berhasil, pengguna akan diberikan akses ke akun mereka atau ke fitur-fitur tertentu yang memerlukan otentikasi.
   
   Contoh: Saat seorang pengguna memasukkan nama pengguna dan kata sandi yang benar, mereka dianggap terautentikasi dan dapat mengakses akun pribadi mereka.

**Otorisasi (Authorization):**

   Otorisasi adalah proses yang terjadi setelah autentikasi. Ini mengatur apa yang pengguna yang telah terautentikasi dapat dan tidak dapat lakukan dalam aplikasi Anda. Otorisasi berkaitan dengan pengelolaan izin dan hak akses pengguna.
   
   Dalam konteks Django, otorisasi melibatkan pengaturan hak akses untuk pengguna, biasanya dengan menggunakan grup dan izin. Ini menentukan apakah pengguna diizinkan mengakses fitur-fitur tertentu, data, atau tindakan tertentu dalam aplikasi.
   
   Otorisasi memastikan bahwa pengguna hanya dapat mengakses bagian-bagian dari aplikasi yang sesuai dengan peran atau izin mereka, dan mencegah akses yang tidak sah ke data atau fungsi penting.
   
   Contoh: Seorang pengguna yang terautentikasi tetapi hanya memiliki izin "pengguna reguler" tidak akan dapat mengakses halaman admin atau mengedit data yang hanya diizinkan untuk admin.

**Mengapa keduanya penting?**

   **Autentikasi** penting karena memastikan bahwa hanya pengguna yang sah yang dapat mengakses sistem Anda. Ini melindungi privasi dan keamanan data pengguna.
   
   **Otorisasi** penting karena mengendalikan apa yang pengguna yang terautentikasi dapat lakukan dalam aplikasi Anda. Ini memungkinkan Anda untuk menjaga kontrol dan keamanan tingkat granular terhadap berbagai fitur dan data.



3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
   
   **Cookies dalam konteks aplikasi web** adalah file kecil yang disimpan di sisi klien (browser) dan digunakan untuk menyimpan informasi terkait sesi atau pengguna. Mereka dapat digunakan untuk mengenali pengguna, menyimpan preferensi, atau mengelola data sesi.
   
   **Django menggunakan cookies untuk mengelola data sesi pengguna** dengan cara menyimpan ID sesi pengguna dalam cookie. Saat pengguna mengakses situs web Django, server menghasilkan ID sesi unik untuk mereka, yang kemudian disimpan dalam cookie di browser pengguna. ID sesi ini digunakan untuk mengidentifikasi pengguna dan mengaitkannya dengan data sesi di server, seperti keranjang belanja atau preferensi pengguna. Ini memungkinkan pengguna untuk tetap masuk dan menyimpan data mereka saat mereka berinteraksi dengan situs web Anda.


4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

      Penggunaan cookies tidak selalu aman secara default dalam pengembangan web, dan ada risiko potensial yang harus diwaspadai:

   **Keamanan Data:** Data yang disimpan dalam cookies dapat terlihat oleh pengguna jika tidak dienkripsi dengan benar. Informasi sensitif seperti kata sandi atau data kartu kredit tidak boleh disimpan dalam cookies.
   
   **Serangan Cross-Site Scripting (XSS):** Jika aplikasi Anda rentan terhadap serangan XSS, penyerang dapat mencuri cookies pengguna, yang dapat digunakan untuk mengakses akun pengguna.
   
   **Serangan Cross-Site Request Forgery (CSRF):** Cookies yang digunakan untuk autentikasi pengguna harus dilindungi dari serangan CSRF, yang dapat mengakibatkan tindakan tidak sah di akun pengguna.
   
   **Cookie Theft:** Jika pengguna menggunakan komputer bersama atau tidak mengamankan perangkat mereka dengan baik, cookies mereka dapat dicuri oleh orang lain yang memiliki akses ke perangkat tersebut.
   
   Untuk mengamankan penggunaan cookies, Anda harus mengikuti praktik terbaik dalam mengenkripsi data sensitif, melindungi aplikasi Anda dari serangan XSS dan CSRF, serta memeriksa pengaturan keamanan peramban untuk mengontrol bagaimana cookies digunakan.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

      Berikut adalah langkah-langkah implementasi checklist yang Anda sebutkan:

      **Langkah 1: Mengimplementasikan Fungsi Registrasi, Login, dan Logout**
      
      1. Buat tampilan (view) untuk registrasi pengguna yang menggunakan Django UserCreationForm atau formulir kustom jika diperlukan.
      2. Buat tampilan (view) untuk login menggunakan Django built-in authentication views atau tampilan kustom.
      3. Buat tampilan (view) untuk logout menggunakan Django built-in `logout` view.
      4. Tentukan rute (URL) untuk setiap tampilan registrasi, login, dan logout.
      5. Buat template HTML yang sesuai untuk masing-masing tampilan tersebut.
      
      **Langkah 2: Membuat Dua Akun Pengguna dengan Dummy Data**
      
      1. Buat skrip manajemen Django (misalnya, dengan menggunakan perintah `python manage.py shell`) untuk membuat dua akun pengguna baru.
      2. Gunakan model User yang telah ada atau buat model kustom yang terhubung dengan User.
      3. Simpan tiga data dummy untuk setiap akun, sesuai dengan struktur model yang telah Anda tentukan.
      4. Simpan data-data ini dalam database.
      
      **Langkah 3: Menghubungkan Model Item dengan User**
      
      1. Pastikan model `Item` memiliki hubungan ForeignKey ke model `User`. Ini akan mengaitkan setiap item dengan pengguna yang memilikinya.
      2. Lakukan migrasi database untuk memastikan struktur database mencerminkan perubahan ini dengan menjalankan `python manage.py makemigrations` dan `python manage.py migrate`.
      
      **Langkah 4: Menampilkan Detail Informasi Pengguna yang Sedang Logged In dan Menggunakan Cookies**
      
      1. Di tampilan utama aplikasi, terapkan kondisi yang memeriksa apakah pengguna telah masuk (logged in) atau belum. Anda dapat melakukannya dengan menggunakan `request.user.is_authenticated`.
      2. Jika pengguna telah masuk, tampilkan informasi pengguna seperti username dan last login menggunakan `request.user.username` dan `request.user.last_login`.
      3. Gunakan cookies untuk menyimpan informasi terkait sesi, seperti last login time. Anda dapat menggunakan library Django's `django.contrib.sessions` untuk mengelola cookies sesi ini.
      
      Pastikan untuk mengikuti praktik terbaik keamanan dan manajemen sesi yang disarankan oleh Django dalam setiap langkah di atas. Selain itu, lakukan pengujian menyeluruh untuk memastikan bahwa aplikasi Anda berfungsi dengan baik.



 ## Pertanyaan Tugas 5

1. **Manfaat dan Penggunaan Selector dalam CSS:**
    - **Element Selector (`tag`):** Selector ini digunakan untuk menargetkan elemen HTML berdasarkan tagnya. Misalnya, `p` akan menargetkan semua elemen paragraf.
    - **Class Selector (`.class`):** Digunakan untuk menargetkan elemen berdasarkan kelas CSS. Ini memungkinkan penggunaan gaya yang sama pada beberapa elemen tanpa harus mengulangi aturan CSS.
    - **ID Selector (`#id`):** Menargetkan elemen berdasarkan ID mereka. Diperlukan bahwa ID unik dalam halaman HTML tertentu.
    - **Attribute Selector (`[attribute]`):** Digunakan untuk menargetkan elemen berdasarkan atribut dan nilainya, seperti `[type="text"]` untuk menargetkan input dengan tipe teks.

2. **HTML5 Tags:**
    - **`<article>`:** Menandakan konten independen yang dapat berdiri sendiri.
    - **`<section>`:** Menandakan bagian dalam dokumen.
    - **`<header>`:** Mengandung elemen-elemen pengantar atau navigasi untuk bagian tertentu.
    - **`<footer>`:** Berisi informasi penutupan atau footer dokumen atau bagian.
    - **`<nav>`:** Menyimpan tautan navigasi atau menu.
    - **`<aside>`:** Menunjukkan konten yang terkait dengan konten yang dielilinginya, seperti sidebar.
    - **`<figure>` dan `<figcaption>`:** Untuk menambahkan gambar dan keterangan.
    - **`<time>`:** Menunjukkan waktu atau tanggal.

3. **Perbedaan Margin dan Padding:**
    - **Margin:** Menentukan ruang di luar elemen dan memengaruhi jarak antara elemen dan elemen lainnya.
    - **Padding:** Menentukan ruang di dalam elemen dan memengaruhi jarak antara batas elemen dan kontennya sendiri.

4. **Perbedaan Tailwind dan Bootstrap:**
    - **Tailwind CSS:** Memiliki pendekatan utility-first, di mana kelas-kelas kecil digunakan untuk membangun tata letak dan desain. Tidak ada komponen bawaan.
    - **Bootstrap:** Menyediakan kumpulan komponen yang sudah dibangun dan dapat disesuaikan dengan menggunakan kelas-kelas mereka. Pendekatan yang lebih mendekati konsep komponen.

    **Kapan Menggunakan Bootstrap atau Tailwind:**
    - **Bootstrap:** Cocok untuk proyek yang memerlukan komponen yang telah dirancang dengan baik dan cepat diimplementasikan. Cocok untuk pengembang yang ingin menghemat waktu dalam mengembangkan antarmuka pengguna.
    - **Tailwind:** Cocok untuk pengembang yang ingin lebih banyak kendali atas desain dan tidak keberatan menulis lebih banyak kode HTML dan CSS. Fleksibel dan cocok untuk proyek dengan desain khusus.

5. **Langkah-langkah Implementasi:**
   
    - **Element Selector dan Class Selector:**
        1. Identifikasi elemen-elemen yang perlu diberi gaya.
        2. Tulis aturan CSS menggunakan Element Selector dan Class Selector.
        3. Terapkan aturan CSS pada elemen-elemen di halaman HTML Anda.

    - **ID Selector:**
        1. Identifikasi elemen yang unik dan memerlukan gaya khusus.
        2. Tulis aturan CSS menggunakan ID Selector.
        3. Terapkan aturan CSS pada elemen dengan ID tersebut.

    - **Attribute Selector:**
        1. Tentukan elemen yang ingin Anda targetkan berdasarkan atributnya.
        2. Tulis aturan CSS menggunakan Attribute Selector.
        3. Terapkan aturan CSS pada elemen dengan atribut tersebut.

    - **HTML5 Tags:**
        1. Tentukan di mana tag HTML5 dapat meningkatkan struktur dan makna.
        2. Gantilah tag HTML yang ada atau tambahkan tag baru sesuai kebutuhan.
        3. Terapkan CSS atau gaya sesuai kebutuhan pada tag HTML5 tersebut.

    - **Margin dan Padding:**
        1. Pahami elemen-elemen yang memerlukan ruang tambahan di dalam atau di sekitarnya.
        2. Gunakan aturan CSS untuk menentukan Margin dan Padding yang sesuai.
        3. Terapkan aturan CSS pada elemen-elemen tersebut.

    - **Tailwind atau Bootstrap:**
        1. Pilih antara Tailwind atau Bootstrap berdasarkan kebutuhan dan preferensi.
        2. Terapkan Tailwind CSS atau Bootstrap sesuai dengan dokumentasi masing-masing.
        3. Sesuaikan komponen atau gaya sesuai kebutuhan proyek.
   

  ## Pertanyaan Tugas 6


   1. **Asynchronous vs. Synchronous Programming**

      Asynchronous programming memungkinkan eksekusi tugas-tugas tanpa harus menunggu tugas sebelumnya selesai. Ini memungkinkan aplikasi untuk tetap responsif terhadap input pengguna dan meningkatkan kinerja. Synchronous programming, sebaliknya, memproses tugas satu per satu dan menunggu setiap tugas selesai sebelum melanjutkan ke tugas berikutnya.

   2. **Paradigma Event-Driven Programming dalam JavaScript dan AJAX**

      Paradigma event-driven programming berfokus pada penggunaan event dan event listener. Dalam konteks JavaScript dan AJAX, ini berarti program merespons kejadian (event) tertentu, seperti klik tombol atau permintaan AJAX selesai. Sebagai contoh pada tugas ini, event-driven programming dapat dilihat dalam penanganan klik tombol "Add Product by AJAX".

   3. **Penerapan Asynchronous Programming pada AJAX**

      Pada AJAX, asynchronous programming memungkinkan permintaan data dari server dilakukan tanpa harus menunggu tanggapan dari server. Dengan ini, halaman web tetap responsif tanpa harus me-refresh seluruh halaman. Implementasi ini terlihat dalam fungsi `addProduct` yang menggunakan `fetch` API untuk mengirim permintaan tanpa menghentikan eksekusi script.

   4. **Fetch API vs. jQuery pada Penerapan AJAX**

      **Fetch API:**
      - **Kelebihan:**
        - Terintegrasi dengan JavaScript modern.
        - Lebih ringan dan cepat dibandingkan dengan library eksternal seperti jQuery.
        - Mendukung Promises untuk penanganan asynchronous yang lebih baik.
      - **Kekurangan:**
        - Memerlukan sedikit lebih banyak kode dibandingkan dengan jQuery.
      
      **jQuery:**
      - **Kelebihan:**
        - Mudah digunakan dan mempersingkat kode.
        - Kompatibilitas dengan berbagai browser.
        - Sintaks yang sederhana dan mudah dipahami.
      - **Kekurangan:**
        - Tambahan berat karena mungkin memuat fitur yang tidak diperlukan.
        - Kurang mendukung konsep Promises.

**Pendapat Pribadi:**
      Pilihan antara Fetch API dan jQuery tergantung pada kebutuhan dan preferensi. Untuk proyek kecil atau jika fokus pada kecepatan dan performa, menggunakan Fetch API bisa menjadi pilihan yang lebih baik. Namun, jika proyek membutuhkan kesederhanaan dan dukungan lintas browser yang kuat, jQuery masih merupakan pilihan yang valid.

5. **Implementasi Checklist secara Step-by-Step**
      
      1. **Analisis Kebutuhan Proyek:**
         - Tentukan kebutuhan desain dan fungsionalitas.
      
      2. **Pemilihan CSS Selector:**
         - Identifikasi elemen-elemen yang memerlukan gaya umum.
      
      3. **Penggunaan HTML5 Tags:**
         - Sesuaikan struktur HTML dengan tag HTML5.
      
      4. **Memahami Margin dan Padding:**
         - Gunakan Margin dan Padding sesuai kebutuhan.
      
      5. **Memahami Perbedaan Tailwind dan Bootstrap:**
         - Pilih antara Tailwind atau Bootstrap berdasarkan kebutuhan dan preferensi.
      
      6. **Langkah-langkah Implementasi:**
         - Implementasikan aturan CSS dan struktur HTML sesuai dengan pilihan desain dan framework.


