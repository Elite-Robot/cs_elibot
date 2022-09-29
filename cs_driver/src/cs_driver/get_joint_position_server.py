from __future__ import print_function
from cs_msgs.srv import GetJointPosition, GetJointPositionResponse, GetJointPositionRequest
import rospy
import instance as instance
from cs_msgs.rtsi import *
import time
from cs_msgs.serialize import *

class GetJointPositionService():

    def __init__(self) -> None:
        s = rospy.Service('get_joint_position', GetJointPosition, self.handle_get_joint_position)
        print("Ready to send joint positions.")
        rospy.spin()

    def handle_get_joint_position(self, req: GetJointPositionRequest) -> GetJointPositionResponse:
        res = GetJointPositionResponse()
        # robot_ip = "192.168.51.83"
        rt = rtsi(self.r_ip_address)
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
        res.pos = a.actual_joint_positions
        return res
        # return GetJointPositionResponse(a.actual_joint_positions)