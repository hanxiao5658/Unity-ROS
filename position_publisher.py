#!/usr/bin/env python3

import roslib
import sys
import random
import rospy
import rosgraph
import time
import numpy as np
import math
import os
import tf
from geometry_msgs.msg import Quaternion
from math import tan, pi
from unity_robotics_demo_msgs.msg import UnityColor
from unity_robotics_demo_msgs.msg import PosRot
from tf import transformations



TOPIC_NAME = 'color'
NODE_NAME = 'color_publisher'
#from sensor_msgs.msg import Joy
#from geometry_msgs.msg import TwistStamped
#from geometry_msgs.msg import PoseStamped

class color_publisher:

	def __init__(self):
    
		self.pub = rospy.Publisher('pos_rot_pub',  PosRot, queue_size=10)
		#self.posdata = rospy.Subscriber("/pos_rot", PosRot, self.pose_callback)
    		
		self.attitude = [0,0,0]
		self.pub_data = PosRot(0,0,0,0,0,0,0)
		
	def wait_for_connections(self,pub, topic):
		ros_master = rosgraph.Master('/rostopic')
		topic = rosgraph.names.script_resolve_name('rostopic', topic)
		num_subs = 0
		for sub in ros_master.getSystemState()[1]:
			if sub[0] == topic:
				num_subs+=1

		for i in range(10):
			if pub.get_num_connections() == num_subs:
				return
			time.sleep(0.1)
		raise RuntimeError("failed to get publisher")



	def pose_callback(self, msg):
		self.attitude = tf.transformations.euler_from_quaternion((msg.rot_x,msg.rot_y,msg.rot_z,msg.rot_w))
		
		

        
	def fan_con(self):
		roll = 1.57
		pitch = 1.57
		yaw = 3.14
		
		angle = tf.transformations.quaternion_from_euler(roll,pitch,yaw)
		
		self.pub_data.pos_x = random.randint(0, 10)
		self.pub_data.pos_y = random.randint(0, 10)
		self.pub_data.pos_z = random.randint(0, 10)
		
		self.pub_data.rot_x = angle[0]
		self.pub_data.rot_y = angle[1]
		self.pub_data.rot_z = angle[2]
		self.pub_data.rot_w = angle[3]
		#self.wait_for_connections(self.pub_data, 'pos_rot_pub')
		self.pub.publish(self.pub_data)
		print("posx",self.pub_data)

    	
def main(args):
    rospy.init_node('color_publisher', anonymous=True)
    r = rospy.Rate(30) 
    ip = color_publisher()

    seq = [0,0]

    while not rospy.is_shutdown():
        ip.fan_con()
        r.sleep()


if __name__ == '__main__':
    main(sys.argv)

