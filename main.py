from tasks import *
from time import sleep
import cv2

if __name__ == '__main__':
    # Use celery worker to process images
    # Webcam
    result_camera1 = semanticSegmentation.delay([0, 2])
    # External webcam
    #result_camera2 = process.delay(2)