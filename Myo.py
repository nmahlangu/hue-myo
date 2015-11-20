import myo as libmyo; libmyo.init('/Users/Nicholas/Documents/cs/git/hue-myo/sdk/myo.framework')
import time
import sys

class Listener(libmyo.DeviceListener):

    def __init__(self):
        super(Listener, self).__init__()
        self.orientation = None 
        self.pose = libmyo.Pose.rest
        self.locked = False

    # Is called when the Myo arm band is connected via Bluetooth.
    def on_connect(self, myo, timestamp, firmware_version):
        myo.vibrate('short')
        print "Connected to Myo"
        time.sleep(1)

    # Is called whenever the Myo arm band detects a new pose.
    def on_pose(self, myo, timestamp, pose):
        self.pose = pose
        self.handler(pose=pose)

    # Is called whenever the Myo arm band detects a new orientation.
    def on_orientation_data(self, myo, timestamp, orientation):
        self.orientation = orientation
        self.handler(orientation=orientation)

    # Handles all data updates
    def handler(self, pose=None, orientation=None):
        if pose:
            print "pose: ", pose
        # if orientation:
        #     print "orientation: ", orientation






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