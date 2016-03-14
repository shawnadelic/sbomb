from base import *
from utils import get_env_variable

DEBUG=False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
	'USER': 'django',
        'PASSWORD': get_env_variable("SBOMB_PROD_PASSWORD"),
	'HOST': 'localhost',
	'PORT': '',
    }
}
