import rospy
import time 
from cs_driver.get_joint_position_server import GetJointPositionService
from cs_driver.joint_move_server import JointMoveService

class CSDriver(GetJointPositionService, JointMoveService):

    def __init__(self) -> None:
        rospy.loginfo("CSDriver is started")
        self.r_ip_address = rospy.get_param("~r_ip_address")
        GetJointPositionService.__init__(self)
        JointMoveService.__init__(self)