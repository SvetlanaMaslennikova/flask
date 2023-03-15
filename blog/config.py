import os

from dotenv import load_dotenv

from blog.enums import EnvType

load_dotenv()

ENV = os.getenv('FLASK_ENV', default=EnvType.production)
DEBUG = ENV == EnvType.development

SECRET_KEY = 'p&fr)$h-eykgsm)ruz)d(ez2zx3$a4+$h+rg^#9p#tf5(#+zb)'

SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
