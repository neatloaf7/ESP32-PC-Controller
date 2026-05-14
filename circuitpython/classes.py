import displayio
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.triangle import Triangle
import vectorio
from theme import spotify_palette

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
            self.circle = vectorio.Circle(radius=25, 
                                          pixel_shader=spotify_palette, 
                                          color_index=0)
            
            points = [(x1,y1), (x2,y2), (x3,y3)]
            self.triangle = vectorio.Polygon(pixel_shader=spotify_palette,
                                             points=points,
                                             color_index=3)

