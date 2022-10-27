# import openCV
import cv2 as cv
import numpy as np

# video capture object intialize
vid = cv.VideoCapture(0)

while(True):
      
    # Capture the video frame by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()