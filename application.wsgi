# my_app.wsgi
import sys
import os

# Add the Flask application path to the system path
sys.path.insert(0, '.')

# Set the FLASK_APP environment variable
os.environ['FLASK_APP'] = 'your_app_name'
# Import the Flask application
from flask import Flask
application = Flask(__name__)
