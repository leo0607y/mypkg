from setuptools import find_packages, setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Reo Ymaguchi',
    maintainer_email='reochimaru@gmail.com',
    description='ROS2の基礎事項練習用',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main', #talker.pyのmain関数
            'listener = mypkg.listener:main',
        ],
    },
)
