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

