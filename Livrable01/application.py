# -*- coding: utf-8 -*-
from flask import Flask
from Database.MongoDB import Connect



def create_app():
    app = Flask(__name__)
    # import blueprints
    from Database.Batiment.views import batiments_app
    from Database.Salle.views import salle_app
    from Database.Presentation.views import presentation_app
    from Database.Horaire.views import horaire_app
    from Database.User.views import user_app

    # register blueprints
    app.register_blueprint(batiments_app)
    app.register_blueprint(salle_app)
    app.register_blueprint(presentation_app)
    app.register_blueprint(horaire_app)
    app.register_blueprint(user_app)

    return app