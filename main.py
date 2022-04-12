import os
from tasks import *
from time import sleep
import cv2
import json
from utils import *

if __name__ == '__main__':
    # Use celery worker to process images
    # Webcam
    processFirstCam.delay()
    # External webcam
    processSecondCam.delay()