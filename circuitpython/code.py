import board
import displayio
import digitalio
import busio
import fourwire
import neopixel
import adafruit_ili9341
import time
import adafruit_ft5336
import adafruit_register
import adafruit_focaltouch

displayio.release_displays()
pixel = neopixel.NeoPixel(board.IO42, 10)
pixel[0] = (255, 0, 0)
pixel.show()

spi = busio.SPI(board.IO12, board.IO11)
tft_cs = board.IO10
tft_rs = board.IO46
display_bus = fourwire.FourWire(spi, command=tft_rs, chip_select=tft_cs)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

backlight = digitalio.DigitalInOut(board.IO45)
backlight.direction = digitalio.Direction.OUTPUT
print("hello nigga")
backlight.value = True
pixel.deinit()

i2c = busio.I2C(board.IO15, board.IO16)
irq = digitalio.DigitalInOut(board.IO17)
irq.direction = digitalio.Direction.INPUT
irq.pull = digitalio.Pull.UP


touch = adafruit_focaltouch.Adafruit_FocalTouch(i2c)


while True:
    t = touch.touches
    print(t)
    print(time.monotonic())
    if t:
        print(f"x= {t[0]["x"]}")
    pass

