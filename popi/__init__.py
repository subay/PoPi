from flask import Flask

app = Flask(__name__)
app.config.update(
    DATABASE_URI = 'sqlite:///./popi.db',
    SECRET_KEY = 'development key'
)
app.debug = True

from popi import views