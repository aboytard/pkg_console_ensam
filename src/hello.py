#!/usr/bin/env python
import rospy
rospy.init_node("greeter")
rate = rospy.Rate(1) # it means 1hz
while not rospy.is_shutdown():
   print("hello world {0}".format(rospy.get_time()))
   rate.sleep()

