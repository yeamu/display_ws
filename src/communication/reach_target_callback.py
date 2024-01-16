#! /usr/bin/env python3
import rospy,socket
from time import sleep
from move_base_msgs.msg import MoveBaseActionResult, MoveBaseActionFeedback

def result_callback(msg):
    if msg.status.status == 3:
        # sleep(0)
        print("Goal reached successfully")
        # send()
    elif msg.status.status == 4:
        print("Goal was unachievable")


def send(server_port=12345):
    autobee = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    autobee.connect(('127.0.0.1',server_port))

    autobee.sendall('send content'.encode())
    response = autobee.recv(1024)
    print(f"{response.decode()}")

    autobee.close()

def main():
    rospy.init_node('move_base_listener')

    rospy.Subscriber('/move_base/result',MoveBaseActionResult,result_callback)

    rospy.spin()

if __name__ == '__main__':
    main()