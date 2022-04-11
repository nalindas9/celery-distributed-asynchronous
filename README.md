# celery-rabbitmq

Plan is to have two webcams simultaneouslty pushing data to rabbitmq and celery and 
semantic segmentation

celery -A tasks worker --loglevel=info -Q first_camera --concurrency 2 -n worker1@%h

celery -A tasks worker --loglevel=info -Q second_camera --concurrency 2 -n worker2@%h
