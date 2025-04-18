from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Tu peux ajouter une clé secrète si besoin de sessions
    app.config.from_object('app.config.Config')

    from app.routes import sms_bp
    app.register_blueprint(sms_bp)

    return app
