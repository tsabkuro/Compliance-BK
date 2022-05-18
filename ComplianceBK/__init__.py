from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '5091628bb0b13ce0c671dfde280ha148'

from ComplianceBK import routes