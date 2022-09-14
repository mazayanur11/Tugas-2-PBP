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

   Kaitan antara urls.py, views.py, models.py, dan berkas html adalah urls.py yang bertugas mem-parse argumen dari user, models.py yang bertugas mengambil data, dan berkas html yang berisi template web, akan memberikan outputnya ke views.py. Kemudian views.py akan menggabungkan ketiga output tersebut dan mengolahnya sehingga menjadi satu halaman web yang utuh.

3. Jelaskan kenapa menggunakan virtual environment? 
   Virtual environment berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Virtual environment ini juga berguna untuk memastikan kalau versi dari sebuah library yang digunakan di satu project tidak akan berubah apabila kita melakukan sebuah update di library yang sama di project lain-nya. 

4. Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun dianjurkan menggunakan environment agar versi dari sebuah library yang digunakan di satu project tidak akan berubah apabila kita melakukan sebuah update di library yang sama di project lain-nya.

5. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
   Cara yang saya lakukan untuk mengimplementasikan poin 1 sampai 4 di atas adalah:
   1. Membuat repositori baru dari template yang sudah diberikan
   2. Melakukan clone repositori tersebut ke komputerdengan perintah git clone <URL_REPOSITORI>
   3. Masuk ke dalam repositori yang sudah di clone ke komputer dan membuat sebuah vitual environment dengan perintah python -m venv env
   4. Menyalakan virtual environment dengan perintah env\Scripts\activate.bat
   5. Menginstall dependencies yang dibutuhkan untuk project Django dengan perintah pip install -r requirements.txt
   6. Menjalankan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal
   7. Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal
   8. Mendaftarkan aplikasi katalog ke dalam urls.py yang ada pada folder project_django dengan menambahkan path('catalog/', include('katalog.urls')), pada variabel urlpatterns
   9. Meng-import models yang sudah dibuat sebelumnya ke dalam file views.py dengan cara from katalog.models import CatalogItem
   10. Memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel, kemudian menambahkan variabel ketiga pada pengembalian fungsi render di fungsi yang sudah dibuat sebelumnya di views.py
   11. Mengubah Fill me! yang ada di dalam HTML tag <p> menjadi nama dan student id
   12. Untuk menampilkan daftar barang ke dalam tabel, perlu melakukan iterasi terhadap variabel list_barang yang telah ikut di render ke dalam HTML
   13.Menambahkan konfigurasi berikut pada settings.py di project_django
   PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
   STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
   14. Melakukan add, commit, dan push perubahan yang sudah dilakukan untuk menyimpannya ke dalam repositori GitHub
   15. Menyalin API key dari akun Heroku
   16. 