import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

DB_PATH = os.path.join(ROOT_DIR, 'db.sqlite3')
DB_CONNECTION_STRING = 'sqlite:///{0}'.format(DB_PATH)
