from kimage import camera,kimageBack
from rmrobot import rm
import jaws
import math
from time import sleep
from transform import transform



def crawl():

    # 最后拍照位
    # endpos = {"command":"movej_p","pose":[-208239,286,314959,3141,-2,-1570],"v":8,"r":0}
    endpos = {"command":"movej_p","pose":[-8563,266519,197725,3071,-46,-3127],"v":16,"r":0}
    place =  {"command":"movej_p","pose":[-9102,410318,-62881,3057,-31,3150],"v":8,"r":0}
    test = {"command":"movej_p","pose":[-5709,109555,555592,1616,20,3096],"v":8,"r":0}


    # 机械臂到拍照位
    bpose =  rm(endpos)

    # 发送信号通知相机拍照
    cpos = transform(bpose,'rm')
    print(cpos,type(cpos))
    active = transform(camera(cpos),'km')
    print('发给rm的点位：',active)

    if rm(active):
        jaws.close()
        rm(endpos)
        return True
    return False
    # f = {"command":"movej_p","pose":[-17652,456369,-83348,2968,-26,-3081],"v":8,"r":0}
    # rm(f)
    # jaws.open()
    # jaws.open()
    # 得到点位信息
    # pos = kimageBack()
    # 处理点位数据
 
    # 将姿态数据发给机械臂
    # rm(pos)
    # jaws.close()
    # jaws.open()
    # sleep(2)
    # rm(pos=placement)
if __name__ == '__main__':

    crawl()




            
        









    