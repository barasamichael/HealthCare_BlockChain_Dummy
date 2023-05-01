from flask import Blueprint, request, jsonify
from app.blockchain.blockchain import Blockchain
from app.models.doctor import Doctor

doctor_bp = Blueprint('doctor_bp', __name__)

# instantiate blockchain
blockchain = Blockchain()

@doctor_bp.route('/doctors', methods=['GET'])
def get_doctors():
    # retrieve doctors from blockchain
    doctors = blockchain.get_doctors()
    return jsonify({'doctors': doctors})

@doctor_bp.route('/hospitals', methods=['GET'])
def get_hospitals():
    # retrieve hospitals from blockchain
    hospitals = blockchain.get_hospitals()
    return jsonify({'hospitals': hospitals})

@doctor_bp.route('/add_doctor', methods=['POST'])
def add_doctor():
    # retrieve data from request
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    hospital_id = data.get('hospital_id')

    # create new doctor object
    doctor = Doctor(name=name, email=email, hospital_id=hospital_id)

    # add doctor to blockchain
    success = blockchain.add_doctor(doctor)

    if success:
        return jsonify({'message': 'Doctor added successfully'})
    else:
        return jsonify({'message': 'Error adding doctor'}), 400