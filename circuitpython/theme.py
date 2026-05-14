import displayio

spotify_palette = displayio.Palette(5)
GRAY0 = 0xb3b3b3 #LIGHTEST
GRAY1 = 0x535353
GRAY2 = 0x212121 #DARKEST
BLACK = 0x121212 
GREEN = 0x1db954 #or 0x1ED760

spotify_palette[0] = GRAY0
spotify_palette[1] = GRAY1
spotify_palette[2] = GRAY2
spotify_palette[3] = BLACK
spotify_palette[4] = GREEN
