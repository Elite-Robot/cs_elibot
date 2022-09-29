# ROS Driver for CS Elite robot

# Instructions

The code was tested with Ubuntu 20.04, and ROS Noetic. Different OS and ROS versions are possible but not supported.

### Clone the following package

`cd <CATKIN_WS_DIR>/src`

`git clone https://github.com/garg-akash-elibot/cs_elibot.git`

### Compile 

`catkin_make`

### Run

Test the GetJointPosition service:

`roslaunch cs_driver cs_driver.launch robot_ip:=<cs_robot_ip>`

`rosrun cs_msgs get_joint_position_client.py`

### Contact

In case of any encountered error, do not hesitate to contact us on

`akashgarg@elibot.cn`
