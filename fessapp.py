from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

heroes = [
    {'name':'juggernaut', 'description':'agility'},
    {'name':'mortred', 'description':'agility'},
    {'name':'skeleton king', 'description': 'strength'},
    {'name':'maigna', 'description':'agility'},
    {'name':'faceless void', 'description':'agility'}
]

@app.route('/')
def index():
    return render_template('index.html', heroes=heroes)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/unregister', methods=['GET', 'POST'])
def unregister():
    return render_template('unregister.html')

@app.route('/hm')
def hm():
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)