#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(f"Node B received: {msg.data}")
    new_message = msg.data + "B"
    pub.publish(new_message)
    rospy.loginfo(f"Node B sending: {new_message}")

def node_b():
    rospy.init_node('node_B')
    global pub
    pub = rospy.Publisher('outgoing_B', String, queue_size=10)
    sub = rospy.Subscriber('incoming_B', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        node_b()
    except rospy.ROSInterruptException:
        pass
