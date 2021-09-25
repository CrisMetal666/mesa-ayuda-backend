from datetime import timedelta

from .predeterminado import APP_ENV_LOCAL

APP_ENV = APP_ENV_LOCAL
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Cris232322@localhost:3306/mesa_ayuda'
JWT_SECRET_KEY = 'super-secret-key'
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
