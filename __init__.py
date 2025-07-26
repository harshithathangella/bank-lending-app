from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    from .routes import lend_bp, payment_bp, ledger_bp, overview_bp

    app = Flask(__name__)
    app.config.from_object("config.Config")
    db.init_app(app)

    app.register_blueprint(lend_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(ledger_bp)
    app.register_blueprint(overview_bp)

    return app
