#!/usr/bin/env python

import rospy
import actionlib
import time
import os
import subprocess 
import sys

import signal
#move_base_msgs
from move_base_msgs.msg import *
from numpy import interp
import tkinter as tk
from tkinter import *
from tkinter import messagebox,ttk
from std_msgs.msg import Bool




def simple_move(x,y,z,w):

	rospy.init_node('simple_move')

	#Simple Action Client
	sac = actionlib.SimpleActionClient('move_base', MoveBaseAction )

	#create goal
	goal = MoveBaseGoal()

	#use self?
	#set goal

	rospy.loginfo("Set X = "+x)
	rospy.loginfo("Set W = "+w)

	goal.target_pose.pose.position.x = float(x)
	goal.target_pose.pose.position.y = float(y)
	goal.target_pose.pose.orientation.z = float(z)
	goal.target_pose.pose.orientation.w = float(w)
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.header.stamp = rospy.Time.now()



	#start listner
	rospy.loginfo("Waiting for server")

	sac.wait_for_server()


	rospy.loginfo("Sending Goals")

	#send goal

	sac.send_goal(goal)
	rospy.loginfo("Waiting for server")

	#finish
	sac.wait_for_result(rospy.Duration.from_sec(10.0)) # wait for 10 sec after the goal point given

	#print result
	print(sac.get_result())

class login_page():
	def __init__(self,window):
		self.main = window


		self.main.update_idletasks()							#	For dynamic changes
		self.main.geometry('500x500+435+115')
		self.main.minsize(width=600,height=600)
		self.main.maxsize(width=600,height=600)
		self.main.title('SMART NAVIGATOR')
		self.main.config(background='#FFFDD0')
		self.user_name = tk.StringVar()
		self.password_ = tk.StringVar()
		tk.Label(self.main,text='WELCOME',background='#FFFDD0',activebackground="green",fg='red',font=("Times New Roman",25,"bold")).place(relx=0.34,rely=0.05)
		tk.Label(self.main,text='TO',background='#FFFDD0',activebackground="green",fg='red',font=("Times New Roman",25,"bold")).place(relx=0.45,rely=0.12)
		tk.Label(self.main,text='SMART NAVIGATOR',background='#FFFDD0',activebackground="green",fg='red',font=("Times New Roman",25,"bold")).place(relx=0.22,rely=0.19) #0.22

		# img_arena2 = tk.PhotoImage(file = "2.png")
		# img_arena2 = img_arena2.subsample(1,1)
		# arena2 = tk.Button(self.main,image=img_arena2,command=enable)
		# arena2.image = img_arena2
		# arena2.place(relx=0.25,rely=0.4)

		frame_team_details= tk.Frame(self.main,background='#F2F5EB')

		tk.Label(frame_team_details,text ='User Name : ',background='#F2F5EB').grid(row=2,column=0)
		tk.Label(frame_team_details,text ='Password : ',background='#F2F5EB').grid(row=3,column=0)

		user = tk.Entry(frame_team_details,textvariable=self.user_name,width=18).grid(row=2,column=1)
		password = tk.Entry(frame_team_details,textvariable=self.password_,width=18,show='*').grid(row=3, column=1)

		submit_button = tk.Button(self.main, activebackground="green" ,text = 'Submit',state='normal',command = self.submit_button_fn,cursor="sb_right_arrow")
		submit_button.place(anchor="center",relx=0.85,rely=0.95)
		frame_team_details.place(anchor="center",relx=0.5,rely=0.5)



		exit_button = tk.Button(self.main,activebackground="red",text='Exit',command= window.destroy,cursor="X_cursor").place(relx=0.45,rely=0.92)


		self.main.protocol('WM_DELETE_WINDOW', self.close)



	def submit_button_fn(self):
		# print(self.user_name.get(),self.password_.get())
		if(self.user_name.get() != 'q' or self.password_.get() != 'q'):
			tk.Label(self.main,text='\twrong credentials\t\t',background='#F2F5EB',fg='red',font=("arial",15,'bold')).place(relx=0.2,rely=0.65)
		else:
			# print('ok')
			second = tk.Toplevel(self.main)
			self.main.withdraw()
			a= manual(second,self.main)
	def close(self):
		self.main.destroy()
		engine.say('thank you')
		engine.runAndWait()

