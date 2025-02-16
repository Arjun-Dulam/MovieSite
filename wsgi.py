import os
from django.core.wsgi import get_wsgi_application

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MovieSite.settings')

# Create the WSGI application
application = get_wsgi_application()

if __name__ == "__main__":
    from gunicorn.app.wsgiapp import run
    run()
