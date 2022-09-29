import rospy
from cs_driver.cs_driver import CSDriver

def main() -> None:
    rospy.init_node('cs_driver', disable_signals=True)
    cs_driver = CSDriver()
    loop_rate = rospy.get_param("~/loop_rate", default=125)
    rate = rospy.Rate(loop_rate)

if __name__ == "__main__":
    main()