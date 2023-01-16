#!/usr/bin/env python
# Software License Agreement (BSD License)

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from hw1_turtlesim.msg import Num
import math
import time
from std_srvs.srv import Empty


class Calc:
    def __init__(self):
        rospy.Subscriber("/hello", circularMotion, self.first_topic_callback)
        self.pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        
        self.x = 0
        self.y = 0
        self.z = 0
        self.ax = 0
        self.ay = 0
        self.az = 0

        # self.radius = 0
        # self.velocity = 0
        # self.direction = 0
        
    def first_topic_callback(self, data):
        print(data.velocity)
        print(data.radius)
        self.x = data.velocity
        self.y = 0
        self.z = 0
        self.ax = 0
        self.ay = 0
        self.az = data.velocity / data.radius

        rospy.loginfo("---")

    def second_msg_publish(self):
        msg = Twist()	

        msg.linear.x = self.x
        msg.linear.y = self.y
        msg.linear.z = self.z
        msg.angular.x = self.ax
        msg.angular.y = self.ay
        msg.angular.z = self.az

        self.pub.publish(msg)
    
def main():
    rospy.init_node('publishernode', anonymous=False)
    rate = rospy.Rate(1)

    calc = Calc()
    while not rospy.is_shutdown():
        calc.second_msg_publish()
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
