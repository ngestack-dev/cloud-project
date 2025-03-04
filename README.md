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