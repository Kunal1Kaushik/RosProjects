#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import sys
import random
def mover():
    rospy.init_node('randombot', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    while not rospy.is_shutdown():
        r = random.randint(1, 90)
        r1 = r/9.0
        vel.linear.x = r1
        vel.linear.y = r1/2
        vel.linear.z = 0.0
        vel.angular.x = 0.0
        vel.angular.y = 0.0
        vel.angular.z = r1/3
        pub.publish(vel)
        rate.sleep()
if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass
# This script gives random linear and angular velocities to Turtlebot3, of which we plot the imu # linear acceleration data through the other node in the package!


