from flask import Blueprint

web_bp = Blueprint('web_bp', __name__)

@web_bp.route('/')
@web_bp.route('/home')
def home():
	return "<h1 style='color:blue'>Hello World!</h1>"
