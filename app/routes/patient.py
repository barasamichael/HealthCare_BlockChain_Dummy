from flask import Blueprint

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/patient', methods=['GET'])
def get_patient():
    # code to retrieve a patient
    return 'This route will retrieve a patient'

@patient_bp.route('/patient', methods=['POST'])
def add_patient():
    # code to add a new patient
    return 'This route will add a new patient'