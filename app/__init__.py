from flask import Flask
from app.web.routes import web_bp

def create_app():
	app = Flask(__name__)

	app.url_map.strict_slashes = False

	app.register_blueprint(web_bp)

	return app