class manual():
	"""docstring for ClassName"""
	def __init__(self, second,main):
		self.second = second
		self.value = True
		self.main = main
		self.second.update_idletasks()							#	For dynamic changes
		self.second.geometry('500x500+435+115')
		self.second.minsize(width=600,height=600)
		self.second.maxsize(width=600,height=600)
		self.second.title('SMART NAVIGATOR')
		self.second.config(background='#FFFDD0')
		# tk.Label(self.second,text='Low Charge Indication - ',background='#FFFDD0',fg='red',font=("Times New Roman",15,"bold")).place(relx=0.05,rely=0.02)
		# if(self.value == False):
		# 	tk.Label(self.second,text='TRUE',background='#FFFDD0',fg='red',font=("Times New Roman",15,"bold")).place(relx=0.45,rely=0.02)
  # 		else:
		# 	tk.Label(self.second,text='FALSE',background='#FFFDD0',fg='green',font=("Times New Roman",15,"bold")).place(relx=0.45,rely=0.02)
		
		tk.Label(self.second ,text='BOT CONTROL',background='#FFFDD0',activebackground="green",fg='red',font=("Times New Roman",15,"bold")).place(relx=0.3,rely=0.05)

		self.auto_control = tk.Button(self.second, activebackground="green" ,text = 'AUTO CONTROL',command = self.auto,cursor="sb_right_arrow",state='disabled').place(relx=0.1,rely=0.2)
		self.voice = tk.Button(self.second, activebackground="green" ,text = 'Voice CONTROL',command = self.voice,cursor="sb_right_arrow",state='disabled').place(relx=0.35,rely=0.35)
		self.manual_control = tk.Button(self.second, activebackground="green" ,text = 'Manual CONTROL',command = self.manual,cursor="sb_right_arrow",state='disabled').place(relx=0.6,rely=0.2)

		back = tk.Button(self.second,text='Back',activebackground='blue',command=self.back_window,cursor="sb_left_arrow").place(anchor="e",relx=0.2,rely=0.95)
		exit_button = tk.Button(self.second,activebackground="red",text='Exit',command= window.destroy,cursor="X_cursor").place(relx=0.45,rely=0.92)
		self.second.protocol('WM_DELETE_WINDOW', self.close)    # Access to default close button
		start = tk.Button(self.second,text='START',activebackground='blue',command=self.start,cursor="sb_left_arrow",font=("Times New Roman",20,"bold"),fg='green').place(anchor="e",relx=0.55,rely=0.5)
		stop = tk.Button(self.second,text='STOP',activebackground='red',command=self.stop,cursor="sb_left_arrow",font=("Times New Roman",20,"bold"),fg='red').place(anchor="e",relx=0.535,rely=0.7)

	def auto(self):
		if(messagebox.askyesno('Type of Navigation','Click Yes for landmark type, No for map type',parent=self.second) == True):
			print("landmark")	
			auto_landmark = tk.Toplevel(self.second)
			self.second.withdraw()
			a= auto_landmark_page(auto_landmark,self.second,self.main)
		else:
			print("map")
			auto_map = tk.Toplevel(self.second)
			self.second.withdraw()
			a= auto_map_page(auto_map,self.second,self.main)

	def voice(self):
		print("voice model")

	def manual(self):
		print("manual model")
		keyboard = tk.Toplevel(self.second)
		self.second.withdraw()
		a= keyboard_page(keyboard,self.second,self.main)

	def start(self):
		self.a = messagebox.askyesno('Image View','Click Yes if Image view is required',parent=self.second)
		if(self.a):
			image = subprocess.Popen(['python',"color_image.py"])
		self.rviz = messagebox.askyesno('RVIZ View','Click Yes if RVIZ view is required',parent=self.second)
		if(self.rviz == True):
			self.process = subprocess.Popen(['python', "python_launch.py",'1'])
		else:
			self.process = subprocess.Popen(['python', "python_launch.py",'0'])
		time.sleep(3)
		self.auto_control = tk.Button(self.second, activebackground="green" ,text = 'AUTO CONTROL',command = self.auto,cursor="sb_right_arrow",state='normal').place(relx=0.1,rely=0.2)
		self.voice = tk.Button(self.second, activebackground="green" ,text = 'Voice CONTROL',command = self.voice,cursor="sb_right_arrow",state='normal').place(relx=0.35,rely=0.35)
		self.manual_control = tk.Button(self.second, activebackground="green" ,text = 'Manual CONTROL',command = self.manual,cursor="sb_right_arrow",state='normal').place(relx=0.6,rely=0.2)

	def stop(self):
		self.auto_control = tk.Button(self.second, activebackground="green" ,text = 'AUTO CONTROL',command = self.auto,cursor="sb_right_arrow",state='disabled').place(relx=0.1,rely=0.2)
		self.voice = tk.Button(self.second, activebackground="green" ,text = 'Voice CONTROL',command = self.voice,cursor="sb_right_arrow",state='disabled').place(relx=0.35,rely=0.35)
		self.manual_control = tk.Button(self.second, activebackground="green" ,text = 'Manual CONTROL',command = self.manual,cursor="sb_right_arrow",state='disabled').place(relx=0.6,rely=0.2)

		try:
			self.process.send_signal(signal.SIGTERM)
			self.process.wait()
			if(self.a == True):
				self.image.kill()
				self.image.wait()
		finally:
			self.process.terminate()
			if(self.a):
				self.image.terminate()
			time.sleep(1)

	def back_window(self):
		self.second.withdraw()               # Hiding of current page and displaying of previous page
		self.main.update()
		self.main.deiconify()

	def close(self):
		self.main.destroy()

