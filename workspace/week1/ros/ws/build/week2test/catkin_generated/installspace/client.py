#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
#导入库
import rospy
import random
from week2test.srv import *

def client():
    rospy.init_node("asker")
    rospy.wait_for_service("get")
    try:
        random_number = random(0,1)
        service = rospy.ServiceProxy("get", Number)
        resp = service(random_number)
        print(random_number)
        if answer:
            print("Yes")
        else
            print("No")

if __name__ == "__main__":
    client()