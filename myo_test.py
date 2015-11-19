from __future__ import print_function
import myo as libmyo; libmyo.init('/Users/Nicholas/Documents/cs/git/hue-myo/sdk/myo.framework')
import time
import sys

feed = libmyo.device_listener.Feed()
hub = libmyo.Hub()
hub.run(1000, feed)
try:
    myo = feed.wait_for_single_device(timeout=10.0)  # seconds
    if not myo:
        print("No Myo connected after 10 seconds.")
        sys.exit()

    while hub.running and myo.connected:
        quat = myo.orientation
        print("Orientation:", quat.x, quat.y, quat.z, quat.w)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Quitting...")
finally:
    hub.shutdown()