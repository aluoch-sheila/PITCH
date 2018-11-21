import os

class Config:
   SECRET_KEY = os.environ.get('SECRET_KEY')
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:6782@localhost/pitch'
   UPLOADED_PHOTOS_DEST = 'app/static/photos'
   MAIL_SERVER = 'smtp.gmail.com'
# email configuration
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
   MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

   # simple mde configurations
   SIMPLEMDE_JS_IIFE = True
   SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
   SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

   @staticmethod
   def init_app(app):
       pass




class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:6782@localhost/pitch'

class DevConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:6782@localhost/pitch'
   DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}