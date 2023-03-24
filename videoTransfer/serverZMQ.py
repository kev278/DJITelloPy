# run this program on the Mac to display image streams from multiple RPis
import cv2
import imagezmq
import time
import os
import glob

# delete all images in folders from last run
files = glob.glob('/home/keval/Desktop/DJISwarm/DJITelloPy/videoTransfer/drone1/*')
for f in files:
    os.remove(f)

files = glob.glob('/home/keval/Desktop/DJISwarm/DJITelloPy/videoTransfer/drone2/*')
for f in files:
    os.remove(f)

path1 = '/home/keval/Desktop/DJISwarm/DJITelloPy/videoTransfer/drone1'
path2 = '/home/keval/Desktop/DJISwarm/DJITelloPy/videoTransfer/drone2'

i = 0

image_hub = imagezmq.ImageHub()

while True:  # show streamed images until Ctrl-C
    rpi_name, image = image_hub.recv_image()

    # get name of computer that talks with the drone
    if rpi_name == 'acer':
        cv2.imwrite(os.path.join(path1 , 'pic{:>05}.jpg'.format(i)), image)
    
    else:
        cv2.imwrite(os.path.join(path2 , 'pic{:>05}.jpg'.format(i)), image)
    
    i = i + 1
    time.sleep(5) 
    cv2.imshow(rpi_name, image) # 1 window for each RPi
    cv2.waitKey(1)
    image_hub.send_reply(b'OK')
