#!/usr/bin/env python2
#导包
import rospy
from ser_cli.srv import *
#回调函数
def answer(request):
    bool ans
    if request < 0.5 :
        ans = True
    else
        ans = False
    rospy.loginfo("收到： %f， 响应：%s", request, ans?"True":"False")
    return ans


if __name__ == "__main__":
    #初始化节点
    rospy.init_node("Server")
    #创建服务端对象
    Server = rospy.Service("number", Number, answer)
    rospy.loginfo("完成!")
    #处理
    
    rospy.spin()
    #s
    pass