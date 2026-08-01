import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/task_tracker'

    # On Google App Engine we always read the URI from the environment
    if os.environ.get('GAE_ENV', '').startswith('standard'):
        MONGO_URI = os.environ.get('MONGO_URI')
