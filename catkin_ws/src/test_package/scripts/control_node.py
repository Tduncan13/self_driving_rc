#!/usr/bin/env python 

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy 

def callback(data):
    h = data.axes[0]
    v = data.axes[1]
    if h > 0.5:
        rospy.loginfo('Left')
    elif h < -0.5:
        rospy.loginfo('Right')

    if v > 0.5:
        rospy.loginfo('Up')
    elif v < -0.5:
        rospy.loginfo('Down')

def get_control_data():
    rospy.init_node('control_listener', anonymous=True)
    rospy.Subscriber('joy', Joy, callback)
    rospy.spin()

if __name__ == '__main__':
    get_control_data()
