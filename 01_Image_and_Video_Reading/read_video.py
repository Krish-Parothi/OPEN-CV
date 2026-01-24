import cv2

capture = cv2.VideoCapture('sunflower.mp4') # This Method Either Takes Integer Argument like 1 or 2 or 3 etc e.g cv2.VideoCapture(3) oe It takes the file path of the video. 

# Integer Arguments (0,1,2,3...) When you are using webcam or cameras connected to your computer.
# 0 -> Webcam
# 1 -> First Camera (if you have multiple cameras)
# 2 -> Second camera (if you have multiple cameras)


# Reading Video frame by frame
while True:
    isTrue, frame = capture.read()

    cv2.imshow('Video',frame)

    if cv2.waitKey(20) & 0xff == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()

# After Frame by frame when video is completed by reading all frames then it shows error like this:

# Traceback (most recent call last):
#   File "C:\Users\Krish\OneDrive\Desktop\GITHUB\OPEN-CV\Image_and_Video_Reading\read_video.py", line 15, in <module>
#     cv2.imshow('Video',frame)
#     ~~~~~~~~~~^^^^^^^^^^^^^^^
# cv2.error: OpenCV(4.12.0) D:\a\opencv-python\opencv-python\opencv\modules\highgui\src\window.cpp:973: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'cv::imshow'

# bcoz there are no more frames left to read thats why this error comes.

# same error comes when u give wrong video path in videocapture method.