import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/leo0607y/work/robo-sys/ros2_ws/src/mypkg/install/mypkg'
