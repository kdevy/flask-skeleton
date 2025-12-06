# Flask
This is a skeleton project for Flask.

## Installation

1. Download the code from GitHub:<br>
```bash
cd /var/www/
mkdir flask
git clone git@github.com:kdevy/flask-skeleton.git
```

2. Set up a Python virtual environment:<br>
```bash
python -m venv venv
source venv/bin/activate
```

3. Install pip packages:<br>
```bash
pip install -r requirements.txt
```

4. Generate a SECRET_KEY.<br>
Paste the generated string into `app/__init__.py` as `app.secret_key`.
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

5. Set up the database.<br>
After creating a MySQL database, update the credentials in the `.env` file.

6. Install tailwindcss
```bash
npm install tailwindcss @tailwindcss/cli
npx @tailwindcss/cli -i app/static/css/tailwindcss/source.css -o app/static/css/tailwindcss/dest.css --watch
```

7. Start the development server:<br>
```bash
python run.py
```

# Commands
## babel
```
$ pybabel extract -F babel.cfg -o translations/messages.pot . -k lazy_gettext
```

```
$ pybabel init -i translations/messages.pot -d translations -l en
$ pybabel init -i translations/messages.pot -d translations -l ja
```

```
$ pybabel compile -d translations -l en -f
$ pybabel compile -d translations -l ja -f
```