from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    email = db.Column(db.String(120))
    turma = db.Column(db.String(50))
    matricula = db.Column(db.String(50))