#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import rospy
import random
from sub_cli.srv import *

def client_srv():
    rospy.init_node("client")
    rospy.wait_for_service("random")
    client = rospy.ServiceProxy("random", Number)
    rosp = client(random.uniform(0, 1))
    rospy.loginfo("返回：%d", rosp.answer)
    #except rospy.ServiceExceptioin, e:
     #   rospy.logwarn("未收到服务!")


if __name__ == "__main__":
    client_srv()