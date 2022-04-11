from tasks import *
from time import sleep

if __name__ == '__main__':
    # Use celery worker to process images
    result_camera1 = processImageFirstCamera.delay(1)
    result_camera2 = processImageSecondCamera.delay(2) 
    # Print status
    while result_camera1.status != 'SUCCESS' or result_camera2.status != 'SUCCESS':
        print('Camera 1: {}, Camera 2: {}'.format(result_camera1.status, 
                                              result_camera2.status))
        sleep(1)
    # Print result
    print('Camera 1: {}, Camera 2: {}'.format(result_camera1.get(),
                                              result_camera2.get()))