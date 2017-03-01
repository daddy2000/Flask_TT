from werkzeug.wsgi import SharedDataMiddleware
from first_app_ext import db, mako
from first_app_utils import get_file_path
from flask import Flask

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object('config')
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {'i': get_file_path()})

mako.init_app(app)
db.init_app(app)
