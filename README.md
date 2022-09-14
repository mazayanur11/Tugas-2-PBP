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
   