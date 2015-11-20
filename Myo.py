# from __future__ import print_function

import myo as libmyo; libmyo.init('/Users/Nicholas/Documents/cs/git/hue-myo/sdk/myo.framework')
import time
import sys

class Listener(libmyo.DeviceListener):
    """
    Listener implementation. Hub is stopped if any function returns
    False.
    """

    interval = 0.05 # Output only 0.05 seconds

    def __init__(self):
        super(Listener, self).__init__()
        self.orientation = None 
        self.pose = libmyo.Pose.rest
        self.locked = False


    def on_connect(self, myo, timestamp, firmware_version):
        """
        Is called when the Myo arm band is connected via Bluetooth.
        """
        myo.vibrate('short')
        myo.vibrate('short')
        print "Connected to Myo"

    def on_pose(self, myo, timestamp, pose):
        """
        Is called whenever the Myo arm band detects a new pose.
        """
        self.pose = pose
        print pose
        # TODO: handle pose

    def on_orientation_data(self, myo, timestamp, orientation):
        """
        Is called whenever the Myo arm band detects a new orientation.
        """
        self.orientation = orientation
        print orientation
        # TODO: handle orientation






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