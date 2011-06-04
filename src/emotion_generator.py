#!/usr/bin/env python
import roslib; roslib.load_manifest('robot_emotions')
import rospy

# Import the EmotionalState message from robot_emotions/msg
from irobot_marvin.msg import EmotionalState

# Import the SensorPacket message from irobot_create_2_1/msg
from irobot_create_2_1.msg import SensorPacket

class Marvin:

    def __init__(self):
        pass

    def find_problem(self, sensorpacket):
        '''Define the callback that will be called when a new
        SensorPacket is received.  This callback is responsible
        for also *publishing* a new robot emotional state
        message, using some function of the sensorPacket data.

        '''
        # The robot is scared of higher voltages!
        scared_value = float(sensorpacket.voltage) / 65535.0
        # Form the new emotion message.
        msg = EmotionalState(
                happiness = 1.0,
                sadness = 0.0,
                angriness = 0.0,
                scaredness = scared_value,
                tenderness = 0.0,
                excitedness = 1.0,
                message = "bitch bitch bitch")
        # Publish the emotion state message.
        self._publisher.publish(msg)

    def listen(self, publisher):
        '''Define the listener function that installs the
        "callback" function and then just spins forever,
        not doing anything else except calling the callback
        on each new received SensorPacket message.

        '''
        self._publisher = publisher
        # Initialize the node with the name "emotion_node"
        rospy.init_node('emotion_node', anonymous=True)
        # Subscribe to the sensorPacket topic, calling
        # the "callback" function with each new packet.
        # lambda is a python builtin in function --
        # look at the python documentation to learn more
        rospy.Subscriber("sensorPacket",
                         SensorPacket,
                         self.find_problem)
        rospy.spin()

# This is called first.
if __name__ == '__main__':
    # Create a publisher object that publishes to the
    # "robot_emotions" topic, and it publishes a message
    # of type EmotionalState
    publisher = rospy.Publisher('robot_emotions', EmotionalState)
    marvin = Marvin()
    # Call the listener and never return
    marvin.listen(publisher)
