from functools import wraps
from flask import request, jsonify

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        if token != 'my-secret-token':
            return jsonify({'message': 'Invalid token'}), 401
        return f(*args, **kwargs)
    return decorated
