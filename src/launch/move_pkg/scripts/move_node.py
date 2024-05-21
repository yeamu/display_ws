#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from time import sleep
# from Visual_grabbing import crawl


class MoveRobotWithOdomAndLidar:
    def __init__(self):
        rospy.init_node('move_robot_with_odom_lidar_node', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.odom_sub = rospy.Subscriber('/wheel_odom', Odometry, self.odom_callback)
        self.lidar_sub = rospy.Subscriber('/scan', LaserScan, self.lidar_callback)

        self.rate = rospy.Rate(10)  # 10 Hz
        self.current_pose = None
        self.min_distance = float('inf')  # 初始化最小距离为正无穷

    def odom_callback(self, odom_msg):
        # 获取里程计信息
        self.current_pose = odom_msg.pose.pose

    def lidar_callback(self, lidar_msg):
        # 获取激光雷达正前方扫描数据
        ranges = lidar_msg.ranges
       
        # 计算当前激光雷达扫描中的最小距离
        self.min_distance = min(ranges[45:135:10])

    def move(self, distance,speed):
        start_pose = self.current_pose
        # target_x = start_pose.position.x + distance
        twist_cmd = Twist()
        twist_cmd.linear.x = speed  # 调整线速度

        while not rospy.is_shutdown() and self.current_pose:
            current_x = self.current_pose.position.x
            distance_travelled = abs(current_x - start_pose.position.x)

            # 如果机器人前方的最小距离小于某个阈值，停止机器人
            if self.min_distance < 0.3:  # 根据实际情况调整阈值
                twist_cmd.linear.x = 0.0  # 停止机器人
                self.cmd_vel_pub.publish(twist_cmd)
                rospy.loginfo("机器人前方有障碍物，停止移动")
                break

            # 如果机器人达到目标距离，停止机器人，并建立 TCP 连接发送点位信息
            if distance_travelled >= distance:
                twist_cmd.linear.x = 0.0  # 停止机器人
                self.cmd_vel_pub.publish(twist_cmd)
                rospy.loginfo(f"达到目标距离: {distance} 米")
                sleep(1)
                # 执行抓取程序
                # crawl()
                break



            self.cmd_vel_pub.publish(twist_cmd)
            self.rate.sleep()


if __name__ == '__main__':
    try:
        move_robot = MoveRobotWithOdomAndLidar()

        rospy.sleep(2)  # 等待订阅者初始化

        move_robot.move(distance=2,speed=0.2)
       
        # move_robot.move(distance=2,speed=-0.2)
        print('start ok')
     
    except rospy.ROSInterruptException:
        pass
            