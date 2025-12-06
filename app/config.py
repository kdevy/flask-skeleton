import os
from myflaskbase import BaseConfig

class ProjectConfig(BaseConfig):
    if os.getenv("FLASK_ENV", "development") == "production":
        DEBUG = False
        TESTING = False
    else:
        DEBUG = True
        TESTING = True

    BABEL_TRANSLATION_DIRECTORIES = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "translations")