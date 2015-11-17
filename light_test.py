import requests
import os
import sys
import json
import random

url = "http://192.168.2.3/api/39e3442017e1190f35cb8070213e28ff/lights/2/state"
for i in xrange(1,41):
	n = int(random.random() * 60000)
	r = requests.put(url,data=json.dumps({"on":True, "sat":254, "bri":254,"hue":n}))
	print r.text