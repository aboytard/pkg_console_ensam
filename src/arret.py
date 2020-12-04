#!/usr/bin/env python

import subprocess

import rospy
from std_msgs.msg import String

def callback(string):
	pub.publish("demande arret urgence recue")
	subprocess.check_call('rosnode kill -a', shell=True)


rospy.init_node("controle")
pub = rospy.Publisher("T_Ordre_urgence", String, queue_size=1)
sub = rospy.Subscriber("T_arret_urgence", String, callback)
rospy.spin()


