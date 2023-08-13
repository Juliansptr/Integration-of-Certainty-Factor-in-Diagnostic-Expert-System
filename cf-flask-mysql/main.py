from flask import Flask, render_template, redirect, url_for, request, session
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.secret_key = '123'

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'db_cf_flask'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cek-login', methods=['GET', 'POST'])
def cek_login():
    username = request.form['username']
    password = request.form['password']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM login WHERE username=%s AND password=%s",
            (username, password))
    data = cursor.fetchall()
    conn.close()
    if (len(data) > 0):
        session['userlogin'] = request.form['username']
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login', pesan="Login Gagal"))

@app.route('/logout')
def logout():
    session.pop('userlogin', None)
    return redirect(url_for('login', pesan="Sudah Logout"))

@app.route('/admin')
def admin():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    return render_template('admin.html')

@app.route('/gejala')
def gejala():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gejala ORDER BY id_gejala")
    data = cursor.fetchall()
    conn.close()

    return render_template('gejala.html', data = data)

@app.route('/add-gejala')
def add_gejala():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    return render_template('add-gejala.html')

@app.route('/edit-gejala')
def edit_gejala():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    id_gejala = request.args.get('id_gejala')
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gejala WHERE id_gejala=%s", id_gejala)
    data = cursor.fetchone()
    conn.close()
    return render_template('edit-gejala.html', data=data)

@app.route('/save-gejala', methods=['GET', 'POST'])
def save_gejala():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        id_gejala = request.form['id_gejala']
        nama_gejala = request.form['nama_gejala']
        cursor.execute(
            "INSERT INTO gejala(id_gejala, nama_gejala) VALUES (%s,%s)",
            (id_gejala, nama_gejala))
        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        return (str(e))
    return redirect(url_for('gejala'))

@app.route('/update-gejala', methods=['GET', 'POST'])
def update_gejala():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        id_gejala = request.form['id_gejala']
        nama_gejala = request.form['nama_gejala']
        cursor.execute(
            "UPDATE gejala SET nama_gejala=%s WHERE id_gejala=%s",
            (nama_gejala, id_gejala))
        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        return (str(e))
    return redirect(url_for('gejala'))

@app.route('/del-gejala')
def del_gejala():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        id_gejala = request.args.get('id_gejala')
        cursor.execute(
            "DELETE FROM gejala WHERE id_gejala=%s",
            (id_gejala))
        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        return (str(e))
    return redirect(url_for('gejala'))

@app.route('/penyakit')
def penyakit():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM penyakit ORDER BY id_penyakit")
    data = cursor.fetchall()
    conn.close()
    return render_template('penyakit.html', data=data)

@app.route('/add-penyakit')
def add_penyakit():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    return render_template('add-penyakit.html')

@app.route('/edit-penyakit')
def edit_penyakit():
    id_penyakit = request.args.get('id_penyakit')
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM penyakit WHERE id_penyakit=%s", id_penyakit)
    data = cursor.fetchone()
    conn.close()
    return render_template('edit-penyakit.html', data=data)

@app.route('/save-penyakit', methods=['GET', 'POST'])
def save_penyakit():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        id_penyakit = request.form['id_penyakit']
        nama_penyakit = request.form['nama_penyakit']
        cursor.execute(
            "INSERT INTO penyakit(id_penyakit, nama_penyakit) VALUES (%s,%s)",
            (id_penyakit, nama_penyakit))
        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        return (str(e))
    return redirect(url_for('penyakit'))

@app.route('/update-penyakit', methods=['GET', 'POST'])
def update_penyakit():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        id_penyakit = request.form['id_penyakit']
        nama_penyakit = request.form['nama_penyakit']
        cursor.execute(
            "UPDATE penyakit SET nama_penyakit=%s WHERE id_penyakit=%s",
            (nama_penyakit, id_penyakit))
        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        return (str(e))
    return redirect(url_for('penyakit'))

@app.route('/del-penyakit')
def del_penyakit():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        id_penyakit = request.args.get('id_penyakit')
        cursor.execute(
            "DELETE FROM penyakit WHERE id_penyakit=%s",
            (id_penyakit))
        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        return (str(e))
    return redirect(url_for('penyakit'))

