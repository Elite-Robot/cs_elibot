from __future__ import print_function

import sys
import rospy
from cs_msgs.srv import *

import instance as instance
from cs_msgs.rtsi import *
import time
from cs_msgs.serialize import *

def joint_move_client():
    rospy.wait_for_service('joint_move')
    try:
        joint_move = rospy.ServiceProxy('joint_move', JointMove)
        joint_ = [-1.57,-1.57,-1.57,-1.57,1.57,0]
        acc_ = 5
        speed_ = 1 
        time_ = 0
        radius_ = 0
        resp1 = joint_move(joint_,acc_,speed_,time_,radius_)
        print("Move joint execution status : ")
        return resp1.result
    
        robot_ip = "192.168.51.83"
        rt = rtsi(robot_ip)
        rt.connect() 
        rt.version_check() 
        version = rt.controller_version() 
        input = rt.input_subscribe('input_double_register0,input_double_register1,input_double_register2,input_double_register3,input_double_register4,input_double_register5,input_double_register6,input_double_register7')
        rt.start()
        input.input_double_register0 = -0.79
        input.input_double_register1 = -1.57
        input.input_double_register2 = 0.79
        input.input_double_register3 = 0.79
        input.input_double_register4 = 0.79
        input.input_double_register5 = 0.79
        input.input_double_register6 = 0.5
        input.input_double_register7 = 0.5
        rt.set_input(input)
        rt.send_message(message = b"123", source = b"Python Client", type = serialize.Message.ERROR_MESSAGE)
        rt.pause()
        rt.disconnect()
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
 
if __name__ == "__main__":
    print("Requesting move joint")
    resp = joint_move_client()
    print(resp)