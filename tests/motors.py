import time

def motor_1_test(conveyor_1):
    print("rotating counter clockwise")
    conveyor_1.rotate_ccw(1000)
    print("motor sequence xxx")
    conveyor_1.disable()
    print("rotating clockwise")
    conveyor_1.rotate_cw(1000)
    conveyor_1.enable()
    time.sleep(3)   
    print("rotating clockwise take 2")
    conveyor_1.rotate_cw(1000)
    conveyor_1.disable()
    print("motor sequence disabled")

def motor_2_test(conveyor_2):
    print("rotating counter clockwise")
    conveyor_2.rotate_ccw(1000)
    print("motor sequence xxx")
    conveyor_2.disable()
    print("rotating clockwise")
    conveyor_2.rotate_cw(1000)
    conveyor_2.enable()
    time.sleep(3)   
    print("rotating clockwise take 2")
    conveyor_2.rotate_cw(1000)
    conveyor_2.disable()
    print("motor sequence disabled")