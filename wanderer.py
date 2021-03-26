#!/usr/bin/env python
import rospy 
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist 

def callback(dt):
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    move = Twist()
# a 15 degree range either side is checked for
    thr1 = 0.8 
    thr2 = 0.8
    if dt.ranges[0]>thr1 and dt.ranges[15]>thr2 and dt.ranges[345]>thr2: 
        move.linear.x = 0.5 
        move.angular.z = 0.0 
    else:
        move.linear.x = 0.0 
        move.angular.z = 0.5 
        if dt.ranges[0]>thr1 and dt.ranges[15]>thr2 and dt.ranges[345]>thr2:
            move.linear.x = 0.5
            move.angular.z = 0.0
    pub.publish(move) 


 
def wanderer():
    rospy.init_node('wanderer', anonymous=True) 
      

    sub = rospy.Subscriber("/scan", LaserScan, callback)  

    rospy.spin() 
if __name__ == '__main__':
   wanderer()   
# rotate the bot on object detection, keep on moving forward otherwise


