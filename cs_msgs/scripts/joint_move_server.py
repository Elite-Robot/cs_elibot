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
    # TODO : put ip as argument
    robot_ip = "192.168.51.82"
    conSuc, sock = connectETController(robot_ip)
    print(conSuc)
    res = JointMoveResponse()
    target_joint_ = req.target_joint
    # TODO : check none values
    acc_ = req.acc
    speed_ = req.speed
    time_ = req.time
    radius_ = req.radius

    # TODO : set parameters from req
    cmdscript.append('def movejscript():\n')
    # cmdscript.append(spacestr+'target_joint_ = [0,0,0.3,0.3,0.3,0]\n')
    # cmdscript.append(spacestr+'acc_ = 5\n')
    # cmdscript.append(spacestr+'speed_ = 1\n')
    # cmdscript.append(spacestr+'time_ = 0\n')
    # cmdscript.append(spacestr+'radius_ = 0\n')
    # cmdscript.append(spacestr+'movej(target_joint_, acc_, speed_, time_, radius_)\n')

    cmdscript.append(spacestr+'j0_ = read_input_float_register(0)\n')
    cmdscript.append(spacestr+'j1_ = read_input_float_register(1)\n')
    cmdscript.append(spacestr+'j2_ = read_input_float_register(2)\n')
    cmdscript.append(spacestr+'j3_ = read_input_float_register(3)\n')
    cmdscript.append(spacestr+'j4_ = read_input_float_register(4)\n')
    cmdscript.append(spacestr+'j5_ = read_input_float_register(5)\n')
    cmdscript.append(spacestr+'a = read_input_float_register(6)\n')
    cmdscript.append(spacestr+'v = read_input_float_register(7)\n')
    cmdscript.append(spacestr+'movej([j0_,j1_,j2_,j3_,j4_,j5_], a, v, 0, 0)\n')
    cmdscript.append('end\n')

    out_script = ''
    for i in range(0,len(cmdscript)):
        out_script = out_script+ cmdscript[i]

    print(out_script)

    sendCMD(sock,out_script)
    time.sleep(10)
    res.result = True # TODO : get feedback from def function
    return res

    if type(result_) == bool:
        res.result = result_
    else:
        res.result = result_[0]
    rospy.loginfo("JointMoveService ended...")
    return res

def joint_move_server():
    rospy.init_node('joint_move_server')
    s = rospy.Service('joint_move', JointMove, handle_joint_move)
    print("Ready to send joint move command.")
    rospy.spin()

if __name__ == "__main__":
    joint_move_server()