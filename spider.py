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
	try:
		Product.objects.get_or_create(title=i['title'], price=i['price'], clearance=i['clearance'], image=i['image'], product_url=i['title_link'], brand='Cleo', brand_url='http://www.cleo.ca/sale/shop-clearance/')
	except Exception:
		pass

url1 = "https://api.import.io/store/data/daeda5d9-f967-4b16-9036-f28d241efdcb/_query?input/webpage/url=http%3A%2F%2Fwww.stevemadden.com%2Fthumbnail%2FCLEARANCE%2FWomens-Clearance%2Fpc%2F-1%2Fc%2F3259%2F2180.uts&_user=3acaed4f-638f-44dc-b772-f47bea053ec6&_apikey=3acaed4f-638f-44dc-b772-f47bea053ec6%3AcRLi6pX7n7Ij0JoqRtRMI3Syy3cI7JhRkwuFGEe0Df2pW4m4AAL%2FxO8P9oCopFP0O3AaQ%2BNsaBpWlgcJOIctLw%3D%3D"
obj1 = urllib2.urlopen(url1)
data1 = json.load(obj1)
for a in data1['results']:
	try:
	    Product.objects.get_or_create(title=a['title'], price=a['price'], clearance=a['clearance'], image=a['image'], product_url=a['title_link'], brand='STEVEMADDEN', brand_url='http://www.bcbg.com/on/demandware.store/Sites-BCBG-Site/en_CA/Search-Show?cgid=sale#sz=264')
	except Exception:
		pass

url2 = "https://api.import.io/store/data/889a8593-296d-4864-8e8b-d7983bc24bc0/_query?input/webpage/url=http%3A%2F%2Fwww.bcbg.com%2Fon%2Fdemandware.store%2FSites-BCBG-Site%2Fen_CA%2FSearch-Show%3Fcgid%3Dsale%23sz%3D621&_user=3acaed4f-638f-44dc-b772-f47bea053ec6&_apikey=3acaed4f-638f-44dc-b772-f47bea053ec6%3AcRLi6pX7n7Ij0JoqRtRMI3Syy3cI7JhRkwuFGEe0Df2pW4m4AAL%2FxO8P9oCopFP0O3AaQ%2BNsaBpWlgcJOIctLw%3D%3D"
obj2 = urllib2.urlopen(url2)
data2 = json.load(obj2)
for b in data2['results']:
	try:
		Product.objects.get_or_create(title=b['title'], price=b['price'], clearance=b['clearance'], image=b['image'], product_url=b['title_link'], brand='BCBG', brand_url='http://www.bcbg.com/on/demandware.store/Sites-BCBG-Site/en_CA/Search-Show?cgid=sale#sz=264')
	except Exception:
		pass

url3 = "https://api.import.io/store/data/045c5a71-7aba-4039-a100-9d757cc6e273/_query?input/webpage/url=http%3A%2F%2Fwww.northernreflections.com%2Fsale%2F&_user=3acaed4f-638f-44dc-b772-f47bea053ec6&_apikey=3acaed4f-638f-44dc-b772-f47bea053ec6%3AcRLi6pX7n7Ij0JoqRtRMI3Syy3cI7JhRkwuFGEe0Df2pW4m4AAL%2FxO8P9oCopFP0O3AaQ%2BNsaBpWlgcJOIctLw%3D%3D"
obj3 = urllib2.urlopen(url3)
data3 = json.load(obj3)
for c in data3['results']:
	try:
		Product.objects.get_or_create(title=c['title'], price=c['price'], clearance=c['clearance'], image=c['image'], product_url=c['title_link'], brand='Northern Reflections', brand_url='http://www.northernreflections.com/sale/')
	except Exception:
		pass

url4 = "https://api.import.io/store/data/5aada532-8452-42f9-ad3d-c503e2468854/_query?input/webpage/url=http%3A%2F%2Fwww.rickis.com%2Fsale%2Fclearance%2F&_user=3acaed4f-638f-44dc-b772-f47bea053ec6&_apikey=3acaed4f-638f-44dc-b772-f47bea053ec6%3AcRLi6pX7n7Ij0JoqRtRMI3Syy3cI7JhRkwuFGEe0Df2pW4m4AAL%2FxO8P9oCopFP0O3AaQ%2BNsaBpWlgcJOIctLw%3D%3D"
obj4 = urllib2.urlopen(url4)
data4 = json.load(obj4)
for d in data4['results']:
	try:
		Product.objects.get_or_create(title=d['title'], price=d['price'], clearance=d['clearance'], image=d['image'], product_url=d['title_link'], brand='Rickis',brand_url='http://www.rickis.com/sale/clearance/')
	except Exception:
		pass

