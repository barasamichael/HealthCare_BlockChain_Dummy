from flask import Blueprint

hospital_bp = Blueprint('hospital', __name__)

@hospital_bp.route('/hospital', methods=['GET'])
def get_hospital():
    # code to retrieve a hospital
    return 'This route will retrieve a hospital'

@hospital_bp.route('/hospital', methods=['POST'])
def add_hospital():
    # code to add a new hospital
    return 'This route will add a new hospital'