import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

recipient = 'patrik.muniak@gmail.com'
me = 'raspberrypi.cm@gmail.com'

msg = MIMEMultipart()
msg['Subject'] = 'emails with python'
msg['From'] = me
msg['To'] = recipient
text = 'motion detected at' + str(datetime.datetime.now())
body = MIMEText(text, 'plain')
fp = open('funny_pug_dog.jpg', 'rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(body)
msg.attach(img)

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login( 'raspberrypi.cm@gmail.com', 'Cubemate01')
server.sendmail(me, recipient, msg.as_string())
server.close()
