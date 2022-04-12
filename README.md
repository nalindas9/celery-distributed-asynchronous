# celery-rabbitmq

[![License:MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/nalindas9/object-detection/blob/master/LICENSE)

Plan is to have two webcams simultaneouslty pushing data to rabbitmq and celery and 
semantic segmentation

celery -A tasks worker --loglevel=info -Q first_camera --concurrency 2 -n worker1@%h

celery -A tasks worker --loglevel=info -Q second_camera --concurrency 2 -n worker2@%h

## About
Using MobileNet SSD model to run inference and detect objects in the scene. Using PyQT5 for FrontEnd GUI.

## Output

https://user-images.githubusercontent.com/44141068/162973679-2c998f96-490a-4159-b8ed-b873aedc01a3.mp4

## System Diagram

![0001](https://user-images.githubusercontent.com/44141068/162976423-2b69927a-b6c8-4305-a2ab-b290e7fc7bca.jpg)

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
2. Navigate into the folder `object-detection` <br>
3. Create and activate [Virtual Environment](https://docs.python.org/3/library/venv.html) <br>
4. Upgrade pip using `python -m pip install --upgrade pip`.
5. Install requirements.txt using command `pip install -r requirements.txt`
6. To run the code, from the terminal, run the command `python3 main.py` <br>
7. You should see a window pop up. Click on open webcam to start detecting.
7. To stop detecting, simply click on stop webcam. To shutdown, click on cross topright corner.:)


