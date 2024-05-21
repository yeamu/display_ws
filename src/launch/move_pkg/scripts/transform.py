import math
import json


def transform(pos,flag):
    
    POS = {"command": "movej_p", "pose": [0, 0, 0, 0, 0, 0], "v": 16, "r": 0}
    # print(pos,type(pos),'xxxx')

    
    if flag == 'rm':
        newPose = json.loads(pos.decode('utf-8'))
        newPose = [x / 1000 for x in newPose['arm_state']["pose"]]
        # 弧度转角度
        newPose[3:] = [round(x * (180 / math.pi),3) for x in newPose[3:]]

        return ','.join(str(x) for x in newPose)
    
    elif flag == 'km':
        if isinstance(pos,str):
            newPose = pos.split(',')
            # 7位数值格式
            newPose = [float(x) for x in newPose[:-1]]
            # 6位数值格式
            # newPose = [float(x) for x in newPose]
            newPose[3:] = [round(x - 180,3) if x > 180 else x for x in newPose[3:]]

            # print(newPose)
            # 角度转弧度
            newPose[3:] = [float(x) for x in newPose[3:]]
            newPose[3:] = [round((x * (math.pi / 180)),3) for x in newPose[3:]]
            # newPose[3:] = [round((x * 2 * math.pi / 360),3) for x in newPose[3:]]
            newPose = [x * 1000 for x in newPose]
            POS['pose'] = newPose
            return POS
            
        else:
            print('kimage传回的值不是字符串')

# rm = {"arm_state":{"arm_err":0,"joint":[-88380,30859,87116,5173,51012,89791],"pose":[-30013,369779,88666,2950,-79,3130],"sys_err":0},"state":"current_arm_state"}
# km = '-307.632,-497.448,479.04,105.628,-38.926,-175.469,2'

# print(transform(km,'km'))