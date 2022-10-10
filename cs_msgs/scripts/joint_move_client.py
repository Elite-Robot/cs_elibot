from __future__ import print_function

import sys
import rospy
from cs_msgs.srv import *

def joint_move_client():
    rospy.wait_for_service('joint_move')
    try:
        joint_move = rospy.ServiceProxy('joint_move', JointMove)
        joint_ = [-1.2,-0.7,-0.9,-1.57,1.57,0]
        acc_ = 3
        speed_ = 2 
        time_ = 0
        radius_ = 0
        resp1 = joint_move(joint_,acc_,speed_,time_,radius_)
        print("Move joint execution status : ")
        return resp1.result
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
 
if __name__ == "__main__":
    print("Requesting move joint")
    resp = joint_move_client()
    print(resp)