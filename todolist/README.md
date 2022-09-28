Nama    : Mazaya Nur Labiba
NPM     : 2106639485
Kelas   : C

Link ke aplikasi Heroku: https://tugas2maza.herokuapp.com/todolist

1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
{% csrf_token %} pada elemen <form> digunakan untuk membandingkan key crsf user ketika ingin melakukan method POST atau GET. Hal tersebut berfungsi untuk memverifikasi bahwa yang melakukan method tersebut adalah user yang terkait. Sehingga, form dapat disubmit dan diakses oleh user yang tepat.
Jika tidak ada potong kode tersebut pada elemen <form>, hal yang sebelumnya hanya bisa dilakukan oleh user yang terkait, menjadi bisa dilakukan secara umum. Hal yang dimaksud adalah logout, delete account, dan lain-lain. Ketika ada orang lain yang mempunyai akses button ke href link tersebut, akun tersebut dapat terhapus atau logout sang user sadari.

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Kita dapat membuat elemen <form> secara manual tanpa menggunakan generator seperti {{ form.as_table }}. Hal tersebut dapat dilakukan dengan cara membuat form dengan tag <form>. Kemudian, menggunakan {% csrf_token %} untuk memverifikasi key crsf user yang terkait. Selanjutnya, membuat kolom untuk input user dengan <input>. Lalu, menggunakan method POST pada fungsi di views.py untuk mengunggah input user ke database. Kemudian, menggunakan method get untuk mengambil jawaban user dari database.

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pertama, user memasukkan input kemudian melakukan submit di HTML form. Setelah itu, input tersebut disimpan ke dalam database dengan perintah form.save() yang ada pada fungsi create_task di views.py. Kemudian, fungsi tersebut akan merujuk ke fungsi show_todolist untuk dimasukkan ke dalam context agar data tersebut bisa diakses oleh template HTML kemudian ditampilkan di website.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Menjalankan python manage.py startapp todolist di folder repo yang terkait
- Menambahkan path('todolist/', include('todolist.urls')), di urls.py project_django agar dapat menjalankan fungsi show_todolist yang ada di views.py
- Menambahkan 'todolist' di setting.py INSTALLED_APPS
- Membuat class Task di model.py kemudian mengisinya dengan variabel user, date, title, description, is_finished
- Membuat fungsi login, logout, register yang masing masing terhubung dengan login.html dan register.html
- Membuat restriksi agar user wajib login dahulu dengan menambahkan @login_required(login_url='/todolist/login/') diatas fungsi yang merupakan main dari project
- Menampikan user dengan mengakses variable yang ada di context ({{username}}) dan membuat dua buah button yang masing-masing memiliki command untuk logout dan tambah task baru, kemudian membuat tabel untuk menampilkan data-data todolist yang sudah disubmit ke database
- Membuat form baru di create-task.html agar user dapat membuat task baru melalui page tersebut
- Membuat tombol ubah status dan hapus task di todolist.html, kemudian membuat fungsi status dan hapus dengan parameter request dan id untuk menjalankan tombol tersebut sesuai dengan task yang tersedia, tidak lupa juga untuk menambahkan @login_required(login_url='/todolist/login/') diatas fungsi agar user wajib login dahulu untuk menjalankan tombol tersebut
- Meng-import dan menambahkan path dari semua fungsi yang telah dibuat di views.py ke urls.py
- Deploy ke heroku dan membuat 2 user dengan masing-masing 3 dummy list to do