@app.route('/pengetahuan')
def pengetahuan():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT pengetahuan.*, penyakit.nama_penyakit, gejala.nama_gejala FROM pengetahuan LEFT JOIN penyakit ON pengetahuan.id_penyakit = penyakit.id_penyakit LEFT JOIN gejala ON pengetahuan.id_gejala = gejala.id_gejala ORDER BY pengetahuan.id_penyakit, pengetahuan.id_gejala")
    data = cursor.fetchall()
    conn.close()
    return render_template('pengetahuan.html', data=data)

@app.route('/add-pengetahuan')
def add_pengetahuan():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM penyakit ORDER BY id_penyakit")
    datapenyakit = cursor.fetchall()
    conn.close()

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gejala ORDER BY id_gejala")
    datagejala = cursor.fetchall()
    conn.close()
    return render_template('add-pengetahuan.html', datapenyakit=datapenyakit, datagejala=datagejala)

@app.route('/edit-pengetahuan')
def edit_pengetahuan():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    id_pengetahuan = request.args.get('id_pengetahuan')
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pengetahuan WHERE id_pengetahuan=%s", id_pengetahuan)
    data = cursor.fetchone()
    conn.close()

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM penyakit ORDER BY id_penyakit")
    datapenyakit = cursor.fetchall()
    conn.close()

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gejala ORDER BY id_gejala")
    datagejala = cursor.fetchall()
    conn.close()

    return render_template('edit-pengetahuan.html', data=data, datapenyakit=datapenyakit, datagejala=datagejala)

@app.route('/save-pengetahuan', methods=['GET', 'POST'])
def save_pengetahuan():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        id_penyakit = request.form['id_penyakit']
        id_gejala = request.form['id_gejala']
        mb = request.form['mb']
        md = request.form['md']
        cursor.execute(
           "INSERT INTO pengetahuan(id_penyakit, id_gejala, mb, md) VALUES (%s,%s,%s,%s)",
           (id_penyakit, id_gejala, mb, md))
        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        return (str(e))
    return redirect(url_for('pengetahuan'))

@app.route('/update-pengetahuan', methods=['GET', 'POST'])
def update_pengetahuan():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        id_pengetahuan = request.form['id_pengetahuan']
        id_penyakit = request.form['id_penyakit']
        id_gejala = request.form['id_gejala']
        mb = request.form['mb']
        md = request.form['md']
        cursor.execute(
           "UPDATE pengetahuan SET id_penyakit=%s, id_gejala=%s, mb=%s, md=%s WHERE id_pengetahuan=%s",
           (id_penyakit, id_gejala, mb, md, id_pengetahuan))
        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        return (str(e))
    return redirect(url_for('pengetahuan'))

@app.route('/del-pengetahuan')
def del_pengetahuan():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        id_pengetahuan = request.args.get('id_pengetahuan')
        cursor.execute(
           "DELETE FROM pengetahuan WHERE id_pengetahuan=%s",
           (id_pengetahuan))
        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        conn.close()
        return (str(e))
    return redirect(url_for('pengetahuan'))

@app.route('/ganti-password')
def ganti_password():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    username = session['userlogin']
    return render_template('ganti-password.html', username=username)

@app.route('/update-password', methods=['GET', 'POST'])
def update_password():
    if session.get('userlogin') is None:
        return redirect(url_for('login', pesan="Belum Login"))
    username = request.form['username']
    lama = request.form['lama']
    baru = request.form['baru']
    konfirmasi = request.form['konfirmasi']
    if (baru == konfirmasi):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM login WHERE username=%s AND password=%s",
               (username, lama))
        data = cursor.fetchall()
        conn.close()
        if (len(data) > 0):
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
               "UPDATE login SET password=%s WHERE username=%s",
               (baru, username))
            conn.close()
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('ganti-password'))
    else:
        return redirect(url_for('ganti-password'))

@app.route('/cf-flask-mysql')
def cf_flask_mysql():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gejala ORDER BY id_gejala")
    datagejala = cursor.fetchall()
    conn.close()
    return render_template('cf-flask-mysql.html', datagejala=datagejala)

