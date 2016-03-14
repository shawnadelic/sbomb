"""
WSGI config for sbomb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from sbomb.settings.utils import get_env_variable
from django.core.wsgi import get_wsgi_application

SETTINGS_MODULE = get_env_variable("SBOMB_SETTINGS_MODULE")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)

application = get_wsgi_application()
