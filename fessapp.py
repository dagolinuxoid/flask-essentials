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
def index(heroes):
    return render_template('index.html', heroes=heores)

if __name__=='__main__':
    app.run(debug=True)