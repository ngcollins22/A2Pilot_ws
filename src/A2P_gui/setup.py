from setuptools import find_packages, setup

package_name = 'A2P_gui'

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
    maintainer='root',
    maintainer_email='ncollins22@vt.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = A2P_gui.my_first_node:main",
            "draw_circle = A2P_gui.draw_circle:main",
            "twist_sub = A2P_gui.my_first_subscriber:main"
        ],
    },
)
