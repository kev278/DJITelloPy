
# Welcome to PyShine
# lets make the client code
# In this code client is sending video to server
import socket,cv2, pickle,struct
import pyshine as ps # pip install pyshine
import imutils # pip install imutils
import time

from djitellopy import tello

drone = tello.Tello()
drone.connect()
drone.streamon()
#drone.set_video_direction(1)


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '192.168.0.117' # Here according to your server ip write the address

port = 9999
client_socket.connect((host_ip,port))

# for saving video
frame_width = int(drone.get_frame_read().frame.get(3))
#frame_width = int(video.get(3))
frame_height = int(drone.get_frame_read().frame.get(3))
size = (frame_width, frame_height)
result = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

if client_socket: 
	while True:
		try:
			frame = drone.get_frame_read().frame
			frame = imutils.resize(frame,width=380)
			a = pickle.dumps(frame)
			message = struct.pack("Q",len(a))+a
			client_socket.sendall(message)
			cv2.imshow(f"TO: {host_ip}",frame)
			# save video from frames
			result.write(frame)
			key = cv2.waitKey(1) & 0xFF
			if key == ord("q"):
				client_socket.close()
		except:
			print('VIDEO FINISHED!')
			break


