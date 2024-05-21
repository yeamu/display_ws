import socket
import json

def rm(pos):
    host = '192.168.2.200'  # 修改为服务器的 IP 地址
    port = 8080  # 修改为服务器的端口号

    # 创建客户端套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    GET_CURRENT_ARM_STATE = {"command":"get_current_arm_state"}
    SET_CHANGE_TOOL_FRAME = {"command":"set_change_tool_frame","tool_name":"jaws"}
    

    try:
        # 连接到服务器
        client_socket.connect((host, port))
        print('成功连接到机械臂')

        # 设置工具坐标
        # client_socket.sendall(json.dumps(SET_CHANGE_TOOL_FRAME).encode('utf-8'))
        # a = client_socket.recv(1024)


        client_socket.sendall(json.dumps(pos).encode('utf-8'))

        res = json.loads(client_socket.recv(1024).decode())
        print('rm 收到点位 返回值：',res)

        if not res['trajectory_state']:
            print('该点位不可达，请检查点or机械臂工作系')
            return False

        # 获取机械臂状态
        client_socket.sendall(json.dumps(GET_CURRENT_ARM_STATE).encode('utf-8'))
        back = client_socket.recv(1024)
        print('收到机械臂返回值:', back.decode())
        
        return back

    except Exception as e:
        print('连接或接收数据时发生错误:',host, e)

    finally:
        # 关闭客户端套接字l
        client_socket.close()
    