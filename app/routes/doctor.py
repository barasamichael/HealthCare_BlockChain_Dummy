from flask import Blueprint

doctor_bp = Blueprint('doctor', __name__)

@doctor_bp.route('/doctor', methods=['GET'])
def get_doctor():
    # code to retrieve a doctor
    return 'This route will retrieve a doctor'

@doctor_bp.route('/doctor', methods=['POST'])
def add_doctor():
    # code to add a new doctor
    return 'This route will add a new doctor'