Nama = Mazaya Nur Labiba
NPM = 2106639485
Kelas = C

Link deployment Heroku = https://tugas2maza.herokuapp.com/todolist

Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Dalam synchronous, diperlukan sebuah input satu per satu untuk melakukan pekerjaan dari function yang sudah dibuat. Dan metode synchronous perlu menunggu sebuah parameter atau perintah sebelumnya agar berjalan. Sementara itu, asynchronous dapat berjalan atau kita dapat memberikan input sebanyak apapun yang kita mau bersamaan dan akan diproses secara bersamaan. Dalam ajax, asynchronous berperan untuk membuat web menjadi lebih efisien karena setiap instruksi yang user berikan akan dikelola oleh mesin ajax dan diproses secara asynchronous di server-side dah user tidak memerlukan refresh page agar instruksi yang diberikan dapat muncul.
Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event driven programming adalah sebuah paradigma yang membuat flow dari program bergantung pada event yang dilakukan oleh user-client. Contohnya adalah ketika mouse diklik, digeser, menekan sesuatu, dan lain-lain. Setiap event yang terjadi dipasangkan dengan sebuah function yang akan jalan dengan otomatis ketika event yang dipasangkan muncul. Pada tugas ini, salah satu event programming pada JS yang saya aplikasikan adalah menjalankan fungsi yang dibentuk untuk memunculkan atau menghilangkan modal (pop up) untuk melakukan add task. Event yang digunakan adalah data-bs-dismiss="modal". Selain itu, ada juga ketika form yang sudah dibuat untuk mengirim task dan description ke database, ketika di submit akan menjalankan fungsi untuk post data dengan Ajax query. Ada pula .ready(function()) yang berarti ketika pada halaman pertama kali muncul dan siap ditampilan, akan menjalankan perintah-perintah yang sudah diatur pada fungsi tersebut.
Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous pada ajax adalah membuat website tidak memerlukan reload ketika terjadi sedikit perubahan data. Contoh penerapan asynchronous pada ajax adalah kita dapat event driven programming yang sudah disebutkan pada sebelumnya. Ajax akan menampung perintah yang akan dijalankan lalu mengirimkannya ke server agar datanya diubah secara asynchronous. Selain itu, implementasi lainnya adalah AJAX get dan AJAX post yang mana akan ditrigger ketika html mengirim method post ataupun get yang akan ditangkap oleh ajax. Data yang ditangkap akan dikirimkan ke server tanpa melalui browser reload sehingga memberikan pengalaman browsing lebih baik.
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Import Jquery Ajax dengan tag script
2. Menghapus code for loop menggunakan django syntax serta isinya dan membuat id pada div yang menaungi grid-cols
3. Membuat document.ready function agar ketika website tampil, untuk pertama kalinya ia akan merender data data task yang sudah ada pada server
4. Membuat perintah dalam js yang bernama untuk merender cards todolist yang ada pada database.json dengan method GET yang diarahkan pada url todolist/json. Render kemudian dimasukkan kedalam div yang menaungi grid-cols atau card view.
5. Membuat modal dalam yang membuat ketika button dipencet, akan menampilkan pop up untuk mengisi form dan menambahkan task.
6. 8. Membuat fungsi add_ajax dan mengambil data yang sudah dipost dengan cara request.POST.get dan membuat new object todo kemudian mereturn hasilnya.
7. Dalam modal, terdapat form dengan method POST yang akan memasukkan data ke database. Input dengan type submit yang ada pada form modal akan diarahkan ke todolist/add_task dan memanggil fungsi add_task yang ada pada views.py
8. Membuat perintah yang dalam js yang ketika form dalam modal disubmit, akan mengirimkan response ajax POST ke todolist/add_task dan ditangkap oleh fungsi add_task