#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan

def LidarCallback(msg):
    dist = msg.ranges
    print(len(dist))
    rospy.loginfo("== %f 米",min(dist[45:135:10]))

if __name__ == "__main__":
    rospy.init_node("lidar_test")
    lidar_sub = rospy.Subscriber("/scan",LaserScan,LidarCallback,queue_size=10)
    rospy.spin()