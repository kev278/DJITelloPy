# run this program on each RPi to send a labelled image stream
import socket
import time
from imutils.video import VideoStream
import imagezmq
from djitellopy import tello

drone = tello.Tello()
drone.connect()
drone.streamon()
#drone.set_video_direction(1)

sender = imagezmq.ImageSender(connect_to='192.168.0.117:5555')

rpi_name = socket.gethostname() # send RPi hostname with each image
time.sleep(2.0)  # allow camera sensor to warm up
while True:  # send images as stream until Ctrl-C
   image = drone.get_frame_read().frame
   sender.send_image(rpi_name, image)
