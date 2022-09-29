#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from cs_msgs.srv import *

def get_joint_position_client():
    rospy.wait_for_service('get_joint_position')
    try:
        get_joint_position = rospy.ServiceProxy('get_joint_position', GetJointPosition)
        resp1 = get_joint_position()
        print("Here are the joint positions [rad] : ")
        return resp1.pos
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
 
if __name__ == "__main__":
    # x = int(sys.argv[1])
    print("Requesting joint positions")
    pos = get_joint_position_client()
    print(pos)