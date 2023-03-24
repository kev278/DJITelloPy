# import the opencv library
import cv2
import os
import time
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
filename = 'image.png'
path1 = '/home/keval/Desktop/DJISwarm/DJITelloPy/videoTransfer/drone1'
path2 = '/home/keval/Desktop/DJISwarm/DJITelloPy/videoTransfer/drone2'
i = 0

while(True):
       
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imwrite(os.path.join(path1 , 'pic{:>05}.jpg'.format(i)), frame)
    i = i + 1
    time.sleep(5)  
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()