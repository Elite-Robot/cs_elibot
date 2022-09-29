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
    robot_ip = "192.168.51.83"
    pc_ip = "192.168."
    conSuc, sock = connectETController(robot_ip)
    print(conSuc)

    cmdscript.append('def getJointState():\n')
    cmdscript.append(spacestr+'global j\n')
    cmdscript.append(spacestr+'j = get_actual_joint_positions()\n')
    # cmdscript.append(spacestr+'print(j)\n')
    cmdscript.append(spacestr+'j0 = j[0]\n')
    cmdscript.append(spacestr+'j1 = j[1]\n')
    cmdscript.append(spacestr+'j2 = j[2]\n')
    cmdscript.append(spacestr+'j3 = j[3]\n')
    cmdscript.append(spacestr+'j4 = j[4]\n')
    cmdscript.append(spacestr+'j5 = j[5]\n')
    cmdscript.append(spacestr+'socket_open(pc_ip,23333,"socket_1")\n')
    cmdscript.append(spacestr+'socket_send_string(str(j0)+","+str(j1)+","+str(j2)+","+str(j3)+","+str(j4)+","+str(j5),"socket_1")\n')
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