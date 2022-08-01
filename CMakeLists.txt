cmake_minimum_required(VERSION 3.0.0)
project(ars_robot_models)

find_package(catkin REQUIRED COMPONENTS
)

catkin_package(
  DEPENDS
  CATKIN_DEPENDS
  INCLUDE_DIRS
  LIBRARIES
)

include_directories(
    ${catkin_INCLUDE_DIRS}
)
