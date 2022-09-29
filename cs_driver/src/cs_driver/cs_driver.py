import rospy
import time
from cs_driver.get_joint_position_server import GetJointPositionService

class CSDriver(GetJointPositionService):

    def __init__(self) -> None:
        rospy.loginfo("CSDriver is started")
        self.r_ip_address = rospy.get_param("~r_ip_address")
        GetJointPositionService.__init__(self)