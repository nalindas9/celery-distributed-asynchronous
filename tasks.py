import queue
from celery import Celery
from time import sleep
import cv2

# Use RabbitMQ as a broker
app = Celery('tasks',
             broker='amqp://guest@localhost//',
             backend='db+sqlite:///db.sqlite3')

@app.task(queue='first_camera')
def processImageFirstCamera(cam_id):
    print('Processing video from camera {}'.format(cam_id))
    # Display video from camera
    cap = cv2.VideoCapture(cam_id)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

@app.task(queue='second_camera')
def processImageSecondCamera(cam_id):
    print('Processing video from camera {}'.format(cam_id))
    # Display video from camera
    cap = cv2.VideoCapture(cam_id)
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
