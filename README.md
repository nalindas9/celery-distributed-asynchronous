# celery-distributed-asynchronous

[![License:MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/nalindas9/celery-distributed-asynchronous/blob/master/LICENSE)

## About
Using Celery Asynchronous Task queue based on distributed message system to fetch two tasks - 1) Data Augmentation (Cam 1), 2) Computing optical flow (Cam 2). 
Assigns the task 1 to celery worker 1 and task 2 to worker 2 and then execute it.

## Output

https://user-images.githubusercontent.com/44141068/162973679-2c998f96-490a-4159-b8ed-b873aedc01a3.mp4

## System Diagram

![celery](https://user-images.githubusercontent.com/44141068/162987909-084eb2b9-abb9-407b-bf4a-fcfb30b6ae54.jpeg)


## System and library requirements

- Ubuntu==18.04.5 LTS
- Python==3.6.9
- celery==5.1.2
- numpy==1.19.5
- opencv_python==4.5.5.64
- Pillow==9.1.0
- scipy==1.5.4
- torchvision==0.11.2

## How to Run
1. Clone this repo. <br>
2. Navigate into the folder `celery-distributed-asynchronous` <br>
3. Create and activate [Virtual Environment](https://docs.python.org/3/library/venv.html) <br>
4. Upgrade pip using `python -m pip install --upgrade pip`.
5. Install requirements.txt using command `pip install -r requirements.txt`
6. Before starting main client, we need to start the celery workers. In two more terminals, enter the following commands (Before that Repeat Step 3 for each terminal) - 

```
Terminal 1 - celery -A tasks worker --loglevel=info -Q frames --concurrency 2 -n worker1@%h # Starts worker 1

Terminal 2 - celery -A tasks worker --loglevel=info -Q frames --concurrency 2 -n worker2@%h # Starts worker 2
```

7. To run the main client, from the terminal, run the command `python3 main.py` <br>
8. You should see two windows pop up. First window shows the Data Augmentation(Rotation, Flip and Perspective Transform) applied to the frames with a probability of 30%. The second window shows the Optical Flow computed where the hue is based on the flow direction and value based on the flow magnitude. Both windows stitched with original frame side by side.


