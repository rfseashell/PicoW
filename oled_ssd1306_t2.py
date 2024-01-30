#OLED连接至Pico W
from machine import SoftI2C, Pin
# 导进SSD1306驱动器控制模块
from ssd1306 import SSD1306_I2C
import time

if __name__ == '__main__':
    # 复位SoftI2C
    # OLED显示屏的scl联接到树莓派PICO的GPIO1, sda联接到GPIO0
    i2c = SoftI2C(scl=Pin(1), sda=Pin(0))
    # oled = SSD1306_I2C(width, height, i2c, addr)
    # width:显示屏宽
    # height: 显示屏高
    # i2c:已界定的I2C目标
    oled = SSD1306_I2C(128, 64, i2c) #OLED显示器复位：128*64屏幕分辨率,OLED的I2C详细地址是c03c
    # OLED表明的字符串数组，横坐标轴和纵轴
    while True:
        oled.text("Hello World!", 0, 0)
#         time.sleep(0.5)
        oled.text("1", 0, 16)
#         time.sleep(0.5)
        oled.text("2", 0, 24)
#         time.sleep(0.5)
        oled.text("3", 0, 32)
#         time.sleep(0.5)
        oled.text("4", 0, 40)
#         time.sleep(0.5)
        oled.text("5", 0, 48)
#         time.sleep(0.5)
        oled.text("0123456789ABCDEF", 0, 56)
#         time.sleep(0.5)
        
        # OLED表明
        oled.show()
#         time.sleep(1)
#         oled.clear()
