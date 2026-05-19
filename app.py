from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'nama': request.form['nama'],
        'umur': request.form['umur'],
        'tanggal_lahir': request.form['tanggal_lahir'],
        'alamat': request.form['alamat'],
        'no_hp': request.form['no_hp'],
        'pesan': request.form['pesan']
    }
    print(data)
    return redirect(url_for('quotes'))

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

if __name__ == '__main__':
    app.run(debug=True)