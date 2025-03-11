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
