from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data sepatu (sementara, tanpa database)
sepatu_list = [
    {"id": 1, "nama": "Nike Air Force 1", "harga": 1200000, "gambar": "https://via.placeholder.com/150"},
    {"id": 2, "nama": "Adidas Superstar", "harga": 950000, "gambar": "https://via.placeholder.com/150"},
    {"id": 3, "nama": "Converse All Star", "harga": 750000, "gambar": "https://via.placeholder.com/150"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

@app.route('/sepatu')
def daftar_sepatu():
    return render_template('daftar_sepatu.html', sepatu_list=sepatu_list)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah_sepatu():
    if request.method == 'POST':
        nama = request.form['nama']
        harga = request.form['harga']
        gambar = request.form['gambar']
        id_baru = max([s['id'] for s in sepatu_list]) + 1 if sepatu_list else 1
        sepatu_baru = {"id": id_baru, "nama": nama, "harga": int(harga), "gambar": gambar}
        sepatu_list.append(sepatu_baru)
        return redirect(url_for('daftar_sepatu'))
    return render_template('tambah_sepatu.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_sepatu(id):
    sepatu = next((s for s in sepatu_list if s['id'] == id), None)
    if not sepatu:
        return "Sepatu tidak ditemukan", 404
    if request.method == 'POST':
        sepatu['nama'] = request.form['nama']
        sepatu['harga'] = int(request.form['harga'])
        sepatu['gambar'] = request.form['gambar']
        return redirect(url_for('daftar_sepatu'))
    return render_template('edit_sepatu.html', sepatu=sepatu)

@app.route('/hapus/<int:id>')
def hapus_sepatu(id):
    global sepatu_list
    sepatu_list = [s for s in sepatu_list if s['id'] != id]
    return redirect(url_for('daftar_sepatu'))

if __name__ == '__main__':
    app.run(debug=True)
