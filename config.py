import os

DB_URL = 'postgres://postgres:123456@127.0.0.1:5432/gpgp'


ROOT = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(ROOT, 'static/upload')
