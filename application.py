from flask import Flask
from waitress import serve

application = Flask(__name__)


@application.route('/')
def hello_world():
    return 'Maximiza Tecnologia: online Inteligence'

if __name__ == '__main__':
    serve(application, host='0.0.0.0', port=5000)  # WSGI serverpy

