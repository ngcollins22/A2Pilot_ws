#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("first_node")
        self.get_logger().info("Hello from ROS2") #write log


def main(args=None):
    rclpy.init(args=args) #always first line
    # my code goes in here

    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown() #always last line

if __name__ == '__main__':
    main()