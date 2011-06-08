#!/usr/bin/env python
'''
Unit testing module for emotion_generator.Marvin.

'''
import copy
import os
import unittest
import sys

from emotion_generator import Marvin

from irobot_create_2_1.msg import SensorPacket
from irobot_marvin.msg import EmotionalState

class KnownValues(unittest.TestCase):
    '''Test some important known values with Marvin's reation.'''

    # TODO: Create some known values to test

    def testSensorDeltasKnownValues(self):
        changed_state = copy.copy(Marvin.quiet_state)
        changed_state.batteryCapacity += .5
        deltas = dict(Marvin.deltas(Marvin.quiet_state, changed_state))
        # TODO: Test known values here
        assert deltas['batteryCapacity'] == .5

    def testUpdateEmotionsKnownValues(self):
        marvin = Marvin()
        assert marvin.emotions is None
        changed_state = Marvin.quiet_state
        marvin.updateEmotions(changed_state)
        assert marvin.emotions is Marvin.start_emotions
        # TODO: Test known values here

if __name__ == '__main__':
    unittest.main()

