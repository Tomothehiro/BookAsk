BookAsk (BookQ)
===================

### [Demo](https://bookq.tomohiro-sato.com)

Simple Python application using Django and PostgreSQL.

Installing and Running
----

Clone GitHub repo:

```
git clone https://github.com/Tomothehiro/BookAsk.git
```

Create and activate virtualenv environment in cloned directory

```
virtualenv env --no-site-packages

source env/bin/activate
```

Install required libraries

```
pip install -r requirements.txt 
```

Update /bookask/settings_secret.py<br>
Obtain a secret from [MiniWebTool](https://www.miniwebtool.com/django-secret-key-generator/) and update SECRET_KEY.<br>
Create a PostgreSQL DB and add the credentials.<br>

Migrate and create admin account
```
python manage.py migrate
python manage.py createsuperuser
```

Start the server
```
python manage.py runserver
```

Go to [http://localhost:8000](http://localhost:8000) in your browser.

Resources
----
- [Django](https://www.djangoproject.com/)
