# motionEmail

File pir.py will be the one that runs. 
  It has raspberry pi GPIO set up for an Infrared Motion Sensor. 
  It will wait until motion is detected and will run the motionemail.py file.

Create info.py which will store all the credentials for the motionEmail.py as such:

class info():
	sender_email = "sender_email@gmail.com"
  password = "sender_email_password"
	receiver_email = "receiver_email@gmail.com"
