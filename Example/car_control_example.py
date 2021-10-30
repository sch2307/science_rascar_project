from SR02 import SR02_Supersonic as Supersonic_Sensor

import front_wheels
import rear_wheels
import time

if __name__ == '__main__':
    try:
        # Example Of Front Servo Motor Control
        steering = front_wheels.Front_Wheels(db='config')
        steering.ready() #PWM 셋업

        steering.center_alignment() #핸들 중앙정렬
        time.sleep(1) #1초 스레드 슬립

        steering.turn_left() #왼쪽 조향
        steering.turn_right() #오른쪽 조향

        steering.turn(-15) #왼쪽 조향 / 앵글값(최대 조향각 35도)
        steering.turn(15) #오른쪽 조향 / 앵글값(최대 조향각 35도)

        # Example Of Real Motor Control
        accelerator = rear_wheels.Rear_Wheels(db='config')
        accelerator.ready() #PWM 셋업
        accelerator.go_forward(50) # 전진(50/100의 속도로)
        time.sleep(1)
        accelerator.stop() #모터 정지
        time.sleep(1)
        accelerator.go_backward(50) #후진(50/100의 속도로)
        time.sleep(1)

        accelerator.stop()
        accelerator.power_down()
        
        # Example of Ultrasonic Sensor
        distance_detector = Supersonic_Sensor.Supersonic_Sensor(17)

        for i in range(10):
            distance = distance_detector.get_distance()
            print("Distance is ", distance)
            time.sleep(1)
        
    except KeyboardInterrupt:
        accelerator.stop()
        accelerator.power_down()