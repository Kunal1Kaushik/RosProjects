#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import sys
def move_turtle():

  

    rospy.init_node('move_circle1', anonymous=False)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
   
    

    rate = rospy.Rate(10) # 10hz
    n = 0
 
    vel = Twist()
    while not rospy.is_shutdown():
        
	vel.linear.x = 3.0
	vel.linear.y = 0
	vel.linear.z = 0

	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = 1.5
# n records the number of times we have published till now. Using the frequency with which we #publish, we know that when we would have published a given number of times, our bot would have #completed a circle ( we can find out the time taken to complete one circle knowing the angular #velocity of the bot )
	if( n>=(((2*3.14)/(1.5))/0.1)-((((2*3.14)/6.0)/(1.5))/0.1)):
		rospy.loginfo("Robot Reached destination")
		rospy.logwarn("Stopping robot")

		break

        pub.publish(vel)

        rate.sleep()
        n = n+1
        

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
