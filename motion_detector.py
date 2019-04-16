import cv2
import numpy as np
import json
import urllib.request
import time
cameraName = "PiMotionCamera"

data = {
		"id": cameraName,
		"data": {
			"movementDetected" : False
		}
}
# Video Capture 
# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture(0)


# History, Threshold, DetectShadows 
# fgbg = cv2.createBackgroundSubtractorMOG2(50, 200, True)
fgbg = cv2.createBackgroundSubtractorMOG2(800, 600, True)

# Keeps track of what frame we're on
frameCount = 0
movement = False
while(1):
	i = 0
	while(i < 30):
            capture.grab()
            i += 1
        # Return Value and the current frame
	ret, frame = capture.read()
	#  Check if a current frame actually exist
	if not ret:
		break

	frameCount += 1
	# Resize the frame
	resizedFrame = cv2.resize(frame, (0, 0), fx=0.70, fy=0.70)

	# Get the foreground mask
	fgmask = fgbg.apply(resizedFrame)

	# Count all the non zero pixels within the mask
	count = np.count_nonzero(fgmask)

	print('Frame: %d, Pixel Count: %d' % (frameCount, count))
	
        # Determine how many pixels do you want to detect to be considered "movement"
	# if (frameCount > 1 and cou`nt > 5000):
	if (frameCount > 1 and count > 20):
		print('Motion Detected')
		cv2.putText(resizedFrame, 'Motion Detected', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
		data = {
                    "id": cameraName,
                    "data": {
			"movementDetected" : True
                    }
                    }
		req = urllib.request.Request("http://10.7.68.172:8080/api/v3/data/post")
		req.add_header("Content-Type", "application/json")
		req.add_header("Authorization", "Basic YXBpOmtleS0ydDEzeW5pbHE1aWlkZjEyNWh6ajV2cWltMmw1cmtoMw==")
		if(movement == False):
                    movement = True
                    response = urllib.request.urlopen(req, json.dumps(data).encode("utf8"))
                    print(response.read())
                    
		
	else:
		data = {
		"id": cameraName,
		"data": {
			"movementDetected" : False
		}
                }
		req = urllib.request.Request("http://10.7.68.172:8080/api/v3/data/post")
		req.add_header("Content-Type", "application/json")
		req.add_header("Authorization", "Basic YXBpOmtleS0ydDEzeW5pbHE1aWlkZjEyNWh6ajV2cWltMmw1cmtoMw==")
		if(movement):
                    movement = False
                    response = urllib.request.urlopen(req, json.dumps(data).encode("utf8"))
                    print(response.read())
	#cv2.imshow('Frame', resizedFrame)
	#cv2.imshow('Mask', fgmask)
	capture.grab()            

	if cv2.waitKey(3)==ord('q'):
		break

capture.release()
cv2.destroyAllWindows()
