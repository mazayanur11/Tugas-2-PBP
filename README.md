Nama : Mazaya Nur Labiba
NPM  : 2106639485
Kelas: C

Link aplikasi Heroku yang sudah dideploy: https://tugas2maza.herokuapp.com/catalog/

Jawaban:
1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya
   ![This is an image](/Bagan_MazayaNurLabiba.jpg)
   
2. Jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
   - Kaitan antara urls.py dan views.py adalah urls.py akan mem-parse argumen dan diteruskan ke views.py yang terkait, kemudian views.py akan mengambil request tersebut dan memberikan web response.
   - Kaitan antara views.py dan berkas html adalah views.py akan mengambil template dari berkas html, kemudian template tersebut di-merge di views.py dan diolah serta digabungkan.
   - Kaitan antara views.py dan models.py adalah models.py akan mengambil data dan diberikan ke views.py.

   Kaitan antara urls.py, views.py, models.py, dan berkas html adalah urls.py yang bertugas mem-parse argumen dari user dan berkas html yang berisi template web akan memberikan outputnya ke views.py. Selanjutnya, ketika ada query pemanggilan data dari views.py, models.py akan menjembatani pemanggilan data ke database. Kemudian views.py akan menggabungkan dan mengolahnya sehingga menjadi satu halaman web yang utuh.

3. Jelaskan kenapa menggunakan virtual environment? 
   Virtual environment berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Virtual environment ini juga berguna untuk memastikan kalau versi dari sebuah library yang digunakan di satu project tidak akan berubah apabila kita melakukan sebuah update di library yang sama di project lain-nya. 

4. Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun dianjurkan menggunakan environment agar versi dari sebuah library yang digunakan di satu project tidak akan berubah apabila kita melakukan sebuah update di library yang sama di project lain-nya.

5. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
   1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
   Meng-import models yang sudah dibuat sebelumnya ke dalam file views.py dengan perintah "from katalog.models import CatalogItem". Selanjutnya, memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel, kemudian menambahkan variabel ketiga pada pengembalian fungsi render di fungsi yang sudah dibuat sebelumnya di views.py.
   2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
   Mendaftarkan aplikasi catalog ke dalam urls.py yang ada pada folder project_django dengan menambahkan "path('catalog/', include('katalog.urls'))," pada variabel urlpatterns.
   3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
   Melakukan iterasi terhadap variabel list_barang yang telah ikut di render ke dalam HTML.
   4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
   - Menambahkan konfigurasi berikut pada settings.py di project_django, dengan perintah sebagai berikut:
   PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
   STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
   - Melakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub
   - Menyalin API key dari akun Heroku dan membuat app baru bernama "tugas2maza"
   - Membuat konfigurasi repositori GitHub dengan pasangan Name-Value dari Heroku
   - Menambahkan variabel repository secret baru untuk melakukan deployment
   - Menyambungkan Heroku dengan repositori Github yang sesuai
   - Link aplikasi Heroku sudah dapat dibuka oleh teman-teman