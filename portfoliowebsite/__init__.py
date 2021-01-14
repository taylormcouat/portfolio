from flask import Flask
from portfoliowebsite.config import Config
from flask_mail import Mail

mail = Mail()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	mail.init_app(app)

	from portfoliowebsite.main.routes import main
	app.register_blueprint(main)

	return app