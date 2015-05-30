import os, sys

# proj_path = "/Users/Deepak/Desktop/clearance/src"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clearance.settings")
# sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
# os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()




import json
import urllib2
from products.models import Product


url = "https://api.import.io/store/data/2a2f0b4f-6f38-4b88-a23e-c3e70876b107/_query?input/webpage/url=http%3A%2F%2Fwww.cleo.ca%2Fsale%2Fshop-clearance%2F&_user=3acaed4f-638f-44dc-b772-f47bea053ec6&_apikey=3acaed4f-638f-44dc-b772-f47bea053ec6%3AcRLi6pX7n7Ij0JoqRtRMI3Syy3cI7JhRkwuFGEe0Df2pW4m4AAL%2FxO8P9oCopFP0O3AaQ%2BNsaBpWlgcJOIctLw%3D%3D"
obj = urllib2.urlopen(url)
data = json.load(obj)
for i in data['results']:
	Product.objects.get_or_create(title=i['title'], price=i['price'], clearance=i['clearance'], image=i['image'], product_url=i['title_link'], brand='Cleo', brand_url='http://www.cleo.ca/sale/shop-clearance/')


import os, sys

# proj_path = "/Users/Deepak/Desktop/clearance/src"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clearance.settings")
# sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
# os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()




import json
import urllib2
from products.models import Product


url = "https://api.import.io/store/data/2a2f0b4f-6f38-4b88-a23e-c3e70876b107/_query?input/webpage/url=http%3A%2F%2Fwww.cleo.ca%2Fsale%2Fshop-clearance%2F&_user=3acaed4f-638f-44dc-b772-f47bea053ec6&_apikey=3acaed4f-638f-44dc-b772-f47bea053ec6%3AcRLi6pX7n7Ij0JoqRtRMI3Syy3cI7JhRkwuFGEe0Df2pW4m4AAL%2FxO8P9oCopFP0O3AaQ%2BNsaBpWlgcJOIctLw%3D%3D"
obj = urllib2.urlopen(url)
data = json.load(obj)
for i in data['results']:
	Product.objects.get_or_create(title=i['title'], price=i['price'], clearance=i['clearance'], image=i['image'], product_url=i['title_link'], brand='Cleo', brand_url='http://www.cleo.ca/sale/shop-clearance/')


# url1 = "https://api.import.io/store/data/9bf2f4af-7fa4-4e2c-8d6f-cc52f6306180/_query?input/webpage/url=http%3A%2F%2Fwww.bcbg.com%2Fon%2Fdemandware.store%2FSites-BCBG-Site%2Fen_CA%2FSearch-Show%3Fcgid%3Dsale%23sz%3D264&_user=3acaed4f-638f-44dc-b772-f47bea053ec6&_apikey=3acaed4f-638f-44dc-b772-f47bea053ec6%3AcRLi6pX7n7Ij0JoqRtRMI3Syy3cI7JhRkwuFGEe0Df2pW4m4AAL%2FxO8P9oCopFP0O3AaQ%2BNsaBpWlgcJOIctLw%3D%3D"
# obj1 = urllib2.urlopen(url1)
# data1 = json.load(obj1)
# for a in data1['results']:
# 	Product.objects.get_or_create(title=a['title'], price=a['price'], clearance=a['clearance'], image=a['image'], product_url=a['title_link'], brand='BCBG', brand_url='http://www.bcbg.com/on/demandware.store/Sites-BCBG-Site/en_CA/Search-Show?cgid=sale#sz=264')