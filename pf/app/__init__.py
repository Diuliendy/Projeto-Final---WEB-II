from flask import Flask
from app.models.alunos import db

def create_app():
     

    app = Flask(__name__,
                static_folder='static',
                template_folder='templates')
    


    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///alunos.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "troque-esta-chave"

    db.init_app(app)

    
    from app.controllers.views import bp
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app
