from flask import Blueprint, request, jsonify
from app.blockchain.blockchain import Blockchain
from app.models.hospital import Hospital

hospital_bp = Blueprint('hospital_bp', __name__)

# instantiate blockchain
blockchain = Blockchain()

@hospital_bp.route('/hospitals', methods=['GET'])
def get_hospitals():
    # retrieve hospitals from blockchain
    hospitals = blockchain.get_hospitals()
    return jsonify({'hospitals': hospitals})

@hospital_bp.route('/add_hospital', methods=['POST'])
def add_hospital():
    # retrieve data from request
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    address = data.get('address')

    # create new hospital object
    hospital = Hospital(name=name, email=email, address=address)

    # add hospital to blockchain
    success = blockchain.add_hospital(hospital)

    if success:
        return jsonify({'message': 'Hospital added successfully'})
    else:
        return jsonify({'message': 'Error adding hospital'}), 400