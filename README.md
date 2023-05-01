# Health Application on Blockchain using Flask
## Introduction
This is a health application built on blockchain technology using the Flask web 
framework. The application allows users to securely store and manage their 
medical data using a decentralized system that ensures data privacy and security.

## File Structure
```md
health_app/
├── app/
│   ├── __init__.py
│   ├── blockchain/
│   │   ├── __init__.py
│   │   ├── block.py
│   │   ├── blockchain.py
│   │   └── transaction.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── hospital.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── patient.py
│   │   ├── doctor.py
│   │   └── hospital.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── patient.html
│   │   ├── doctor.html
│   │   └── hospital.html
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   └── utils/
│       ├── __init__.py
│       ├── auth.py
│       └── validation.py
├── requirements.txt
├── config.py
├── run.py
└── README.md
```

The `health_app/ directory` is the main directory of our application. It contains 
an `app/ directory`, which contains the main code for our Flask application.

The `app/ directory` contains the following subdirectories:

1. `blockchain/`: This directory contains the code for our blockchain 
implementation, including the `block.py`, `blockchain.py`, and `transaction.py` 
modules.

2. `models/`: This directory contains the code for our data models, including 
the `patient.py`, `doctor.py`, and `hospital.py` modules.

3. `routes/`: This directory contains the code for our Flask routes, including 
the `patient.py`, `doctor.py`, and `hospital.py` modules.

4. `templates/`: This directory contains the HTML templates for our application, 
including `base.html`, `index.html`, `patient.html`, `doctor.html`, and 
`hospital.html`.

5. `static/`: This directory contains static files for our application, including 
CSS, JavaScript, and image files.

6. `utils/`: This directory contains utility functions used in our application, 
including `auth.py` and `validation.py`.

The `requirements.txt` file lists the Python packages required to run our 
application.

The `config.py` file contains configuration settings for our application.

The `run.py` file is the entry point for our application.

The `README.md` file contains documentation for our application.

## Installation
1. Clone the repository:
```sh
git clone https://github.com/username/health_app.git
```

2. Install the required packages:
```sh
pip install -r requirements.txt
```

3. Set the Flask app environment variable:
```sh
export FLASK_APP=run.py
```

4. Run the app:
```sh
flask run
```

## Usage
The app has three main functionalities for different types of users: **patients**, 
**doctors**, and **hospitals**. Each user can create an account, log in, and access
 their own medical data. Patients can view and update their medical records, 
doctors can view and update patient records that they are authorized to access, 
and hospitals can manage their patient records.

## Contributing
If you would like to contribute to this project, please open an issue or submit a 
pull request. All contributions are welcome!

## Authors
1. Barasa Michael Murunga michael.barasa@strathmore.edu
