import serial
from time import sleep

# 配置串口
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=5,
    write_timeout=5,
)


def close():
  
    close_hex = bytes.fromhex('7b01020120492000c8F87d')
    ser.write(bytearray(close_hex))

    print("关闭夹具")
    sleep(1)
    # ser.close()

def open():
  
    open_hex = bytes.fromhex('7b01020020492000c8F97d')
    ser.write(bytearray(open_hex))
    # ser.close()
    print("打开夹具")
    sleep(1)

if __name__ == '__main__':
    # close()
    open()