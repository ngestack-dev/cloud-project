## Cloud-Project

Repository ini berisi tugas mata kuliah Cloud Computing, yaitu membuat API sederhana dengan Flask serta React + Vite

`by Hardi`

### Instalasi

#### Backend

1. Buka terminal lalu ke direktori `cloud-project/backend`
2. Lalu jalankan perintah `python -m venv venv`
3. Masuk ke virtual environtment dengan perintah `venv\Scripts\activate`
4. Install install flask dengan perintah `pip install Flask`


#### Frontend
1. Buka terminal lalu ke direktori `cloud-project/frontend`
2. Di terminal jalankan perintah `npm create vite@latest my-react-app -- --template react`
3. Kemudian ke direktori `my-react-app`
4. Terakhir jalankan `npm install` dan `npm run dev`

### Contoh Penggunaan

#### Backend

1. Buat file dengan contoh nama `app.py`<br>
Kemudian isi dengan 
```py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

```


2. Lalu di terminal jalan perintah `python app.py`
3. Buka web browser dan buka alamat `http://localhost:5000/`
4. Akan muncul tulisan "Hello from Flask" jika berhasil

#### Frontend

1. Buka file `App.jsx` di folder `frontend/my-react-app/src`
2. Ganti isinya dengan kode berikut
```jsx
import React from 'react';

function App() {
  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Hello from React + Vite!</h1>
      <p>This is a simple React app built with Vite.</p>
    </div>
  );
}

export default App;
```

3. Kemudian jalankan di terminal dengan perintah `npm run dev`
4. Terakhir buka browser lalu pergi ke alamat `http://localhost:5173/`
5. Jika berhasil akan muncul tulisan "Hello from React + Vite"

### Integrasi React & Flask

#### - Flask

1. Ganti konten pada file `app.py` dengan kode berikut 
```py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/data')
def get_data():
    return jsonify({"data": "Hello from Flask API"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
 2. Masuk kedalam virtual environment dengan perintah `venv\Scripts\activate` di terminal pada direktori `cloud-project/backend`

 3. Jalankan server dengan perintah `python app.py`
 4. Kemudian akses endpoint pada alamat `http://localhost:5000/api/data`
 5. Jika berhasil akan memunculkan tulisan "Hello from Flask API"

 #### - React
 1. Ganti konten pada file `App.jsx` dengan kode berikut
 ```jsx
 import React, { useState, useEffect } from 'react';

function App() {
  const [apiData, setApiData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/data')
      .then(response => response.json())
      .then(data => {
        setApiData(data.data);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>React & Flask Integration</h1>
      <p>{apiData ? apiData : "Loading data..."}</p>
    </div>
  );
}

export default App;
```

2. Di terminal direktori `cloud-project/frontend/my-react-app` jalankan perintah `npm run dev`
3. Kemudian akses `http://localhost:5173/` pada web browser
4. Jika berhasil, akan muncul tulisan
```
React & Flask Integration
Hello from Flask API
```
<br>

`Note!`<br>
Jika tidak muncul tulisan "Hello from Flask API" melainkan "Loading data..." maka lakukan prosedur berikut.

1. Buka file `requirements.txt`, kemudian tambahkan `Flask-CORS==4.0.0` pada baris baru

2. Selanjutnya masuk ke virtual environment, kemudian jalankan perintah `pip install -r requirements.txt`
3. Jika sudah, jalankan kembali React dan Flask sesuai prosedur sebelumnya.

## Integrasi Flask dengan PostgreSQL

