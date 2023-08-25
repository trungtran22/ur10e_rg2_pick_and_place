# ur10e_rg2_pick_and_place
## Performing accurate pick-and-place with Ur10e and Onrobot RG2 gripper
## Python 2/3 - ROS Melodic - Ubuntu 18.04

**Cloning universal_robot:**
https://github.com/ros-industrial/universal_robot.git

**Cloning onrobot_rg2 gripper:**
https://github.com/Osaka-University-Harada-Laboratory/onrobot.git

Modifying URDF file (attach RG2 with Ur10e robot arm):
> Add meshes file of RG2 gripper and create joints with the Ur10e Robot Arm
>
> Additional: adding HEX torque sensor to the robot arm, access this link to download step file for HEX: https://onrobot.com/en/downloads?_gl=1*15scm0x*_ga*MTMzNDkxODE2Mi4xNjkyODYwMzgw*_up*MQ..
>
Create Ur10e attached with RG2 gripper package via Moveit Setup Assistant
>
![moveit_setup_assistant](http://docs.ros.org/en/melodic/api/moveit_tutorials/html/_images/setup_assistant_start.png)
>
After finishing creating the package, you will have the folder (for example: ur10e_moveit_config), remember to `catkin build`
>
Launching the package:
>
`roslaunch ur10e_rg2_moveit_config demo.launch`
>
![ur10e_rg2](https://github.com/trungtran22/ur10e_rg2_pick_and_place/blob/253399e7db206ef86994cccb9b2b6cb1e1eeb6b1/image/ur10e_rg2.png)



