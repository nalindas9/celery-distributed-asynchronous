from celery import Celery
from time import sleep
import cv2
import pickle
import numpy as np
from scipy import rand
from torchvision import models
from utils import *
from PIL import Image
import random

# Use RabbitMQ as a broker
app = Celery('tasks',
             broker='amqp://guest@localhost//',
             backend='db+sqlite:///db.sqlite3')

@app.task(queue='frames')
def processFirstCam():
    """
    Process the first webcam. Display
    the Data Augmentation and the Original
    frame side by side

    Args:
        None
    Returns:
        None
    """
    print("Processing first webcam")
    # Video capture object for the cameras
    cap = cv2.VideoCapture(0)
    # Display video for the cameras
    while True:
        # Read the frame
        ret, frame = cap.read()
        # Display the stitched frames
        cv2.imshow('first cam', frame)
        augment_frame = Image.fromarray(np.uint8(frame)).convert('RGB')
        # Augment the image with probability 0.2
        random_no = random.random()
        if random_no < 0.3:    
            augment_frame = augmentImg(augment_frame)
        # Convert the frame to numpy array
        augment_frame = np.array(augment_frame)
        # Horizontal stich augment frame and original frame
        stitched_frame = np.hstack((frame, augment_frame))
        # Display the augmented frame
        cv2.imshow('first cam', stitched_frame)
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
    """
    Process the second webcam. Display
    the Optical Flow and the Original
    frame side by side

    Args:
        None
    Returns:
        None
    """
    print("Processing second webcam")
    # Video capture object for the cameras
    cap = cv2.VideoCapture(2)

    ret, first_frame = cap.read()
    # Create zeros image for the first frame
    mask = np.zeros_like(first_frame)
    # Set image saturation to max
    mask[:, :, 1] = 255
    # Convert frame to grayscale
    prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    # Display video for the cameras
    while True:
        # Read the frames
        ret, frame = cap.read()
        # Convert image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Calculate dense optical flow Farnback algorithm
        flow = cv2.calcOpticalFlowFarneback(prev=prev_gray,
                                            next=gray, 
                                            flow=None, 
                                            pyr_scale=0.5, 
                                            levels=3, 
                                            winsize=15, 
                                            iterations=3, 
                                            poly_n=5, 
                                            poly_sigma=1.2, 
                                            flags=0)
        # Calculate magnitude and angle of the flow
        magnitude, angle = cv2.cartToPolar(flow[:, :, 0], flow[:, :, 1])
        # Set image hue according to the optical flow direction
        mask[:, :, 0] = angle * 180 / np.pi / 2
        # Set image value according to the optical flow magnitude (normalized)
        mask[:, :, 2] = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
        # Convert to RGB for display
        rgb = cv2.cvtColor(mask, cv2.COLOR_HSV2RGB)
        # Horizontal stich rgb and frame
        horizontal_stich = np.hstack((frame, rgb))
        # Display the frames
        cv2.imshow('second cam', horizontal_stich)
        # Stop if 'q' is pressed
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    # Release the video capture objects
    cap.release()
    # Destroy all windows
    cv2.destroyAllWindows()
    
    