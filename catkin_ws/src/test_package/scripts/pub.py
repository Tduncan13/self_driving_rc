#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('talker', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) #10hz
    counter = 0
    while not rospy.is_shutdown():
        counter
        hello_str = "hello world %s" % counter
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        counter += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    

    
