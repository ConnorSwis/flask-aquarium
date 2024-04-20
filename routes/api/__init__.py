from flask import jsonify, Blueprint
from models import Aquarium
import threading

api = Blueprint('api', __name__)

aquarium = Aquarium()

@api.route('/status', methods=['GET'])
def get_status():
    response = jsonify(aquarium.status())
    response.headers.add('Cache-Control', 'no-cache, no-store, must-revalidate')
    response.headers.add('Pragma', 'no-cache')
    response.headers.add('Expires', '0')
    return response

def init():
    updater_thread = threading.Thread(target=aquarium.update, daemon=True)
    updater_thread.start()
    return api