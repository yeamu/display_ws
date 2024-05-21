import socket

def camera(cpos):
    # kimage
    server_host = "192.168.2.188"
    server_port = 3000
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接到kimage server
    client_socket.connect((server_host, server_port))
    # 发送可以拍照
    client_socket.sendall('PP'.encode())
    bool = client_socket.recv(1024)
    client_socket.sendall(cpos.encode())

    try:
        
        while True:
            # 接收服务器发送的消息
            data = client_socket.recv(1024)

            if not data:
                break
            
            # 打印接收到的消息
            print("接收到Kimage服务器消息:",data)
            # print(data)
            # client_socket.sendall(bpose.encode())
            return data.decode('utf-8')
    except Exception as e:
        print("与服务器通信时发生错误:", str(e))
    finally:
        # 关闭客户端套接字
        client_socket.close()

def kimageBack():
    host = '192.168.2.100'
    port = 3001
    # 创建 TCP 服务器套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定主机和端口
    server_socket.bind((host, port))
    
    # 开始监听连接
    server_socket.listen(5)
    
    print(f"TCP 服务器已经启动，监听在 {host}:{port}")

    while True:
        # 等待客户端连接
        client_socket, client_address = server_socket.accept()
        print(f"收到来自 {client_address} 的连接")
        data = client_socket.recv(1024)
        print(data)
        # client_socket.close()
        # return data
        # 处理连接
        # handle_client(client_socket, client_address)

