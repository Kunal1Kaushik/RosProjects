#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import sys
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
def callback(vel): 
    global a
    global b
    global c
    global d
    global e
    global f
    a = vel.linear.x
    b = vel.linear.y
    c = vel.linear.z
    d = vel.angular.x
    e = vel.angular.y
    f = vel.angular.z
    if ( a==0 and b==0 and c==0 and d==0 and e==0 and f==0 ):
        rospy.loginfo("x : %f",g)
        rospy.loginfo("y : %f",h)
        with open('poses.txt', 'a') as file:
            file.write("x : (" + str(g) + ")" + ", y : (" + str(h) + ")\n")
def callback1(data):
    global g
    global h
    g = data.pose.pose.position.x 
    h = data.pose.pose.position.y
    
     
     
def record_pose():
   
    rospy.init_node('record_pose', anonymous=True)
    rospy.Subscriber('/cmd_vel', Twist, callback)
    rospy.Subscriber('/odom', Odometry, callback1)
    
    rospy.spin()
if __name__ == '__main__':
    record_pose()   
# We note the poses of the bot when its linear and angular velocity is zero. The .txt file is made #in the home directory in the hidden .ros folder.
         

