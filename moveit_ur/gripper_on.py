#!/usr/bin/env python

import rospy
from onrobot_rg_control.msg import OnRobotRGOutput

def genCommand(char, command):
    """ Updates the command according to the input character.

        Args:
            char (str): set command service request message
            command (OnRobotRGOutput): command to be sent

        Returns:
            command: command message with parameters set
    """
    gtype = rospy.get_param('/onrobot/gripper', 'rg2')
    if gtype == 'rg2':
        max_force = 400
        max_width = 1100
    elif gtype == 'rg6':
        max_force = 1200
        max_width = 1600
    else:
        rospy.signal_shutdown(
            rospy.get_name() +
            ": Select the gripper type from rg2 or rg6.")

    if char == 'c':
        command.rGFR = 400
        command.rGWD = 40
        command.rCTR = 16
    elif char == 'o':
        command.rGFR = 400
        command.rGWD = max_width
        command.rCTR = 16
    else:
        # If the command entered is a int, assign this value to rGWD
        try:
            command.rGFR = 400
            command.rGWD = min(max_width, int(char))
            command.rCTR = 16
        except ValueError:
            pass

    return command

def rg2_publisher(char):
    """ Main loop which requests new commands and
        publish them on the OnRobotRGOutput topic.
    """
    pub = rospy.Publisher(
        'OnRobotRGOutput', OnRobotRGOutput, queue_size=1)
    command = OnRobotRGOutput()

    command = genCommand(char, command)
    pub.publish(command)
    rospy.sleep(0.1)


