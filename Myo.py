import myo as libmyo; libmyo.init('/Users/Nicholas/Documents/cs/git/hue-myo/sdk/myo.framework')
import time
import sys
import credentials
import LightController

class Listener(libmyo.DeviceListener):

    def __init__(self):
        # myo
        super(Listener, self).__init__()
        self.orientation = None 
        self.pose = libmyo.Pose.rest
        self.locked = False
        # hue lights
        creds = credentials.get_credentials()
        self.lc = LightController.LightController(creds["ip_addr"],creds["username"])
        self.lc.reset_lights_to_white()

    def on_connect(self,myo,timestamp,firmware_version):
        """
        Is called when the Myo arm band is connected via Bluetooth.
        """
        myo.vibrate('short')
        time.sleep(1)

    def on_pose(self,myo,timestamp,pose):
        """
        Is called whenever the Myo arm band detects a new pose.
        """
        self.pose = pose
        self.handler(pose=pose)

    def on_orientation_data(self,myo,timestamp,orientation):
        """
        Is called whenever the Myo arm band detects a new orientation.
        """
        self.orientation = orientation
        self.handler(orientation=orientation)

    def handler(self,pose=None,orientation=None):
        """
        Handles all pose and orientation data updates.
        """
        if pose == libmyo.Pose.double_tap:
            print "pose: double_tap"
            for light in self.lc.lights:
                self.lc.change_hue(light,xy=[0.3227,0.329])
        elif pose == libmyo.Pose.fingers_spread:
            print "pose: fingers_spread"
            for light in self.lc.lights: 
                self.lc.change_hue(light,xy=[0.6679,0.3181])
        elif pose == libmyo.Pose.wave_in:
            print "pose: wave_in"
            for light in self.lc.lights:
                self.lc.change_hue(light,xy=[0.1691,0.0441])
        elif pose == libmyo.Pose.wave_out:
            print "pose: wave_out"
            for light in self.lc.lights:
                self.lc.change_hue(light,xy=[0.4149,0.1776])
        elif pose == libmyo.Pose.fist:
            print "pose: fist"
            for light in self.lc.lights:
                self.lc.change_hue(light,xy=[0.41,0.51721])

def main():
    print("Connecting to Myo ... Use CTRL^C to exit.")
    try:
        hub = libmyo.Hub()
    except MemoryError:
        print("Myo Hub could not be created. Make sure Myo Connect is running.")
        return

    hub.set_locking_policy(libmyo.LockingPolicy.none)
    hub.run(1000, Listener())

    # Listen to keyboard interrupts and stop the hub in that case.
    try:
        while hub.running:
            time.sleep(0.25)
    except KeyboardInterrupt:
        print("\nQuitting ...")
    finally:
        print("Shutting down hub...")
        hub.shutdown()


if __name__ == '__main__':
    main()