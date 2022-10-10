from __future__ import print_function
from cs_msgs.srv import JointMove,JointMoveResponse,JointMoveRequest
from .__basecs import BaseCS
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

class JointMoveService(BaseCS):

    def __init__(self) -> None:
        s = rospy.Service('joint_move', JointMove, self.handle_joint_move)
        print("Ready to send joint move command.")
        rospy.spin()

    def handle_joint_move(self, req: JointMoveRequest) -> JointMoveResponse:
        cmdscript = []
        spacestr = "  "
        robot_ip = self.r_ip_address
        print(robot_ip)
        conSuc, sock = self.connectETController(robot_ip)
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

        self.sendCMD(sock,out_script)
        time.sleep(10)
        # TODO : get feedback from def function
        res.result = True 
        return res