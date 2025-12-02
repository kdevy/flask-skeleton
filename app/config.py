import os
from myflaskbase import BaseConfig

class ProjectConfig(BaseConfig):
    if os.getenv("FLASK_ENV", "development") == "production":
        DEBUG = False
        TESTING = False
    else:
        DEBUG = True
        TESTING = True