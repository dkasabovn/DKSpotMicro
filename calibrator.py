import board
import digitalio
import busio
from adafruit_servokit import ServoKit
import adafruit_motor.servo

i2c_bus = busio.I2C(board.SCL, board.SDA);
i2c_bus2 = busio.I2C(board.SCL_1, board.SDA_1);
kit = ServoKit(channels=16, i2c=i2c_bus)
kit2 = ServoKit(channels=16, i2c=i2c_bus2)

print("===HELP===")
print("c - Change port number")
print("b - Change board number")
print("d - Change power of current servo")
print("Any input other than the above will be interpreted as an angle")
print("===HELP===")

port = 0
board = True

while True:
    print("Board one" if board else "Board two")
    cin = input("Enter int to change angle, c to change port, d to change power, s to stop: ")
    if (cin == "c"):
        port = int(input("Input port number: "))
        print(f"Port is now {port}")
    elif (cin == "b"):
        board = not board
        print("Board changed")
    elif (cin == "d"):
        power = float(input(f"Enter power given to servo at port {port} [-1.0,1.0]: "))  
        if board:
            kit.servo[port].throttle = power
        else:
            kit2.servo[port].throttle = power
    elif (cin == "s"):
        break
    else:
        if board:
            kit.servo[port].angle = int(cin)
        else:
            kit2.servo[port].angle = int(cin)