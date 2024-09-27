from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration


keyboard_to_joy_config = (
    get_package_share_directory("keyboard") + "/config/example_config.yaml"
)

def generate_launch_description():
    config_file_name = LaunchConfiguration("config_file_name")
    config_file_name_arg = DeclareLaunchArgument(
        "config_file_name",
        default_value=keyboard_to_joy_config,
        description="Path to the config file",
    )

    keyboard_to_joy_node = Node(
        namespace="foot_pedal_state",
        package="keyboard",
        executable="keyboard_to_joy.py",
        output="screen",
        parameters=[
            {"config_file_name": config_file_name},
        ],
    )
    keyboard_node = Node(
        package="keyboard",
        executable="keyboard",
        output="screen",
    )


    return LaunchDescription(
        [
            config_file_name_arg,
            keyboard_to_joy_node,
            keyboard_node,
        ]
    )
