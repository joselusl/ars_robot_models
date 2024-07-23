from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, GroupAction
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node

from ament_index_python import get_package_share_directory

import os

def generate_launch_description():
        
    urdf_file = os.path.join(
        get_package_share_directory('ars_robot_models'),
        'urdf',
        'dji_tello.urdf'
    )

    return LaunchDescription([
        
        DeclareLaunchArgument(
          'screen',
          default_value='screen',
          description='Output setting for the nodes'
        ),

        GroupAction(
          [
            Node(
                package='robot_state_publisher',
                executable='robot_state_publisher',
                name='robot_state_publisher',
                output=LaunchConfiguration('screen'),
                parameters=[{'robot_description': open(urdf_file).read()}]
            ),
            Node(
                package='joint_state_publisher',
                executable='joint_state_publisher',
                name='joint_state_publisher',
                output=LaunchConfiguration('screen'),
            ),
            ]
        )
    ])
