## Cloud-Project

Repository ini berisi tugas mata kuliah Cloud Computing, yaitu membuat API sederhana dengan Flask

### Instalasi

<!-- #### Backend -->

1. Buka terminal lalu ke direktori `cloud-project/backend`
2. Lalu jalankan perintah `python -m venv venv`
3. Masuk ke virtual environtment dengan perintah `venv\Scripts\activate`
4. Install install flask dengan perintah `pip install Flask`


### Contoh Penggunaan

<!-- #### Backend -->

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

