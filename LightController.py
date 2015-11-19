import json
import requests
import credentials

class LightController:

    def __init__(self,ip_addr,username):
        """
        Create a class instance. The IP address of a Philips Hue bridge and the
        username of an authorized user are required.
        See http://www.developers.meethue.com/documentation/getting-started for
        where to find these credentials.

        type ip_addr: str
        type username: str
        """
        self.ip_addr  = ip_addr
        self.username = username
        self.url      = "http://"+ip_addr+"/api/"+username
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
            return self.exec_request(self.url+"/lights/"+str(light)+"/state",data=data)
        return False

    def turn_off_light(self,light,transition_time=None):
        """
        Turn off a light.

        type light: int
        type transition_time: int
        """
        if light in self.lights:
            data = json.dumps({"on":False,"transitiontime":transition_time}) if transition_time != None else json.dumps({"on":False})
            return self.exec_request(self.url+"/lights/"+str(light)+"/state",data=data)
        return False

    def turn_on_all_lights(self,transition_time=None):
        """
        Turn on all lights.
        """
        retval = True
        for light in self.lights:
            tmp = retval and self.turn_on_light(light,transition_time) if transition_time != None else self.turn_on_light(light)
        return retval

    def turn_off_all_lights(self,transition_time=None):
        """
        Turn off all lights.
        """
        retval = True
        for light in self.lights:
            tmp = retval and self.turn_off_light(light,transition_time) if transition_time != None else self.turn_off_light(light)
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
            return self.exec_request(self.url+"/lights/"+str(light)+"/state",data=data)
        return False

    def change_hue(self,light,xy=None,ct=None,hue=None,sat=None,transition_time=None):
        """
        Change the hue (color) of a light. xy takes presidence over ct, which takes
        presidence over hue.

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
                return self.exec_request(self.url+"/lights/"+str(light)+"/state",data)
        return False   
                
    def start_color_loop(self,light):
        """
        Put a light into a color looping mode.

        type light: int
        """
        if light in self.lights:
            data = json.dumps({"effect":"colorloop"})
            return self.exec_request(self.url+"/lights/"+str(light)+"/state",data)
        return False

    def end_color_loop(self,light):
        """
        Turn off color looping mode for a light.

        type light: int
        """
        if light in self.lights:
            data = json.dumps({"effect":"none"})
            return self.exec_request(self.url+"/lights/"+str(light)+"/state",data)
        return False

    def alert(self,light):
        """
        Make a light blink.

        type light: int
        """
        if light in self.lights:
            data = json.dumps({"alert":"select"})
            return self.exec_request(self.url+"/lights/"+str(light)+"/state",data)
        return False