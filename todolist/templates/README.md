<p>Nama    : Mazaya Nur Labiba</p>
<p>NPM     : 2106639485</p>
<p>Kelas   : C</p>
<br>
<p>Link Deployment Heroku: <a href="https://tugas2maza.herokuapp.com/todolist">disini</a></p>
<br>
1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
<ul>
<li>Inline CSS adalah menuliskan code CSS atau menghias elemen tersebut di dalam tag HTML-nya masing-masing dengan cara menambahkan style pada tag. Kelebihan dari style ini adalah mudah diperbaiki dan diatur karena hanya terfokus untuk mengedit satu elemen saja, namun kekurangannya adalah tidak efisien untuk mengedit keseluruhan website karena harus mengubah tiap elemen satu per satu.
<li>Internal CSS adalah menuliskan code CSS atau menghias halaman suatu website di dalam file HTML itu sendiri dengan cara menambahkan <style></style> pada bagian header. Kelebihan dari style ini adalah mudah diperbaiki dan diatur karena hanya terfokus untuk mengedit satu halaman HTML saja, namun kekurangannya adalah tidak efisien jika terdapat banyak halaman web yang dibuat dan harus mengedit setiap halamannya satu per satu.
<li>External CSS adalah menuliskan code CSS atau menghias website dengan membuat suatu file CSS baru kemudian menghubungkannya dengan file HTML yang ingin dihias, misal nama file CSS yang dibuat adalah style.css, maka di bagian header HTML dituliskan <link rel="stylesheet" href="style.css"/> untuk merujuk ke file CSS yang sudah dibuat sebelumnya. Kelebihan dari style ini adalah lebih rapi dan efisien dalam menghias website karena style diletakkan di halaman terpisah, namun kekurangannya adalah sulit untuk mengakses elemen terkecil dalam suatu halaman web jadi tidak efisien jika digunakan untuk halaman atau elemen yang sedikit.
</ul>
<br>
2. Jelaskan tag HTML5 yang kamu ketahui.
<ul>
<li> h yang merupakan text dengan berbagai macam ukuran, h1 adalah ukuran terbesar kemudian h6 yang terkecil.
<li>title yang merupakan judul dari halaman website tersebut yang diletakkan di header.
<li>p yang merupakan paragraf dalam website.
<li>br yang merupakan jarak antar satu elemen dengan elemen lainnya.
<li>ul dan  yang merupakan urutan list atau nomor dalam sebuah website.
<li>img untuk menambahkan gambar dalam sebuah website.
<li>button untuk menambahkan tombol dalam sebuah website.
<li>a href untuk menghubungkan website ke sebuah link atau halaman website lain.
<li>input untuk meminta input dari user berupa text, tombol, atau yang lainnya.
<li>form yang merupakan suatu struktur form dalam website yang nantinya di dalam form tersebut dapat ditambahkan elemen lain seperti input, tombol, dan lain-lain.
<li>label yang merupakan suatu text yang fleksibel dan dapat diatur style-nya.
<li>dan masih banyak lagi tag lainnya
</ul>
<br>
3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
<ul>
<li> Terdapat basic element selector dengan menuliskan tipe dari tag tersebut, seperti h1 {}, body {}, dan lain-lain.
<li> (.) yang merupakan selector untuk element di dalam class dalam sebuah div.
</ul>
<br>
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
<ul>
<li> Meng-import link bootstrap ke dalam base.html, yaitu HTML yang di-extends oleh keempat HTML lainnya yang ingin dihias dengan cara menambahkan <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous"> pada header-nya dan   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script> pada body-nya
<li> Menghias keempat halaman tersebut dengan internal CSS dan inline CSS agar lebih mudah untuk mengakses masing-masing halaman website dan masing-masing elemen kemudian menghiasnya sesuai keinginan
<li> Mengubah HTML dari register.html dan todolist.html dari form as table menjadi tag form manaual dari HTML agar lebih mudah dan fleksibel dalam menghias halaman website
<li> Mengubah function register dan create_task di views.py agar dapat menyesuaikan message yang ditampilkan serta data dari user yang dibuat dan task yang dibuat
<li> Membuat card pada todolist.html sebanyak jumlah task yang telah dibuat atau akan dibuat dengan menerapkan for loop list_barang yang berisi semua task dari user yang sedang login
<li> Karena saya menggunakan bootstrap dalam menghias keempat halaman web, jadi keempat halaman website tersebut sudah otomatis menjadi responsive
<li> Membuat animasi hover pada card dengan internal CSS untuk mengedit transition card
</ul>