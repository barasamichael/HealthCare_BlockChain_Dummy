from .patient import patient_bp
from .doctor import doctor_bp
from .hospital import hospital_bp

def init_app(app):
    app.register_blueprint(patient_bp)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(hospital_bp)