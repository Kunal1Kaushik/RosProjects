#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2
from angles import shortest_angular_distance
import sys

x = 0.0
y = 0.0
theta = 0.0

def odomo(msg):
    global x
    global y
    global theta
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    q = msg.pose.pose.orientation
    (r, p, theta) = euler_from_quaternion([q.x, q.y, q.z, q.w])
def driver(ra, tx, ty):
    rospy.init_node("driver")
    rospy.Subscriber("/odom", Odometry, odomo)
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    velocity = Twist()
    t = rospy.Rate(10)
    goal = Point()
    goal.x = tx
    
    goal.y = (ty - ra) 
# we approach the point (targetx, targety -radius) . When our bot is close to this point, we stop #and orient our bot parallel to the x-axis, and then revolve around (targetx, targety)
    
    while not rospy.is_shutdown():
        ix = goal.x - x
        iy = goal.y - y
        if ( abs(ix)<=0.2 and abs(iy)<=0.2):
            velocity.linear.x = 0.0
            velocity.linear.y = 0.0
            velocity.linear.z = 0.0
            velocity.angular.x = 0.0
            velocity.angular.y = 0.0
            velocity.angular.z = 0.0
            pub.publish(velocity)
            t.sleep()
            
            
            if abs(theta)>0.1 :
                velocity.linear.x = 0.0
                velocity.linear.y = 0.0
                velocity.linear.z = 0.0
                velocity.angular.x = 0.0
                velocity.angular.y = 0.0
                velocity.angular.z = 0.7
                pub.publish(velocity)
                t.sleep()
            else :
                velocity.linear.x = 0.0
                velocity.linear.y = 0.0
                velocity.linear.z = 0.0
                velocity.angular.x = 0.0
                velocity.angular.y = 0.0
                velocity.angular.z = 0.0
                pub.publish(velocity) 
                rospy.sleep(3)
                velocity.linear.x = 0.4
                velocity.linear.y = 0.0
                velocity.linear.z = 0.0
                velocity.angular.x = 0.0
                velocity.angular.y = 0.0
                velocity.angular.z = (0.4/ra)
                pub.publish(velocity)
                break

            
            
            
        else:
            angletogoal = atan2( iy, ix)
            ang_dist = shortest_angular_distance(theta, angletogoal)
            sign = ang_dist/abs(ang_dist)
            if abs(ang_dist)>0.1:
                velocity.linear.x = 0.0
                if ang_dist>0.5:
                    velocity.angular.z = sign
                else:
                    velocity.angular.z = sign*max(abs(0.3*sign), abs(ang_dist))
            else : 
                velocity.linear.x = 0.5
                velocity.angular.z = 0.0
            pub.publish(velocity)
            t.sleep()
if __name__ == '__main__':
   driver(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))   





