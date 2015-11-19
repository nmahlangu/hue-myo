import requests
import os
import sys
import json
import random
import time
import credentials

# randomly flash colors
creds = credentials.get_credentials()
url = "http://"+creds["ip_addr"]+"/api/"+creds["username"]+"/lights/2/state"
# for i in xrange(1,41):
# 	n = int(random.random() * 60000)
# 	r = requests.put(url,data=json.dumps({"on":True, "sat":254, "bri":254,"hue":n,"transitiontime":0}))
# 	print r.text

# randomly flash colors faster by turning on and off
# last = False
# for i in xrange(1,41):
# 	n = int(random.random() * 60000)
# 	r = requests.put(url,data=json.dumps({"on":last,"sat":254,"bri":254,"hue":n,"transitiontime":0}))
# 	last = not last
# 	print r.text

# r = requests.get(url)
# d = json.loads(r.text)
# print [int(n) for n in d["lights"]]
# print r.text

# print json.loads(requests.get(url).text)["lights"]

# requests.put(url,data=json.dumps({"on":True,"transitiontime":0,"sat":254,"bri":254,"hue":30000}))
# time.sleep(1)
# requests.put(url,data=json.dumps({"on":False,"transitiontime":0}))

