#!/usr/bin/env python

import rospy
from std_msgs.msg import String,Bool
import time
import os
import subprocess 
import sys
import signal
# import rospy
# import actionlib
# from move_base_msgs.msg import *


class server():
	"""docstring for ser"""
	def __init__(self):

		rospy.init_node('server',anonymous=True)
		rospy.Subscriber("start",String,self.callback,queue_size=10)
		rospy.spin()

	def start(self):
		if(self.list[1]=='1'):
			self.image = subprocess.Popen(['python',"color_image.py"])
		if(self.list[2]=='1'):
			self.process = subprocess.Popen(['python', "python_launch.py",'1'])
		else:
			self.process = subprocess.Popen(['python', "python_launch.py",'0'])
		time.sleep(3)
		
	def stop(self):

		try:
			self.process.send_signal(signal.SIGTERM)
			self.process.wait()
			if(self.list[1]):
				self.image.kill()
				self.image.wait()
		finally:
			self.process.terminate()
			if(self.list[1]):
				self.image.terminate()
			time.sleep(1)


	def callback(self,data):

		self.list = []
		a = data.data
		self.list = a.split()
		if(self.list[0]=='1'):
			self.start()	
		else:
			self.stop()
	

	


if __name__ == '__main__':
	server()