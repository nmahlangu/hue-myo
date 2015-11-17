import json
import time     # debug
import random   # debug
import requests

class LightController:

    def __init__(self,ip_addr,username):
        self.ip_addr  = ip_addr
        self.username = username
        self.url = "http://"+ip_addr+"/api/"+username
        self.lights   = self.get_all_lights()

    def exec_request(self,url,data):
        """
        Execute a request to Philips Hue bridge.

        type url: str
        type data: dict
        """
        return requests.put(url,data=data).status_code == 200

    def get_all_lights(self):
        """
        Get a list of all known lights.
        """
        return [int(n) for n in json.loads(requests.get(self.url+"/groups/0").text)["lights"]]

    def turn_on_light(self,light,transition_time=None):
        """
        Turn on a light.

        type light: int
        type transition_time: int
        """
        if light in self.lights:
            data = json.dumps({"on":True,"transitiontime":0}) if transition_time != None else json.dumps({"on":True})
            return self.exec_request(self.url+"/lights/%s/state"%str(light),data=data)
        return False

    def turn_off_light(self,light,transition_time=None):
        """
        Turn off a light.

        type light: int
        type transition_time: int
        """
        if light in self.lights:
            data = json.dumps({"on":False,"transitiontime":transition_time}) if transition_time != None else json.dumps({"on":False})
            return self.exec_request(self.url+"/lights/%s/state"%str(light),data=data)
        return False

    def turn_on_all_lights(self):
        """
        Turn on all lights.
        """
        retval = True
        for light in self.lights:
            retval = retval and self.turn_on_light(light)
        return retval

    def turn_off_all_lights(self):
        """
        Turn off all lights.
        """
        retval = True
        for light in self.lights:
            retval = retval and self.turn_off_light(light)
        return retval

    def change_brightness(self,light,br,transition_time=None):
        """
        Change the brightness of a light.

        type light: int
        type br: int
        type transition_time: int
        """
        if light in self.lights and 0 < br < 255:
            data = json.dumps({"bri":br,"transitiontime":transition_time}) if transition_time != None else json.dumps({"bri":br})
            return self.exec_request(self.url+"/lights/%s/state"%str(light),data=data)
        return False

    def change_hue(self,light,xy=None,ct=None,hue=None,sat=None,transition_time=None):
        """
        Change the hue (color) of a light.

        type xy: int[]
        type ct: int
        type hue: int
        type sat: int
        type transition_time: int
        """
        if light in self.lights:
            if xy and 0 <= x <= 1 and 0 <= y <= 1:
                data = json.dumps({"xy":xy,"transitiontime":transition_time}) if transition_time != None else json.dumps({"xy":xy})
            elif ct and 153 <= ct <= 500:
                data = json.dumps({"ct":ct,"transitiontime":transition_time}) if transition_time != None else json.dumps({"ct":ct})
            elif hue and 0 <= hue <= 65535 and sat and 0 <= sat <= 254:
                data = json.dumps({"hue":hue,"sat":sat,"transitiontime":transition_time}) if transition_time != None else json.dumps({"hue":hue,"sat":sat})
            if data:
                return self.exec_request(self.url+"/lights/%s/state"%str(light),data)
        return False   
                
    def start_color_loop(self,light):
        """
        Put a light into a color looping mode.

        type light: int
        """
        if light in self.lights:
            data = json.dumps({"effect":"colorloop"})
            return self.exec_request(self.url+"/lights/%s/state"%str(light),data)
        return False

    def end_color_loop(self,light):
        """
        Turn off color looping mode in a light.

        type light: int
        """
        if light in self.lights:
            data = json.dumps({"effect":"none"})
            return self.exec_request(self.url+"/lights/%s/state"%str(light),data)
        return False

    def alert(self,light):
        """
        Make the light do a blink.

        type light: int
        """
        if light in self.lights:
            data = json.dumps({"alert":"select"})
            return self.exec_request(self.url+"/lights/%s/state"%str(light),data)
        return False

if __name__ == "__main__":
    ip_addr = None
    username = None
    lc = LightController(ip_addr,username)

    # lc.turn_off_light(2,0)
    # time.sleep(1)
    # lc.turn_on_light(2,0)

    # lc.turn_off_all_lights()
    # time.sleep(1)
    # lc.turn_on_all_lights()

    # for i in xrange(255):
    #     time.sleep(0.1)
    #     lc.change_brightness(2,i)
    #     print "Brightness: ", i

    # bris = [20, 40, 80, 140, 230, 254]
    # for b in bris:
    #     lc.change_brightness(2,b,0)
    #     time.sleep(1)

    # lc.alert(2)

    # lc.start_color_loop(2)
    # time.sleep(8)
    # lc.end_color_loop(2)

    # for i in xrange(10):
    #     x = random.random() * 0.8
    #     y = random.random() * 0.9
    #     lc.change_hue(2,xy=[x,y],transition_time=0)
    #     time.sleep(1)    

    # for i in xrange(10):
    #     ct = int((random.random() * 347) + 153)
    #     print ct
    #     lc.change_hue(2,ct=ct,transition_time=0)
    #     time.sleep(1)

    # for i in xrange(10):
    #     hue = int(random.random() * 65536)
    #     sat = int(random.random() * 254)
    #     print hue
    #     lc.change_hue(2,hue=hue,sat=sat,transition_time=0)
    #     time.sleep(1)
