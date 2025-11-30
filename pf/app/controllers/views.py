from flask import Blueprint, render_template, request, redirect, url_for
from app.models.alunos import db, Aluno

bp = Blueprint("views", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/alunos")
def listar():
    alunos = Aluno.query.all()
    return render_template("listar.html", alunos=alunos)

@bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        matricula = request.form.get("matricula")
        existe = Aluno.query.filter_by(matricula=matricula).first()
        if existe:
            return render_template("cadastro.html", erro="Essa matrícula já existe!")

        
        aluno = Aluno(
            nome=request.form.get("nome"),
            idade=request.form.get("idade") or None,
            email=request.form.get("email"),
            turma=request.form.get("turma"),
            matricula=matricula
        )
        db.session.add(aluno)
        db.session.commit()
        return redirect(url_for("views.listar"))

    return render_template("cadastro.html")

@bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    aluno = Aluno.query.get_or_404(id)

    if request.method == "POST":
        nova_matricula = request.form.get("matricula")

        
        existe = Aluno.query.filter(
            Aluno.matricula == nova_matricula,
            Aluno.id != id
        ).first()

        if existe:
           return render_template("editar.html", aluno=aluno, erro="Essa matrícula já existe!")

        aluno.nome = request.form.get("nome")
        aluno.idade = request.form.get("idade") or None
        aluno.email = request.form.get("email")
        aluno.turma = request.form.get("turma")
        aluno.matricula = nova_matricula
        
        db.session.commit()
        return redirect(url_for("views.listar"))

    return render_template("editar.html", aluno=aluno)

@bp.route("/deletar/<int:id>")
def deletar(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for("views.listar")) 
