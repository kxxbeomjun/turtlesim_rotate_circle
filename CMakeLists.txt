cmake_minimum_required(VERSION 3.0.2)
project(hw1_turtlesim)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  geometry_msgs
  roslaunch
)

roslaunch_add_file_check(launch)

add_message_files(
  FILES
  circularMotion.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)

find_package(Boost REQUIRED COMPONENTS system)


catkin_package(
  INCLUDE_DIRS include
  CATKIN_DEPENDS roscpp std_msgs
  DEPENDS system_lib
)
 
include_directories(
  ${catkin_INCLUDE_DIRS}
)
 

