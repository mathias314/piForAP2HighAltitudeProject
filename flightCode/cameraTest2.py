from picamera import PiCamera
from time import sleep

camera = PiCamera()

for i in range(690000):
    sleep(5)
    print("Taking photo")
    camera.capture('/home/pi/cameraPhotos/image%s.jpg' % i)
    print("Photo taken")
