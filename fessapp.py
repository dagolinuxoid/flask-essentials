from flask import Flask, render_template, url_for, redirect, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    with sql.connect('herodata.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM hero_dashboard')
        heroes = cur.fetchall()
    return render_template('index.html', heroes=heroes)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    # if request.method == 'POST':
    if request.form.get('hero_name') !='' and request.form.get('hero_descr') !='':
        with sql.connect('herodata.db') as conn:
            cur = conn.cursor()
            # add hero's info into a database
            cur.execute('INSERT INTO hero_dashboard (hero_name, hero_descr) VALUES(?,?)',
                        (request.form['hero_name'], request.form.get('hero_descr')))
            conn.commit()
        return 'So hero — {} and description — {}|was added to db'.format(request.form['hero_name'], request.form.get('hero_descr'))

@app.route('/unregister', methods=['GET', 'POST'])
def unregister():
    if request.method == 'GET':
        # don't do this :)
        conn = sql.connect('herodata.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM hero_dashboard')
        heroes = cur.fetchall()
        conn.close()
        return render_template('unregister.html', heroes = heroes)
    if request.form.get('id'):
        with sql.connect('herodata.db') as conn:
            cur = conn.cursor()
            cur.execute('DELETE FROM hero_dashboard WHERE id=?', (request.form.get('id')))
            conn.commit()
        return 'Something has been deleted'

@app.route('/hm')
def hm():
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)