class keyboard_page():
	"""docstring for ke"""
	def __init__(self, keyboard,second,main):
		self.second = second
		self.main = main
		self.keyboard = keyboard
		self.keyboard.geometry('500x500+435+115')
		self.keyboard.minsize(width=600,height=600)
		self.keyboard.maxsize(width=600,height=600)
		self.keyboard.title('SMART NAVIGATOR')
		self.keyboard.config(background='#FFFDD0')
		back = tk.Button(self.keyboard ,text='Back',activebackground='blue',command=self.back_window,cursor="sb_left_arrow").place(anchor="e",relx=0.2,rely=0.95)
		# exit_button = tk.Button(self.keyboard,activebackground="red",text='Exit',command= window.destroy,cursor="X_cursor").place(relx=0.45,rely=0.92)
		tk.Label(self.keyboard ,text='MANUAL CONTROL',background='#FFFDD0',activebackground="green",fg='red',font=("Times New Roman",15,"bold")).place(relx=0.34,rely=0.05)
		
		start = tk.Button(self.keyboard,text='Start',activebackground='blue',command=self.start,cursor="sb_left_arrow").place(anchor="e",relx=0.3,rely=0.5)
		stop = tk.Button(self.keyboard,text='Stop',activebackground='red',command=self.stop,cursor="sb_left_arrow").place(anchor="e",relx=0.3,rely=0.7)

	def close(self):
		self.main.destroy()

	def start(self):
		self.teleop = subprocess.Popen(['python', "navigator_teleop_key.py"])
		back = tk.Button(self.keyboard ,text='Back',activebackground='blue',command=self.back_window,cursor="sb_left_arrow",state='disabled').place(anchor="e",relx=0.2,rely=0.95)
		tk.Label(self.keyboard,text="Please go to the command promt and follow",background='#FFFDD0',font=("Times New Roman",15,"bold"),fg='blue').place(relx=0.2,rely=0.2)
		tk.Label(self.keyboard,text="the keyboard instructions to run the bot manually",background='#FFFDD0',font=("Times New Roman",15,"bold"),fg='blue').place(relx=0.16,rely=0.25)
		start = tk.Button(self.keyboard,text='Start',activebackground='blue',command=self.start,cursor="sb_left_arrow",state='disabled').place(anchor="e",relx=0.3,rely=0.5)

	def stop(self):
		back = tk.Button(self.keyboard ,text='Back',activebackground='blue',command=self.back_window,cursor="sb_left_arrow",state='normal').place(anchor="e",relx=0.2,rely=0.95)
		start = tk.Button(self.keyboard,text='Start',activebackground='blue',command=self.start,cursor="sb_left_arrow",state='normal').place(anchor="e",relx=0.3,rely=0.5)

	 	try:
	 		self.teleop.kill()
	 		self.teleop.wait()
	 	finally:
	 		self.teleop.terminate()
	 		time.sleep(1)

	 	
	def back_window(self):
		self.keyboard.withdraw()               # Hiding of current page and displaying of previous page
		self.second.update()
		self.second.deiconify()

