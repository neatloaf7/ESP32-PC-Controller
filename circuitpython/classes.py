import displayio
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.triangle import Triangle
import vectorio

class Background:
    def __init__(self):
        bitmap = displayio.Bitmap(320, 240, 1)
        palette = displayio.Palette(1)
        palette[0] = 0x212121
        self.background = displayio.TileGrid(bitmap, pixel_shader=palette)

class MediaButton(displayio.Group):
    def __init__(self, x, y, button):

        super().__init__(x=x, y=y)

        self.button = button

        if button == "play":
            self.circle = vectorio.Circle(r=25, fill=0xb3b3b3)
            self.triangle = 

