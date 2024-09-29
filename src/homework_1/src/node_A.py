#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(f"Node A received final message: {msg.data}")

def node_a():
    rospy.init_node('node_A')
    pub = rospy.Publisher('outgoing_A', String, queue_size=10)
    sub = rospy.Subscriber('incoming_A', String, callback)

    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
        secret_message = "Message from A"
        rospy.loginfo(f"Node A sending: {secret_message}")
        pub.publish(secret_message)
        rate.sleep()

if __name__ == '__main__':
    try:
        node_a()
    except rospy.ROSInterruptException:
        pass
