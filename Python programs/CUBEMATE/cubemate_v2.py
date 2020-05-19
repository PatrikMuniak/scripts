#!/usr/bin/env python3
from picamera import PiCamera
import time
import os
import cv2
import numpy as np
import datetime
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

os.chdir(r'/home/pi/Desktop') #ACTION REQUIRED!!! SET A NEW DIRECTORY WHERE TO STORE THE PICTURES

#SETTING UP EMAILS
def sending_email(frame1_name, frame2_name):
	sender_address = 'RASPBERRYPI EMAIL'			#ACTION REQUIRED!!!
	recipient_address = 'YOUR EMAIL'		#ACTION REQUIRED!!!
	msg = MIMEMultipart()
	msg['Subject'] = 'Motion detected!!!'
	msg['From'] = sender_address
	msg['To'] = recipient_address
	text = 'Motion detected on ' + str(datetime.datetime.now())
	body = MIMEText(text, 'plane')
	frame_to_send_1 = open(frame1_name, 'rb')
	attached_frame1 = MIMEImage(frame_to_send_1.read())
	frame_to_send_2 = open(frame2_name, 'rb')
	attached_frame2 = MIMEImage(frame_to_send_2.read())
	frame_to_send_1.close()
	frame_to_send_2.close()
	#ATTACHING TO EMAIL
	msg.attach(body)
	msg.attach(attached_frame1)
	msg.attach(attached_frame2)

	#SENDING EMAIL
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login( sender_address, '**PASSWORD**')		#inster password and change EMAIL ADDRESS
	server.sendmail(sender_address, recipient_address, msg.as_string())
	server.close()
	print('email sent')

def delete_frames(frame1_name, frame2_name):
		os.remove(frame1_name)
		os.remove(frame2_name)


#CAMERA SETTINGS
camera = PiCamera( resolution =(640,320))
camera.led = False


def take_frameset():
	#TAKING PICTURES
	tempo=time.time()
	frame1_name=str(tempo)+'.jpg'
	camera.led = False
	camera.capture(str(tempo)+'.jpg', resize = (320, 240))
	time.sleep(0.5)
	tempo=time.time()
	frame2_name=str(tempo)+'.jpg'
	camera.led = False
	camera.capture(str(tempo)+'.jpg', resize = (320, 240))

	#READING PICTURES
	frame1=cv2.imread(frame1_name, 0)
	frame2=cv2.imread(frame2_name, 0)

	#TOTAL FRAME1 AND TOTAL FRAME2

	np_matrix_frame1 = np.asmatrix(frame1)
	total_frame1 = np_matrix_frame1.sum()

	np_matrix_frame2 = np.asmatrix(frame2)
	total_frame2 = np_matrix_frame2.sum()

	#PIXEL DIFFERENCE TOTAL
	total_difference = int(total_frame2) - int(total_frame1)


	#TOTAL VARIATION FROM FRAME1

	relative_total_variation = (total_difference/total_frame1)*100
	print(str(round(relative_total_variation, 2))+'%')

	if abs(relative_total_variation) >= 2:   #THIS VALUE NEEDS TO BE ADAPTED FOR THE CIRCUMSTANCES
		sending_email(frame1_name, frame2_name)
		take_frameset()
	else:
		delete_frames(frame1_name, frame2_name)
		take_frameset()

take_frameset()
