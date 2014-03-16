from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.config.update(
    DATABASE_URI = 'sqlite:///./popi.db',
    SECRET_KEY = 'development key'
)
app.debug = True
app.wsgi_app = ProxyFix(app.wsgi_app)

from popi import views