@app.route('/proses-cf-flask-mysql', methods=['GET', 'POST'])
def proses_cf_flask_mysql():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gejala ORDER BY id_gejala")
    datagejala = cursor.fetchall()
    conn.close()
    sql = ''
    i = 0
    list_gejala_terpilih = []
    list_id_gejala_terpilih = []
    # mengecek semua chekbox gejala
    for row in datagejala:
        # jika gejala dipilih
        # menyusun daftar gejala misal '1', '2', '3'dst utk dipakai di query
        #request.form['username']
        #if (('gejala'+str(row[1])) in request.form):
        if (request.form.get('gejala'+str(row[0])) is not None):
            if (request.form[('gejala'+str(row[0]))] == 'true'):
                list_gejala_terpilih.append(row[1])
                list_id_gejala_terpilih.append(row[0])
                if (sql == ''):
                    sql = "'"+str(row[0])+"'"
                else:
                    sql = sql + ",'" + str(row[0]) + "'"

    html='';
    id_penyakit_terbesar = ''
    nama_penyakit_terbesar = ''
    list_daftar_cf = []
    list_daftar_penyakit = []
    list_daftar_id_penyakit = []

    cf_terbesar = 0

    # mencari id_penyakit di tabel pengetahuan yang gejalanya dipilih
    perintah = "SELECT id_penyakit FROM pengetahuan WHERE id_gejala IN (" + sql + ") GROUP BY id_penyakit ORDER BY id_penyakit"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(perintah)
    datapenyakitterpilih = cursor.fetchall()
    conn.close()

    if (sql != ''):
        html=html+"<br/>"+perintah+"<br/>"
        c = 0
        for rowpenyakitterpilih in datapenyakitterpilih:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM penyakit WHERE id_penyakit = '"+str(rowpenyakitterpilih[0])+"'")
            rowpenyakit = cursor.fetchone()
            conn.close()
            id_penyakit = str(rowpenyakitterpilih[0])
            nama_penyakit = rowpenyakit[1]
            list_daftar_penyakit.append(nama_penyakit)
            list_daftar_id_penyakit.append(id_penyakit)
#     // memproses id penyakit satu persatu
            html = html + "<br/>Proses Penyakit "+rowpenyakit[1]+"<br/>==============<br/>"
#     // mencari gejala  yang  mempunyai id  penyakit tersebut, agar  bisa  menghitung CF dari MB dan  MD nya
            conn = mysql.connect()
            cursor = conn.cursor()
            perintah="SELECT id_penyakit, mb, md, id_gejala FROM pengetahuan WHERE id_gejala IN (" + sql + ") AND id_penyakit = '" + str(rowpenyakitterpilih[0]) + "'"
            cursor.execute(perintah)
            datagejalapenyakit = cursor.fetchall()
            conn.close()
            html = html + perintah + '<br/>'
            #     // mencari jumlah  gejala yang ditemukan
            jml = len(datagejalapenyakit)
            html = html + 'jml gejala' + str(jml) + '<br/>'
