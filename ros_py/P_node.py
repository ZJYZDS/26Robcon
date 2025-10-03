#!/usr/bin/env python3
#coding = utf-8

import rospy
from std_msgs.msg import String
if __name__=="__main__":
    rospy.init_node("P_node")
    rospy.logwarn("node init successfully")
    pub = rospy.Publisher("topic_py",String,queue_size=10)
    rate=rospy.Rate(10)
    while(not rospy.is_shutdown()):
        m=String()
        m.data="2023113135张家源"
        pub.publish(m)  
        rate.sleep()