#!/usr/bin/env python3
#coding = utf-8



import rospy
from std_msgs.msg import String

def callback(m):
  rospy.loginfo(m.data)


if __name__ == "__main__":
  rospy.init_node("s_node")
  rospy.logwarn("node successfully init")
  sub=rospy.Subscriber("topic_py",String,callback=callback,queue_size=10)
  while not rospy.is_shutdown() :
    rospy.spin()