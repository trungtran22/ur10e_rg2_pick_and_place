#!/usr/bin/env python

##-----------------------------------------
## The main code of simple pick and place using Moveit
##----------------------------------------

from move_group_joint_state import MoveGroupPythonJointState
from gripper_on import rg2_publisher
def main():
    # Define run variable as class MoveGroupPythonJointState
    # to run the operation funtion in the class MoveGroupPythonJointState
    run = MoveGroupPythonJointState()
    # Define two char varibales as input for open and close operation
    # of the onrobot gripper
    open_gripper = 'o'
    closed_gripper = 'c'
    width = 510 # Open the gripper with 50 mm
    width_2 = 280

    # The operation:
    # Step 0: Goto Initial State
    run.go_to_initial_state()
    # Step 1: open the gripper
    # - Call publish_open function with variable char1 as input
    rg2_publisher(open_gripper)
    # Step2: Pick the object with dimension 50 mm
    run.go_to_pose_goal(0.5, 0.4, 0.5, 0.0, 1.0, 0.0, 0.0)
    run.go_to_pose_goal(0.5, 0.4, 0.33, 0.0, 1.0, 0.0, 0.0)
    rg2_publisher(width)
    # Step3: Move to the new place 
    run.go_to_pose_goal(0.5, 0.4, 0.5, 0.0, 1.0, 0.0, 0.0)
    run.go_to_pose_goal(0.5, 0.2, 0.5, 0.0, 1.0, 0.0, 0.0)
    # Step4: Place the object
    run.go_to_pose_goal(0.5, 0.2, 0.33, 0.0, 1.0, 0.0, 0.0)
    rg2_publisher(open_gripper)
    run.go_to_pose_goal(0.5, 0.2, 0.5, 0.0, 1.0, 0.0, 0.0)
    
if __name__ == "__main__":
    main()
