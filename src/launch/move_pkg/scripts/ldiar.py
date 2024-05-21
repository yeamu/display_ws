#!/usr/bin/env python3
# coding=utf-8

import rospy
from sensor_msgs.msg import LaserScan

def lidar_callback(msg):
    dist = msg.ranges[0]
    rospy.loginfo("前方测距 = %f ",dist)


if __name__ == "__main__":
    rospy.init_node("lidar_node")
    lidar_sub = rospy.Subscriber("/scan",LaserScan,lidar_callback,queue_size=20)

    rospy.spin()