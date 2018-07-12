#!/usr/bin/env python

import json

json_input = (open("./conf/wines_from_api2.json", 'r')).read()

json_data = json.loads(json_input)
print(json_data)
