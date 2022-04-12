import queue
from celery import Celery
from time import sleep
import cv2

# Use RabbitMQ as a broker
app = Celery('tasks',
             broker='amqp://guest@localhost//',
             backend='db+sqlite:///db.sqlite3')

@app.task(queue='semantic_segmentation')
def semanticSegmentation(cam_ids):
    print('Semantic segmentation task started')
    print('Camera IDs:', cam_ids)
    # Video capture object for the cameras
    cap = [cv2.VideoCapture(cam_id) for cam_id in cam_ids]
    print('Video capture objects created: {}'.format(cap))
    # Display video for the cameras
    while True:
        # Read the frames
        frames = [cap[i].read()[1] for i in range(len(cap))]
        # Stitch the frames horizontally
        stitched = cv2.hconcat(frames)
        # Show the stitched frames
        cv2.imshow('Semantic segmentation', stitched)
        # Wait for key press
        key = cv2.waitKey(1)
        # Stop if 'q' is pressed
        if key == ord('q'):
            break
    # Release the video capture objects
    for cap in cap:
        cap.release()
    # Destroy all windows
    cv2.destroyAllWindows()

@app.task(queue='second_camera')
def process(cam_id):
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
