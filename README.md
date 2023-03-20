# motionEmail
This project was a feature used for my senior design project. <br />
It may not be supported anymore as gmail drops support for "Less secure apps".

First provide the credentials to your gmail account in info.py <br />
Make sure the data cable for the PIR motion sensor connected to gpio 4 of the Pi. <br />
You can choose to have a LED (connected to gpio 17) go off when motion is detected. <br />
Run pir.py which will wait until the PIR sensor will send a signal. <br />
It will wait until motion is detected and will run the motionemail.py file. <br />
