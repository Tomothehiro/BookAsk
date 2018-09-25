"""
Django settings for bookask project.

Keep all sensitive information here
"""

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '####################'

# SMTP server
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.###'
EMAIL_PORT = 587
EMAIL_HOST_USER = '###@####'
EMAIL_HOST_PASSWORD = '####'
DEFAULT_FROM_EMAIL = 'BookQ Password Reset <###@###>'

DATABASES = {
    'default': {
        'ENGINE': '####',
        'NAME': '###',
        'USER': '###',
        'PASSWORD': '####',
        'HOST': 'elmer.db.elephantsql.com',
        'PORT': '5432',
    }
}