#     // jika gejalanya 1 langsung ketemu CF nya
            if (jml == 1):
                mb = datagejalapenyakit[0][1]
                md = datagejalapenyakit[0][2]
                cf = mb - md
                html = html + "<br/>proses 1<br/>------------------------<br/>"
                html = html + "mb = " + str(mb) + "<br/>"
                html = html + "md = " + str(md) + "<br/>"
                html = html + "cf = mb - md = " + str(mb) + " - " + str(md) + " = " + str(cf) + "<br/><br/><br/>"
                list_daftar_cf.append(cf)
                #     // cek apakah penyakit ini adalah penyakit dgn CF terbesar ?
                if ((id_penyakit_terbesar == '') or (cf_terbesar < cf)):
                    cf_terbesar = cf
                    id_penyakit_terbesar = id_penyakit
                    nama_penyakit_terbesar = nama_penyakit
            elif (jml > 1):
                i=1
                for rowgejalapenyakit in datagejalapenyakit:
                    if (i==1):
                        mblama = rowgejalapenyakit[1]
                        mdlama = rowgejalapenyakit[2]
                        html = html + "mblama = "+str(mblama)+"<br/>"
                        html = html + "mdlama = "+str(mdlama)+"<br/>"
                    elif (i == 2):
                        mbbaru = rowgejalapenyakit[1]
                        mdbaru = rowgejalapenyakit[1]
                        mbsementara = mblama + (mbbaru * (1 - mblama))
                        mdsementara = mdlama + (mdbaru * (1 - mdlama))
                        html = html + "mbsementara = mblama + (mbbaru * (1 - mblama)) = "+str(mblama)+" + ("+str(mbbaru)+" * (1 - "+str(mblama)+")) = "+str(mbsementara)+"<br/>"
                        html = html + "mdsementara = mdlama + (mdbaru * (1 - mdlama)) = "+str(mdlama)+" + ("+str(mdbaru)+" * (1 - "+str(mdlama)+")) = "+str(mdsementara)+"<br/>"
                        if (jml == 2):
                            mb = mbsementara
                            md = mdsementara
                            cf = mb - md
                            html = html + "mb = mbsementara = "+str(mb)+"<br/>"
                            html = html + "md = mdsementara = "+str(md)+"<br/>"
                            html = html + "cf = mb - md = "+str(mb)+" - "+str(md)+" = "+str(cf)+"<br/><br/><br/>"
                            list_daftar_cf.append(cf)
                            #     // cek apakah penyakit ini adalah penyakit dgn CF terbesar ?
                            if ((id_penyakit_terbesar == '') or (cf_terbesar < cf)):
                                cf_terbesar = cf
                                id_penyakit_terbesar = id_penyakit
                                nama_penyakit_terbesar = nama_penyakit
                    elif (i >= 3):
                        mblama = mbsementara
                        mdlama = mdsementara
                        html = html + "mblama = mbsementara = "+str(mblama)+"<br/>"
                        html = html + "mdlama = mdsementara = "+str(mdlama)+"<br/>"
                        mbbaru = rowgejalapenyakit[1]
                        mdbaru = rowgejalapenyakit[2]
                        html = html + "mbbaru = "+str(mbbaru)+"<br/>"
                        html = html + "mdbaru = "+str(mdbaru)+"<br/>"
                        mbsementara = mblama + (mbbaru * (1 - mblama))
                        mdsementara = mdlama + (mdbaru * (1 - mdlama))
                        html = html + "mbsementara = mblama + (mbbaru * (1 - mblama)) = "+str(mblama)+" + ("+str(mbbaru)+" * (1 - "+str(mblama)+")) = "+str(mbsementara)+"<br/>"
                        html = html + "mdsementara = mdlama + (mdbaru * (1 - mdlama)) = "+str(mdlama)+" + ("+str(mdbaru)+" * (1 - "+str(mdlama)+")) = "+str(mdsementara)+"<br/>"
                        # jika ini adalah gejala terakhir berarti CF ketemu
                        if (jml == i):
                            mb = mbsementara
                            md = mdsementara
                            cf = mb - md
                            html = html + "mb = mbsementara = "+str(mb)+"<br/>"
                            html = html + "md = mdsementara = "+str(md)+"<br/>"
                            html = html + "cf = mb - md = "+str(mb)+" - "+str(md)+" = "+str(cf)+"<br/><br/><br/>"
                            list_daftar_cf.append(cf)
                            #     // cek apakah penyakit ini adalah penyakit dgn CF terbesar ?
                            if ((id_penyakit_terbesar == '') or (cf_terbesar < cf)):
                                cf_terbesar = cf
                                id_penyakit_terbesar = id_penyakit
                                nama_penyakit_terbesar = nama_penyakit

                    i=i+1
    #// urutkan daftar gejala berdasarkan besar CF

    i=0
    #print(datapenyakitterpilih)
    # print(list_daftar_cf)
    for rowpenyakitterpilih in datapenyakitterpilih:
        j=0
        for rowpenyakitterpilih in datapenyakitterpilih:
            if (j>=i):
                if (list_daftar_cf[j] > list_daftar_cf[i]):
                    t = list_daftar_cf[i]
                    list_daftar_cf[i] = list_daftar_cf[j]
                    list_daftar_cf[j] = t

                    tt = list_daftar_penyakit[i]
                    list_daftar_penyakit[i] = list_daftar_penyakit[j]
                    list_daftar_penyakit[j] = tt

                    ttt = list_daftar_id_penyakit[i]
                    list_daftar_id_penyakit[i] = list_daftar_id_penyakit[j]
                    list_daftar_id_penyakit[j] = ttt
            j=j+1
        i=i+1
    # print(list_daftar_cf)
    html = html + "penyakit terbesar = "+str(id_penyakit_terbesar)+"."+nama_penyakit_terbesar+"<br/>"

    return render_template('proses-cf-flask-mysql.html', sql=sql, html=html, list_gejala_terpilih=list_gejala_terpilih, list_daftar_cf=list_daftar_cf, list_daftar_penyakit=list_daftar_penyakit, list_daftar_id_penyakit=list_daftar_id_penyakit)

if __name__ == '__main__':
    app.run()
