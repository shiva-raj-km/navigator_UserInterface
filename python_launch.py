import roslaunch
import rospy
import time
import sys
print(sys.argv[1])
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)

cli_args1 = ['navigator_bringup', 'robot_standalone.launch']
cli_args2 = ['navigator_bringup', '3dsensor.launch']
cli_args3 = ['cartographer_navigator', 'cartographer_demo.launch']
cli_args4 = ['navigator_bringup', 'view_navigation.launch']

roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(cli_args1)
# roslaunch_args1 = cli_args1[2:]

roslaunch_file2 = roslaunch.rlutil.resolve_launch_arguments(cli_args2)
# roslaunch_args2 = cli_args2[2:]

roslaunch_file3 = roslaunch.rlutil.resolve_launch_arguments(cli_args3)
roslaunch_file4 = roslaunch.rlutil.resolve_launch_arguments(cli_args4)

 

parent1 = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_file1)
parent2 = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_file2)
parent4 = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_file4)
parent3 = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_file3)


if(sys.argv[1] == '1'):
	parent1.start()
	parent2.start()
	time.sleep(5)
	parent3.start()
	time.sleep(5)
	parent4.start()
elif(sys.argv[1] == '0'):
	parent1.start()
	parent2.start()	
	time.sleep(5)
	parent3.start()

try:
	if(sys.argv[1] == '1'):
		parent1.spin()
		parent2.spin()
		parent3.spin()
		parent4.spin()
	elif(sys.argv[1] == '0'):
		parent1.spin()
		parent2.spin()
		parent3.spin()

   
finally:
  # After Ctrl+C, stop all nodes from running
  	if(sys.argv[1] == '1'):
		parent1.shutdown()
		parent2.shutdown()
		parent3.shutdown()
		parent4.shutdown()
	elif(sys.argv[1] == '0'):
		parent1.shutdown()
		parent2.shutdown()
		parent3.shutdown()
