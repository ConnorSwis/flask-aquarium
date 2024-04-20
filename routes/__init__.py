from flask import Flask, send_from_directory, Blueprint, render_template
from routes.api import init as api
import os

root = Blueprint('root', __name__)

@root.route('/')
def home():
    return render_template('index.html')

@root.route('/static/js/<path:filename>')
def custom_static(filename):
    return send_from_directory('static/js', filename, mimetype='application/javascript')

@root.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(root.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon')


def init_app(app: Flask):
    app.register_blueprint(api(), url_prefix='/api')
    app.register_blueprint(root)
    