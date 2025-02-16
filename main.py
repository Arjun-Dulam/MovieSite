import os
from django.core.wsgi import get_wsgi_application

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

# Create the WSGI application
application = get_wsgi_application()
