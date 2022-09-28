from __future__ import print_function

from cs_msgs.srv import GetJointPosition,GetJointPositionResponse
import rospy

import cmd
from logging import NullHandler
from pickle import TRUE
from turtle import goto
import socket
import json
import time
import copy
import os

def connectETController(ip, port=30001):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, port))
        return (True, sock)
    except Exception as e:
        sock.close()
        return (False,)

def sendCMD(sock, cmd, params=None, id=1):
    try:
        sock.sendall(cmd.encode("utf8"))
    except Exception as e:
        return (False, None, None)

def handle_get_joint_position(req):
    cmdscript = []
    spacestr = "  "
    robot_ip = "192.168.51.41"
    conSuc, sock = connectETController(robot_ip)
    print(conSuc)

    cmdscript.append('def getState():\n')
    cmdscript.append(spacestr+'global j\n')
    cmdscript.append(spacestr+'j = get_actual_joint_positions()\n')
    cmdscript.append(spacestr+'print(j)\n')
    cmdscript.append('end\n')
    out_script = ''
    for i in range(0,len(cmdscript)):
        out_script = out_script+ cmdscript[i]
    print(out_script)
    sendCMD(sock,out_script)
    time.sleep(10)

    print("Returning joints")
    return GetJointPositionResponse(j)

def get_joint_position_server():
    rospy.init_node('get_joint_position_server')
    s = rospy.Service('get_joint_position', GetJointPosition, handle_get_joint_position)
    print("Ready to get joint positions.")
    rospy.spin()

if __name__ == "__main__":
    get_joint_position_server()