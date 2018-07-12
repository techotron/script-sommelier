#!/usr/bin/env python

import json
import urllib2

wine_api_host = "https://api.globalwinescore.com/"
#wine_api_host = "http://private-anon-a202a959a8-globalwinescore.apiary-mock.com/"

wine_api_query = "globalwinescores/latest/?color=white&limit=100"
wine_api_url = "%s%s" % (wine_api_host, wine_api_query)
wine_api_key = (open("c:\\temp\\globalwinescoreapikey.txt", 'r')).read()
auth_token = 'Token %s' % wine_api_key

request = urllib2.Request(wine_api_url)
request.add_header("Authorization", 'Token %s' % (wine_api_key))
request.add_header("Accept", "application/json")

response = urllib2.urlopen(request).read()
#
# output = open("./conf/wines_from_api.json", 'w')
# output.write(response)
# output.close()

# with open("./conf/wines_from_api2.json", 'w') as outfile:
#     json.dump(response, outfile)
