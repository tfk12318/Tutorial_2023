#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import rospy
import random
from sub_cli.srv import *

def server_srv():
        #初始化节点
    rospy.init_node("server")
    #创建发布者对象
    ser = rospy.Service("random", Number, back)
    rospy.loginfo("完成！")
    rospy.spin()

def back(request):
    rospy.loginfo("收到：", request.number)
    return NumberResponse(a)    


if __name__ == "__main__":
    server_srv()

    #while not rospy.is_shutdown():
        #创建Number数据

        #赋值

        #