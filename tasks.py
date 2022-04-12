from celery import Celery
from time import sleep
import cv2
import pickle
import numpy as np
import pixellib
from pixellib.semantic import semantic_segmentation

# Use RabbitMQ as a broker
app = Celery('tasks',
             broker='amqp://guest@localhost//',
             backend='db+sqlite:///db.sqlite3')

@app.task(queue='frames')
def processFirstCam():
    print('Preprocessing...')
    # Video capture object for the cameras
    cap = cv2.VideoCapture(0)
    print('Video capture objects created: {}'.format(cap))
    # Display video for the cameras
    while True:
        # Read the frame
        ret, frame = cap.read()
        # Display the stitched frames
        cv2.imshow('first cam', frame)
        # Stop if 'q' is pressed
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    # Release the video capture objects
    cap.release()
    # Destroy all windows
    cv2.destroyAllWindows()   

@app.task(queue='frames')
def processSecondCam():
    print('Semantic segmentation...')
    # Video capture object for the cameras
    cap = cv2.VideoCapture(2)
    print('Video capture objects created: {}'.format(cap))
    # Display video for the cameras
    while True:
        # Read the frames
        ret, frame = cap.read()
        # Display the frames
        cv2.imshow('second cam', frame)
        # Stop if 'q' is pressed
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    # Release the video capture objects
    cap.release()
    # Destroy all windows
    cv2.destroyAllWindows()
    
    