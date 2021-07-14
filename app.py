from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///musicas.sqlite3"
db = SQLAlchemy(app)

class Musica(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    artista = db.Column(db.String(150), nullable=False)
    link = db.Column(db.String(300), nullable=False)

    def __init__(self, nome, artista, link):
        self.nome = nome
        self.artista = artista
        self.link = link

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def new():
    return render_template("new.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)