class auto_map_page():
	def __init__(self,auto_map,second,main):
		self.auto_map = auto_map
		self.second = second
		self.main = main
		self.direc_list = ["N", "S", "E", "W", "NE", "NW","SE","SW"]
		self.direc = tk.StringVar()
		self.auto_map.update_idletasks()							#	For dynamic changes
		self.auto_map.geometry('500x500+435+115')
		self.auto_map.minsize(width=600,height=600)
		self.auto_map.maxsize(width=600,height=600)
		self.auto_map.title('SMART NAVIGATOR')
		self.auto_map.config(background='#FFFDD0')
		# exit_button = tk.Button(self.auto_map,activebackground="red",text='Exit',command= window.destroy,cursor="X_cursor").place(relx=0.45,rely=0.92)

		canvas = Canvas(self.auto_map, width = 360, height = 300,bg='#FFFDD0')      
		canvas.place(relx=0.2,rely=0.25)     
		self.img = PhotoImage(file="map.png")  
		self.img = self.img.subsample(2,2)

		x1 = 20
		y1 = 30
		x2 = 380
		y2 = 370    
		# canvas.create_rectangle(x1, y1, x2, y2, fill="blue", tag='map')
		canvas.create_image(0,0, anchor=NW, image=self.img,tag='map')
		canvas.tag_bind('map', '<Button-1>', self.showxy) 
		tk.Label(self.auto_map ,text ='Orientation: ',background='#FFFDD0').place(relx=0.2,rely=0.15)
		tk.Label(self.auto_map ,text='AUTOMATIC CONTROL',background='#FFFDD0',activebackground="green",fg='red',font=("Times New Roman",15,"bold")).place(relx=0.34,rely=0.05)
		direction = ttk.Combobox(self.auto_map,textvariable=self.direc,values=self.direc_list,width=17).place(relx=0.35,rely=0.15)
		back = tk.Button(self.auto_map ,text='Back',activebackground='blue',command=self.back_window,cursor="sb_left_arrow").place(anchor="e",relx=0.2,rely=0.95)
		self.auto_map.protocol('WM_DELETE_WINDOW', self.close)

	def close(self):
		self.main.destroy()

	def showxy(self,event):
		x = event.x
		y = event.y
		print(x,y)
		x_ = interp(x,[123,273],[-1,1])
		y_ = interp(y,[79,227],[1,-1])
		
		if(self.direc.get() == 'N'):
			z=0
			w=1
		elif(self.direc.get() == 'E'):
			z=-0.7
			w=0.7
		elif(self.direc.get() == 'S'):
			z=1
			w=0
		elif(self.direc.get() == 'W'):
			z=0.7
			w=0.7
		elif(self.direc.get() == 'NE'):
			z=-0.34
			w=0.938
		elif(self.direc.get() == 'NW'):
			z=0.4
			w=0.908
		elif(self.direc.get() == 'SE'):
			z=-0.859
			w=0.511
		elif(self.direc.get() == 'SW'):
			z=0.83
			w=0.549
		x_ = str(x_)
		y_ = str(y_)
		z = str(z)
		w = str(w)
		print(x_,y_,z,w)
		# try:
		# 	simple_move(x_,y_,z,w)
		# except rospy.ROSInterruptException:
		# 	print ("Keyboard Interrupt")

	def back_window(self):
		self.auto_map.withdraw()               # Hiding of current page and displaying of previous page
		self.second.update()
		self.second.deiconify()

