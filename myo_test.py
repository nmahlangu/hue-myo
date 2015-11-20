import Myo
# # import myo as libmyo; libmyo.init('/Users/Nicholas/Documents/cs/git/hue-myo/sdk/myo.framework')
# import time
# import sys

print("Connecting to Myo ... Use CTRL^C to exit.")
try:
    hub = libmyo.Hub()
except MemoryError:
    print("Myo Hub could not be created. Make sure Myo Connect is running.")

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

