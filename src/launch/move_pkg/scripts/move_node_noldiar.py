#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from time import sleep
from Visual_grabbing import crawl
from rmrobot import rm
import jaws
class MoveRobotWithOdom:
    def __init__(self):
        rospy.init_node('move_robot_with_odom_node', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.odom_sub = rospy.Subscriber('/wheel_odom', Odometry, self.odom_callback)

        self.rate = rospy.Rate(10)  # 设置发布速率为10Hz
        self.current_pose = None

        # 等待里程计消息
        rospy.wait_for_message('/wheel_odom', Odometry)

    def odom_callback(self, odom_msg):
        # 接收里程计信息并更新当前位置
        self.current_pose = odom_msg.pose.pose

    def move(self, distance, speed):
        rospy.loginfo(f"开始移动 {distance} 米，速度 {speed} m/s")

        # 等待里程计数据被更新
        while self.current_pose is None and not rospy.is_shutdown():
            rospy.loginfo("等待里程计数据更新...")
            rospy.sleep(1)  # 等待1秒

        start_pose = self.current_pose
        twist_cmd = Twist()
        twist_cmd.linear.x = speed  # 设置线速度

        while not rospy.is_shutdown() and self.current_pose:
            current_x = self.current_pose.position.x
            distance_travelled = abs(current_x - start_pose.position.x)

            rospy.loginfo(f"已移动距离: {distance_travelled} 米")

            # 如果机器人达到目标距离，执行抓取程序并停止机器人
            if distance_travelled >= distance:
                rospy.loginfo(f"达到目标距离: {distance} 米")
                twist_cmd.linear.x = 0.0  # 停止机器人
                self.cmd_vel_pub.publish(twist_cmd)
                
                # 执行抓取程序
                # rm(place)
                # jaws.open()
                # rm(pos)
                
                break

            self.cmd_vel_pub.publish(twist_cmd)
            self.rate.sleep()

        rospy.loginfo("移动结束")

if __name__ == '__main__':
    try:
        pos = {"command":"movej_p","pose":[-8563,266519,197725,3071,-46,-3127],"v":8,"r":0}
        place =  {"command":"movej_p","pose":[2512,468698,113159,2954,-42,3145],"v":8,"r":0}
        move_robot = MoveRobotWithOdom()

        for _ in range(2):
        
            crawl()
            # 向后移动 1 米，速度为 -0.2 m/s
            move_robot.move(distance=1, speed=-0.2)
            rm(place)
            jaws.open()
            # 静止位
            rm(pos)
            move_robot.move(distance=1, speed=0.2)


    except rospy.ROSInterruptException:
        pass