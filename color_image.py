import time
import os
import subprocess 
import sys
import signal

google = os.system('rosrun image_view image_view image:=/camera/rgb/image_color')