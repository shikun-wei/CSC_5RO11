#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(f"Node C received: {msg.data}")
    new_message = msg.data + "C"
    pub.publish(new_message)
    rospy.loginfo(f"Node C sending: {new_message}")

def node_c():
    rospy.init_node('node_C')
    global pub
    pub = rospy.Publisher('outgoing_C', String, queue_size=10)
    sub = rospy.Subscriber('incoming_C', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        node_c()
    except rospy.ROSInterruptException:
        pass
