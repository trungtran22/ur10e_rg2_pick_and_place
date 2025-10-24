# ur10e_rg2_pick_and_place
## Building model for Ur10e attached with Onrobot RG2 gripper and HEX Torque sensor
## Python 2/3 - ROS Noetic - Ubuntu 20.04

**Installation universal_robot package:**
https://github.com/ros-industrial/universal_robot.git

**Installation onrobot_rg2 gripper package:**
https://github.com/Osaka-University-Harada-Laboratory/onrobot.git

Modifying URDF file (attach RG2 with Ur10e robot arm):\
STL files of RG2 and HEX can be found [here](https://github.com/trungtran22/ur10e_rg2_pick_and_place/tree/main/ur10e_rg2_hex_tracik_moveit_config/description)\
\
**Step:**
- Modify UR10e URDF file: adding RG2 and HEX.

- Create Ur10e attached with RG2 gripper and HEX sensor package via Moveit Setup Assistant

![moveit_setup_assistant](http://docs.ros.org/en/melodic/api/moveit_tutorials/html/_images/setup_assistant_start.png)\


**Launching the package:**
>
`roslaunch ur10e_rg2_moveit_config demo.launch`
>
![ur10e_rg2](https://github.com/trungtran22/ur10e_rg2_pick_and_place/blob/253399e7db206ef86994cccb9b2b6cb1e1eeb6b1/image/ur10e_rg2.png)
>
**Perform Pick and Place in Rviz:**
>
`rosrun moveit_ur main.py`
>
>
**Demo Video:**

https://youtube.com/shorts/rOTPqwZyU7w?si=ZUvhbGPq-e-PDXsw

