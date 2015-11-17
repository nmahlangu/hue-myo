import requests
import os
import sys
import json
import random
import time

# randomly flash colors
url = "http://192.168.2.2/api/39e3442017e1190f35cb8070213e28ff/lights/2/state"
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

# url = "http://192.168.2.3/api/39e3442017e1190f35cb8070213e28ff/groups/0"
# r = requests.get(url)
# d = json.loads(r.text)
# print [int(n) for n in d["lights"]]
# print r.text

# print json.loads(requests.get(url).text)["lights"]

requests.put(url,data=json.dumps({"on":True,"transitiontime":0,"sat":254,"bri":254,"hue":30000}))
time.sleep(1)
requests.put(url,data=json.dumps({"on":False,"transitiontime":0}))