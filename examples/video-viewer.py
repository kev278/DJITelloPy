from djitellopy import tello
import cv2


drone = tello.Tello()
drone.connect()
drone.streamon()
#drone.set_video_direction(1)

while True:
    img = drone.get_frame_read().frame
    cv2.imshow('stream', img)
    cv2.waitKey(1)
