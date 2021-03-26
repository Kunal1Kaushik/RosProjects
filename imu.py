#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import Imu
from matplotlib import pyplot as plt
counter = 0
def callback(data):
    g = data.linear_acceleration.x
    h = data.linear_acceleration.y
    i = data.linear_acceleration.z
    with open('linear_accleration.txt', 'a') as file:
        file.write("x : " + str(g) + "\ny : " + str(h) + "\nz : " + str(i) + "\n")
    
    global counter
    if counter % 10==0 :
        plt.plot(g, h, '*')
        plt.axis("equal")
        plt.draw()
        plt.pause(0.00000000001)

    counter += 1

   
       
    
    

def imua():
    global counter
    counter = 0
    rospy.init_node('imu', anonymous=True)
    rospy.Subscriber("/imu", Imu, callback)
    plt.ion()
    plt.show()
    rospy.spin()

if __name__ == '__main__':
    imua()   
# This script plots the imu linear acceleration data ( x-acceleration vs y-acceleration( x-axis   #and y-axis respectively )
         