class auto_landmark_page():
	"""docstring for ClassName"""
	def __init__(self,auto_landmark, second,main):
		self.auto_landmark = auto_landmark
		self.second = second
		self.main = main
		self.auto_landmark.update_idletasks()							#	For dynamic changes
		self.auto_landmark.geometry('500x500+435+115')
		self.auto_landmark.minsize(width=600,height=600)
		self.auto_landmark.maxsize(width=600,height=600)
		self.auto_landmark.title('SMART NAVIGATOR')
		self.auto_landmark.config(background='#FFFDD0')
		tk.Label(self.auto_landmark ,text='AUTOMATIC CONTROL',background='#FFFDD0',activebackground="green",fg='red',font=("Times New Roman",15,"bold")).place(relx=0.34,rely=0.05)
		# exit_button = tk.Button(self.auto_landmark,activebackground="red",text='Exit',command= window.destroy,cursor="X_cursor").place(relx=0.45,rely=0.92)
		back = tk.Button(self.auto_landmark ,text='Back',activebackground='blue',command=self.back_window,cursor="sb_left_arrow").place(anchor="e",relx=0.2,rely=0.95)
		self.auto_landmark.protocol('WM_DELETE_WINDOW', self.close)
		charge_button = tk.Button(self.auto_landmark, activebackground="green" ,text = 'POINT-1',state='normal',command = self.Charge,cursor="sb_right_arrow").place(relx=0.1,rely=0.3)
		rest_button = tk.Button(self.auto_landmark, activebackground="green" ,text = 'START',state='normal',command = self.living_room,cursor="sb_right_arrow").place(relx=0.1,rely=0.8)
		water_button = tk.Button(self.auto_landmark, activebackground="green" ,text = 'POINT-2',state='normal',command = self.bed_room,cursor="sb_right_arrow").place(relx=0.8,rely=0.3)
		tv_button = tk.Button(self.auto_landmark, activebackground="green" ,text = 'POINT-3',state='normal',command = self.kitchen,cursor="sb_right_arrow").place(relx=0.8,rely=0.8)


	def back_window(self):
		self.auto_landmark.withdraw()               # Hiding of current page and displaying of previous page
		self.second.update()
		self.second.deiconify()
	def close(self):
		self.main.destroy()

	def Charge(self):
		# try:
		# 	simple_move("1.97","0.04","0.006","0.999")
		# except rospy.ROSInterruptException:
		# 	print "Keyboard Interrupt"

		print "Charging Point Reached"

	def living_room(self):
		# try:
		# 	simple_move("0.034","0.027","0.005","0.999")
		# except rospy.ROSInterruptException:
		# 	print "Keyboard Interrupt"
		print "living_room Point Reached"

	def bed_room(self):
		# try:
		# 	simple_move("1.98","-1.63","-0.72","0.68")
		# except rospy.ROSInterruptException:
		# 	print "Keyboard Interrupt"
		print "bed Point Reached"

	def kitchen(self):
		# try:
		# 	simple_move("0.072","-1.525","1.0","0.006")
		# except rospy.ROSInterruptException:
		# 	print "Keyboard Interrupt"
		print "kitchen Point Reached"

window = tk.Tk()
login_page(window)
window.mainloop()