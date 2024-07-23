#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist #remember to add dependency to package.xml
from turtlesim.srv import SetPen
from functools import partial

class TwistSubscriberNode(Node):

    def __init__(self):
        super().__init__("twist_sub")
        self.twist_sub = self.create_subscription(Twist, "/turtle1/cmd_vel", self.twist_callback, 10)
        self.get_logger().info("sub node has been started")

    def twist_callback(self, msg: Twist):
        self.get_logger().info(str(msg))

    def call_service(self, x):
        client = self.create_client(SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service")

        request = SetPen.Request()
        request.r = x

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_service))

    def callback_service(self, future): #callback for when service replies
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service call failed: %r" % (e,))


def main(args=None):
    rclpy.init(args=args)

    node = TwistSubscriberNode()
    rclpy.spin(node)

    rclpy.shutdown()