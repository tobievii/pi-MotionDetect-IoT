# pi-MotionDetect-IoT
Uses USB Camera to detect movement , you can change the code to the DeviceId you want 
You can also uncomment the #cv2.imshow('Frame', resizedFrame) to see what the camera is seeing

to run in terminal
python3 /home/pi/prototype/examples/ComputerVision/pi-MotionDetect-IoT/motion_detector.py

to run in terminal no log output
python3 /home/pi/prototype/examples/ComputerVision/pi-MotionDetect-IoT/motion_detector.py &

Make sure you have OPENCV installed 

pip3 install -r requirements.txt 