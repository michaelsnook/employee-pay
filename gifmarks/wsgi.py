"""
WSGI config for gifmarks project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gifmarks.settings")

from django.core.wsgi import get_wsgi_application
#   Cling makes static files work on Heroku
#

from dj_static import Cling
application = Cling(get_wsgi_application())

#   otherwise comment the above 2 lines out and use this instead
#   application = get_wsgi_application()
