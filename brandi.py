import os, sys

proj_path = "/Users/dbhattachar/Desktop/test/src"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clearance.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


from products.models import Product, Brand

def populate():

	add_brand(title='ABC', url="www.google.com")
	add_brand(title='DEF', url = "yahoo.com")
	add_brand(title='GHI', url= "www.msn.com")


def add_brand(title, url):
	p = Brand.objects.get_or_create(title=title)[0]
	p.url = url
	p.save()
	return p   

populate()

# if __name__ == '_main_':
# 	populate()








