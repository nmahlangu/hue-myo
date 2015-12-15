# Hue-Myo
This project combines two pieces of cool hardware I have in my dormitory: [Philips Hue](http://www2.meethue.com/en-us/) + [Myo Gesture Control Armband](https://www.myo.com/). 

## Files
* [LightController.py](https://github.com/nmahlangu/hue-myo/blob/master/LightController.py): Implements a class with basic functionality for controlling a Hue bridge
* [Myo.py](https://github.com/nmahlangu/hue-myo/blob/master/Myo.py): Implements a class that listens to gestures from the Myo armband and uses a LightController object to modify Hue lights.

## Dependencies
* [Myo SDK](https://developer.thalmic.com/start/)

## Resources Used
* [myo-python](Python bindings for the Myo SDK)