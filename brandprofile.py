import os, sys

proj_path = "/Users/Deepak/Desktop/clearance/src"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clearance.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from products.models import Brand


brands = Brand.objects.all()
for brand in brands:
	Brand.objects.create(title='Cleo', url='www.cleo.com', description='Hello World')

