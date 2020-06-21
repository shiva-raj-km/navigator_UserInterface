# navigator_UserInterface
A User Interface application for controlling the Smart_navigator
## Prerequisites
Complete setup of Smart_navigator or the cartographer_navigator.
## Setup
``` bash
sudo apt-get install python-tk # To install tkinter

git clone https://github.com/shiva-raj-km/navigator_UserInterface.git
# Copy the Python scripts to scripts folder in navigator_bringup package.
```
## Usage
The main script is gui.py which runs the launch files. It has login page, bot control page with start & stop button to run the launch files. The python_launch.py script is a file used to run the launch files using python script.

The navigator can be controlled using the system, at this time only roscore and server.py should be run in terminals.

## References
* [Python Tkinter](https://docs.python.org/3/library/tk.html) To develop GUI.
* [Python roslaunch API](http://wiki.ros.org/roslaunch/API%20Usage) To run launch files using Python script.
* [ROS Workspace Overlay](http://wiki.ros.org/catkin/Tutorials/workspace_overlaying) When using two workspaces, but automation is required. 
* [ROS Network](http://wiki.ros.org/ROS/NetworkSetup) For server-client operation.
