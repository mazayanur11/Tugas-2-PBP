Nama    : Mazaya Nur Labiba
NPM     : 2106639485
Kelas   : C

Link aplikasi Heroku yang sudah dideploy: https://tugas2maza.herokuapp.com/mywatchlist/

Jelaskan perbedaan antara JSON, XML, dan HTML!
- HTML atau HyperText Markup Language merupakan sebuah markup language yang berfokus pada penyajian data dalam bentuk Web.
- XML atau Extensible Markup Language merupakan suatu markup language yang menyimpan data dalam format teks dan tag sederhana. 
- JSON atau JavaScript Object Notation merupakan suatu format yang dibuat di atas JavaScript untuk merepresentasikan data dalam bentuk key dan value. 

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Di dalam suatu platform, terdapat pertukaran data/data delivery antara clients dan juga server. Dengan menggunakan data delivery tersebut, tentu mempermudah kita untuk melakukan pengiriman data. Pengiriman data bisanya menggunakan format HTML, XML, ataupun JSON agar data yang dideliver bisa diterima dengan baik oleh user dan mudah dipahami berbagai programming language.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Menjalankan perintah python manage.py startapp mywatchlist di directory repository yang ingin dibuat untuk membuat aplikasi baru.
2. Menambahkan path('mywatchlist/', include('mywatchlist.urls')), di urls.py pada project_django. Kemudian, menambahkan urlpatterns = [ ..., path('xml/', show_xml, name='show_xml'), path('json/', show_json, name='show_json'), ... ] di urls.py pada mywatchlist
3. Membuat model baru di models.py pada mywatchlist bernama MyWatchListItem dengan fields watched, title, rating, release_date, dan review. Setelah itu, dilakukan migrasi agar model terbuat pada database.
4. Membuat file initial_mywatchlist_data.json, kemudian menambahkan 10 data untuk objek MyWatchList yang sudah dibuat sebelumnya.
5. Menambahkan function pada views.py untuk menampilkan data dalam bentuk HTML, XML, dan JSON.
6. Melakukan git add, commit, dan push ke repositori github yang sesuai

Screenshot akses URL HTML menggunakan Postman 
![This is an image](/mywatchlist/Postman_HTML_MazayaNurLabiba.jpg)

Screenshot akses URL XML menggunakan Postman 
![This is an image](/mywatchlist/Postman_XML_MazayaNurLabiba.jpg)

Screenshot akses URL JSON menggunakan Postman 
![This is an image](/mywatchlist/Postman_JSON_MazayaNurLabiba.jpg)