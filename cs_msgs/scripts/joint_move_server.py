from __future__ import print_function
from cs_msgs.srv import JointMove,JointMoveResponse
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

def disconnectETController(sock):
    if (sock):
        sock.close()
        sock = None
    else:
        sock = None

def sendCMD(sock, cmd, params=None, id=1):
    try:
        sock.sendall(cmd.encode("utf8"))

    except Exception as e:
        return (False, None, None)

def handle_joint_move(req):
    cmdscript = []
    spacestr = "  "
    robot_ip = "192.168.51.82"
    conSuc, sock = connectETController(robot_ip)
    print(conSuc)
    res = JointMoveResponse()
    target_joint_ = list(req.target_joint)
    acc_ = req.acc
    speed_ = req.speed
    time_ = req.time
    radius_ = req.radius

    cmdscript.append('def movejscript():\n')
    cmdscript.append(spacestr+'target_joint_ = ' + str(target_joint_) + '\n')
    cmdscript.append(spacestr+'acc_ = ' + str(acc_) + '\n')
    cmdscript.append(spacestr+'speed_ = ' + str(speed_) + '\n')
    cmdscript.append(spacestr+'time_= ' + str(time_) + '\n')
    cmdscript.append(spacestr+'radius_ = ' + str(radius_) + '\n')
    cmdscript.append(spacestr+'movej(target_joint_, acc_, speed_, time_, radius_)\n')
    cmdscript.append('end\n')

    out_script = ''
    for i in range(0,len(cmdscript)):
        out_script = out_script+ cmdscript[i]

    print(out_script)

    sendCMD(sock,out_script)
    time.sleep(10)
    # TODO : get feedback from def function
    res.result = True 
    return res

def joint_move_server():
    rospy.init_node('joint_move_server')
    s = rospy.Service('joint_move', JointMove, handle_joint_move)
    print("Ready to send joint move command.")
    rospy.spin()

if __name__ == "__main__":
    joint_move_server()