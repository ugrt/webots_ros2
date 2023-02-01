"""webots_ros2 package setup file."""

from setuptools import setup


package_name = 'webots_ros2_turtlebot_ugrt'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/robot_launch.py']))
data_files.append(('share/' + package_name + '/resource', [
    'resource/turtlebot3_burger_example_map.pgm',
    'resource/turtlebot3_burger_example_map.yaml',
    'resource/turtlebot_webots.urdf',
    'resource/ros2control.yml'
]))

data_files.append(('share/' + package_name + '/world', [
    'world/turtlebot3_burger_example_ugrt.wbt'
]))

data_files.append(('share/' + package_name + '/protos', [
    'protos/TurtleBot3BurgerUGRT.proto'
]))

data_files.append(('share/' + package_name + '/protos/meshes', [
    'protos/meshes/wheel_shape.obj',
    'protos/meshes/zed2.stl'
]))

data_files.append(('share/' + package_name, ['package.xml']))


setup(
    name=package_name,
    version='2023.0.1',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    # author='Cyberbotics',
    # author_email='support@cyberbotics.com',
    author='University of Guelph Robotics',
    author_email='ugrt@uoguelph.ca',
    maintainer='University of Guelph Robotics',
    maintainer_email='ugrt@uoguelph.com',
    keywords=['ROS', 'Webots', 'Robot', 'Simulation', 'Examples'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='TurtleBot3 Burger robot ROS2 interface for Webots.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros']
    }
)
