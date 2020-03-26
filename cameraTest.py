import sched, time
from picamera import PiCamera

s = sched.scheduler(time.time, time.sleep)
camera = PiCamera()

def do_something(sc):
    print ("Doing stuff...")
    camera.capture('/home/pi/camerPhotos/')
    s.enter(10, 1, do_something, (sc,))

s.enter(10, 1, do_something, (s,))
s.run()
