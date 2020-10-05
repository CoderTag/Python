import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
b = 'sqlite:///' + os.path.join(basedir, 'app.db')
print(b)

# SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#     'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLALCHEMY_TRACK_MODIFICATIONS = False
