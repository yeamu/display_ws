#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from time import sleep
from Visual_grabbing import crawl
from rmrobot import rm
import jaws


# ROS节点初始化
rospy.init_node('move_robot_node', anonymous=True)

# 创建速度发布器
cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

def move(distance, linear_speed):
    twist_cmd = Twist()
    twist_cmd.linear.x = linear_speed  # 设置线速度

    # 计算移动的持续时间
    move_duration = abs(distance) / abs(linear_speed)

    start_time = rospy.Time.now()
    current_time = rospy.Time.now()

    while (current_time - start_time).to_sec() < move_duration and not rospy.is_shutdown():
        cmd_vel_pub.publish(twist_cmd)
        current_time = rospy.Time.now()

    # 停止机器人移动
    twist_cmd.linear.x = 0.0
    cmd_vel_pub.publish(twist_cmd)
    rospy.loginfo("机器人移动完成")

if __name__ == '__main__':
    try:
        pos = {"command":"movej_p","pose":[-8563,266519,197725,3071,-46,-3127],"v":32,"r":0}
        place =  {"command":"movej_p","pose":[2512,468698,113159,2954,-42,3145],"v":32,"r":0}

        for _ in range(2):

            if crawl():

                move(1, -0.2)
                rm(place)
                jaws.open()
                # 静止位
                rm(pos)
                move(1, 0.2)
            else:
                print('没有识别到抓取物')
                break
    
    except rospy.ROSInterruptException:
        pass