1. Masuk kedalam virtual environment dengan perintah `venv\Scripts\activate` di terminal pada direktori `cloud-project/backend`
2. Jalankan perintah `pip install psycopg2-binary` untuk menginstal Psycopg2
3. Selanjutnya, modifikasi konten pada `app.py` dengan kode dibawah ini
```python
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2  # Import library untuk koneksi ke PostgreSQL

# Fungsi untuk koneksi ke database PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",  # Alamat host database PostgreSQL
        database="test_db",  # Sesuaikan dengan nama database yang Anda buat
        user="student",  # Sesuaikan dengan nama user database
        password="password"  # Sesuaikan dengan password user database
    )
    return conn

# Inisialisasi Flask
app = Flask(__name__)

@app.route('/')  # Endpoint utama untuk mengembalikan pesan JSON
def home():
    return jsonify({"message": "Hello from Flask!"})

# Endpoint untuk membaca data dari tabel 'items'
@app.route('/api/items', methods=['GET'])
def get_items():
    conn = get_db_connection()  # Membuka koneksi ke database
    cur = conn.cursor()  # Membuat objek cursor untuk eksekusi query
    cur.execute("SELECT id, name, description FROM items;")  # Query untuk mengambil data dari tabel 'items'
    rows = cur.fetchall()  # Mengambil semua hasil query
    cur.close()  # Menutup cursor
    conn.close()  # Menutup koneksi database

    # Mengonversi hasil query menjadi format JSON
    items = [{"id": row[0], "name": row[1], "description": row[2]} for row in rows]
    return jsonify(items)  # Mengembalikan data dalam format JSON

# Endpoint untuk menambahkan data ke tabel 'items'
@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.json  # Mengambil data dari request body dalam format JSON
    name = data['name']  # Mengambil nilai 'name' dari request
    description = data['description']  # Mengambil nilai 'description' dari request

    conn = get_db_connection()  # Membuka koneksi ke database
    cur = conn.cursor()  # Membuat objek cursor untuk eksekusi query
    
    # Menjalankan query untuk menambahkan data baru ke tabel 'items'
    cur.execute("INSERT INTO items (name, description) VALUES (%s, %s) RETURNING id;", (name, description))
    new_id = cur.fetchone()[0]  # Mengambil ID dari item yang baru dimasukkan
    conn.commit()  # Menyimpan perubahan ke database
    cur.close()  # Menutup cursor
    conn.close()  # Menutup koneksi database

    # Mengembalikan respons JSON dengan data item yang baru ditambahkan
    return jsonify({"id": new_id, "name": name, "description": description}), 201

# Jalankan Flask jika file dieksekusi secara langsung
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Menjalankan aplikasi Flask dengan mode debug aktif
```
4. Buka PgAdmin kemudian login dan buat database baru (contoh: test_db)
5. Buat table dengan menggunakan query pgAdmin
```sql
CREATE TABLE IF NOT EXISTS items (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  description TEXT
);
```
6. Kemudian jalankan dengan perintah `python app.py`
7. Selanjutnya cek koneksi database dengan perintah `psql -U postgres -d test_db` (isi 'postgres' dengan user anda)
8. Jika sudah terkoneksi, tes endpoint dengan perintah
```
Invoke-WebRequest -Uri "http://localhost:5000/api/items" -Method GET
```
Kemudian
```
$headers = @{
    "Content-Type" = "application/json"
}

$body = @{
    "name" = "Test Item"
    "description" = "Test Description"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5000/api/items" -Method POST -Headers $headers -Body $body

```
`!Note` _Gunakan perintah ini jika anda menggunakan terminal powershell_<br>

9. Terakhir, pergi ke alamat `http://localhost:5000/api/items` di web browser, dan jika ada tulisan description, id, dan name maka integrasi berhasil

## Dockerization - Part 1

  1. Pertama, tambahkan konten berikut ke file `requirements.txt`
  ```
  flask
flask-cors
psycopg2-binary
```
  2. Kemudian buka aplikasi Docker Dekstop
  2. Tunggu hingga muncul status "Docker is Running"
  3. Selanjutnya buat file di direktori `/backend` dengan nama `Dockerfile`
  4. Isi konten file tersebut dengan kode berikut
  ```Docker

# Menggunakan image dasar Python versi 3.9 dengan varian slim (lebih ringan)
FROM python:3.9-slim

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt requirements.txt

# Menginstal dependencies yang tercantum di requirements.txt tanpa menyimpan cache
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh isi direktori proyek ke dalam container
COPY . .

# Membuka port 5000 agar container dapat menerima koneksi
EXPOSE 5000

# Menjalankan aplikasi dengan perintah default
CMD ["python", "app.py"]

```

6. Selanjutnya, jalankan perintah `docker build -t flask-backend:1.0 .` di direkotri `/backend` 
7. Kemudian cek dengan perintah `docker image`
8. Selanjutnya, jalankan container dengan perintah `docker run -d -p 5000:5000 --name flask-container flask-backend:1.0`
9. Cek apakah container berjalan dengan perintah `docker ps`
9. Kemudian pergi alamat `http://localhost:5000/` di browser
10. Jika berhasil, akan muncul tulisan "Hello from Flask"