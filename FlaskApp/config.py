import os


class Config(object):
    GREETING = 'Welcome to the lunch club!'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-key-for-devs'
