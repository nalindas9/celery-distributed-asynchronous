import queue
from celery import Celery
from time import sleep

# Use RabbitMQ as a broker
app = Celery('tasks',
             broker='amqp://guest@localhost//',
             backend='db+sqlite:///db.sqlite3')

@app.task(queue='first_camera')
def processImageFirstCamera(img_id):
    sleep(5)
    print('Processing imageee: {}'.format(img_id))
    return 'Processed imageee: {}'.format(img_id)

@app.task(queue='second_camera')
def processImageSecondCamera(img_id):
    sleep(3)
    print('Processing imageee: {}'.format(img_id))
    return 'Processed imageee: {}'.format(img_id)