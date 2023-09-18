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





   


   

   
