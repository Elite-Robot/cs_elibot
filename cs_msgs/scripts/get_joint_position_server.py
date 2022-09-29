from __future__ import print_function
from cs_msgs.srv import GetJointPosition,GetJointPositionResponse
import rospy
import instance as instance
from cs_msgs.rtsi import *
import time
from cs_msgs.serialize import *

def handle_get_joint_position(req):
    robot_ip = "192.168.51.83"
    rt = rtsi(robot_ip)
    rt.connect() 
    rt.version_check() 
    version = rt.controller_version() 
    # print("veriosn", version)

    output = rt.output_subscribe('actual_joint_positions',1)

    rt.start() 

    a = rt.get_output_data()
    # print(a.actual_joint_positions)
    # time.sleep(1)

    rt.send_message(message = b"123", source = b"Python Client", type = serialize.Message.ERROR_MESSAGE)
    rt.pause()
    rt.disconnect()
    return GetJointPositionResponse(a.actual_joint_positions)

def get_joint_position_server():
    rospy.init_node('get_joint_position_server')
    s = rospy.Service('get_joint_position', GetJointPosition, handle_get_joint_position)
    print("Ready to send joint positions.")
    rospy.spin()

if __name__ == "__main__":
    get_joint_position_server()