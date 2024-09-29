#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(f"Node D received: {msg.data}")
    new_message = msg.data + "D"
    pub.publish(new_message)
    rospy.loginfo(f"Node D sending: {new_message}")

def node_d():
    rospy.init_node('node_D')
    global pub
    pub = rospy.Publisher('outgoing_D', String, queue_size=10)
    sub = rospy.Subscriber('incoming_D', String, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        node_d()
    except rospy.ROSInterruptException:
        pass
