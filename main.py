from machine import Pin, I2C
import utime
from ssd1306 import SSD1306_I2C
import framebuf
import freesans20
import writer

WIDTH = 128
HEIGHT = 32
i2c = I2C(1, scl = Pin(27), sda = Pin(26), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

led_pin = Pin(25, Pin.OUT)
led_org = Pin(21, Pin.OUT)
led_grn = Pin(22, Pin.OUT)
relay1 = Pin(1, Pin.OPEN_DRAIN)
relay2 = Pin(2, Pin.OPEN_DRAIN)
relay3 = Pin(3, Pin.OPEN_DRAIN)
relay4 = Pin(4, Pin.OPEN_DRAIN)
relay5 = Pin(5, Pin.OPEN_DRAIN)
relay6 = Pin(6, Pin.OPEN_DRAIN)
relay7 = Pin(7, Pin.OPEN_DRAIN)
relay8 = Pin(8, Pin.OPEN_DRAIN)
btnpin1 = Pin(16, Pin.IN, Pin.PULL_UP)
btnpin2 = Pin(17, Pin.IN, Pin.PULL_UP)
btnpin3 = Pin(18, Pin.IN, Pin.PULL_UP)
btnpin4 = Pin(19, Pin.IN, Pin.PULL_UP)
btnpin5 = Pin(20, Pin.IN, Pin.PULL_UP)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)


print("I2C Address : "+hex(i2c.scan()[0]).upper())

oled.fill(0)
oled.text("Mike Saturday", 0, 0)
oled.text("Enterprises", 0, 8)
oled.show()

utime.sleep(1)

oled.fill(0)
oled.text("Pico reporting", 0, 0)
oled.text("for duty", 0, 8)
oled.show()
led_org.value(1)
utime.sleep(0.2)
led_org.value(0)
utime.sleep(0.2)
led_grn.value(1)
utime.sleep(0.2)
led_grn.value(0)
utime.sleep(0.2)
led_org.value(1)
utime.sleep(0.2)
led_org.value(0)

oled.fill(0)
oled.text("|               ",0,0)
oled.text("|               ",0,8)
oled.text("|               ",0,16)
oled.text("|               ",0,24)
oled.show()
while True:
    if btnpin1.value() == False:
        led_org.toggle()
        if led_org.value() == False:
            oled.fill_rect(0,16,8,16,0)
            oled.text("|               ",0,0)
            oled.text("|               ",0,8)
            oled.text("                ",0,16)
            oled.text("                ",0,24)
            oled.show()
        else:
            oled.fill_rect(0,0,8,16,0)
            oled.text("                ",0,0)
            oled.text("                ",0,8)
            oled.text("|               ",0,16)
            oled.text("|               ",0,24)
            oled.show()
            led_grn.toggle()

        utime.sleep(0.2)
    if btnpin2.value() == False:
        if led_org.value() == False:
            relay1.toggle()
            if relay1.value() == False:
                oled.fill_rect(7,0, 28, 16,1)
                oled.show()
            else:
                oled.fill_rect(7,0, 28, 16,0)
                oled.show()
            utime.sleep(0.2)
        else:
            relay2.toggle()
            if relay2.value() == False:
                oled.fill_rect(7,16, 28, 16,1)
                oled.show()
            else:
                oled.fill_rect(7,16, 28, 16,0)
                oled.show()
            utime.sleep(0.2)
    if btnpin3.value() == False:
        if led_org.value() == False:
            relay3.toggle()
            if relay3.value() == False:
                oled.fill_rect(37,0, 28, 16,1)
                oled.show()
            else:
                oled.fill_rect(37,0, 28, 16,0)
                oled.show()
            utime.sleep(0.2)
        else:
            relay4.toggle()
            if relay4.value() == False:
                oled.fill_rect(37,16, 28, 16,1)
                oled.show()
            else:
                oled.fill_rect(37,16, 28, 16,0)
                oled.show()
            utime.sleep(0.2)
    if btnpin4.value() == False:
        if led_org.value() == False:
            relay5.toggle()
            if relay5.value() == False:
                oled.fill_rect(67,0, 28, 16,1)
                oled.show()
            else:
                oled.fill_rect(67,0, 28, 16,0)
                oled.show()
            utime.sleep(0.2)
        else:
            relay6.toggle()
            if relay6.value() == False:
                oled.fill_rect(67,16, 28, 16,1)
                oled.show()
            else:
                oled.fill_rect(67,16, 28, 16,0)
                oled.show()
            utime.sleep(0.2)
    if btnpin5.value() == False:
        if led_org.value() == False:
            relay7.toggle()
            if relay7.value() == False:
                oled.fill_rect(97,0, 28, 16,1)
                oled.show()
            else:
                oled.fill_rect(97,0, 28, 16,0)
                oled.show()
            utime.sleep(0.2)
        else:
            reading = sensor_temp.read_u16() * conversion_factor
            temperature = 27 - (reading - 0.706)/0.001721
            font_writer = writer.Writer(oled, freesans20)
            font_writer.set_textpos(0, 0)
            font_writer.printstring(str(temperature))
            print(temperature)
            oled.show()
            utime.sleep(2)
            oled.fill(0)
            oled.show()
            
            