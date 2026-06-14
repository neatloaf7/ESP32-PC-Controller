import board
import displayio
import digitalio
import busio
import fourwire
import neopixel
import adafruit_ili9341
import time
import adafruit_focaltouch
import terminalio
from adafruit_display_text import label

displayio.release_displays()
pixel = neopixel.NeoPixel(board.IO42, 1)
pixel[0] = (0, 255, 0)
pixel.show()

spi = busio.SPI(board.IO12, board.IO11)
tft_cs = board.IO10
tft_rs = board.IO46
display_bus = fourwire.FourWire(spi, command=tft_rs, chip_select=tft_cs)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

backlight = digitalio.DigitalInOut(board.IO45)
backlight.direction = digitalio.Direction.OUTPUT
backlight.value = True
#pixel.deinit()

i2c = busio.I2C(board.IO15, board.IO16)
irq = digitalio.DigitalInOut(board.IO17)
irq.direction = digitalio.Direction.INPUT
irq.pull = digitalio.Pull.UP


touch = adafruit_focaltouch.Adafruit_FocalTouch(i2c)
text = "hello world"
font = terminalio.FONT
color = 0xFFFFFF

text_area = label.Label(font, text=text, color=color)

text_area.x = 100
text_area.y = 100
display.root_group = text_area

#hello

while True:
    t = touch.touches
    if t:
        x = t[0]["y"]
        y = 239 - t[0]["x"]
        text_area.x = x
        text_area.y = y
        print(f"x= {t[0]["y"]}, y= {t[0]["x"]}")
    pass