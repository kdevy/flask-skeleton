# GitHub Copilot Instructions for Flask Skeleton Project

## Project Architecture

This workspace contains two Flask projects:
- **myflaskbase**: A reusable Flask base package providing common extensions, configs, and initialization
- **flask-skeleton**: A concrete application built on top of myflaskbase

### Key Architectural Patterns

**Modular Structure**:
- Use blueprints for feature organization (e.g., `app/user/` for user management)
- Separate concerns: models, forms, services, views, templates
- Service layer handles business logic (see `app/user/services.py`)

**Internationalization**:
- Default locale: Japanese (`ja`)
- Use `flask_babel.lazy_gettext()` for translatable strings in forms and messages
- Translation files in `translations/` directory

**Authentication**:
- Flask-Login with UserMixin models
- Password hashing via Werkzeug
- Login-required views use `@login_required` decorator

## Development Workflow

### Setup
```bash
# For flask-skeleton
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Generate SECRET_KEY and set in .env
python -c "import secrets; print(secrets.token_hex(32))"
# Setup MySQL database credentials in .env
npm install tailwindcss @tailwindcss/cli
npx @tailwindcss/cli -i app/static/css/tailwindcss/source.css -o app/static/css/tailwindcss/dest.css --watch
python run.py
```

### Testing
- Use pytest with fixtures (`tests/conftest.py`)
- Test database: In-memory SQLite for isolation
- Run tests: `pytest`

### Building myflaskbase
```bash
# From myflaskbase directory
pip install -e .
pip install .[dev]  # for pytest
pytest
```

## Coding Conventions

### Views
- Use `MethodView` for REST-like endpoints
- Handle both GET (render template) and POST (process form/return JSON)
- Return JSON responses for API calls, even on errors (status 200 with error field)

### Forms
- Flask-WTF with validators
- Use `lazy_gettext` for labels and error messages
- Example: `StringField(lazy_gettext('Username'), validators=[DataRequired(message=lazy_gettext("ユーザ名を入力してください"))])`

### Models
- SQLAlchemy with PyMySQL for MySQL
- User model extends UserMixin for Flask-Login
- Password hashing: `generate_password_hash()` and `check_password_hash()`

### Templates
- Jinja2 with TailwindCSS
- Base templates in `templates/` with `_base.html` pattern
- Static files served from `app/static/`

### Configuration
- Environment variables via python-dotenv
- Config classes inheriting from BaseConfig
- Database URI: `mysql+pymysql://{user}:{password}@{host}/{dbName}?charset=utf8`

## Key Files to Reference

- `myflaskbase/myflaskbase/__init__.py`: Package exports
- `flask-skeleton/app/__init__.py`: App factory pattern
- `flask-skeleton/app/user/services.py`: Business logic example
- `flask-skeleton/app/user/views/login_view.py`: MethodView pattern
- `tests/conftest.py`: Test fixtures setup</content>
<parameter name="filePath">/var/www/flask-skeleton/.github/copilot-instructions.md