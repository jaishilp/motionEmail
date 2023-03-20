# motionEmail
This project was a feature used for my senior design project.

File pir.py will be the one that runs. <br />
It has raspberry pi GPIO configured set up for an Infrared Motion Sensor.  <br />
It will wait until motion is detected and will run the motionemail.py file. <br />

Create an info.py which will store all the credentials for the motionEmail.py as such:

```
class info():
	sender_email = "sender_email@gmail.com"
	password = "sender_email_password"
	receiver_email = "receiver_email@gmail.com"
```
