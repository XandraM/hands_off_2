import threading
import tuke_openlab
from tuke_openlab import lights
from tuke_openlab.lights import Color
import random



spring_palette = [
    Color(r=200, g=255, b=200),   # mint green
    Color(r=255, g=220, b=240),   # soft pink
    Color(r=255, g=255, b=180),   # spring yellow
]

summer_palette = [
    Color(r=0, g=200, b=255),     # turquoise
    Color(r=255, g=255, b=0),     # sun yellow
    Color(r=0, g=120, b=255),     # sea blue
]

autumn_palette = [
    Color(r=255, g=140, b=0),     # orange
    Color(r=180, g=60, b=20),     # dark amber
    Color(r=255, g=80, b=20),     # pumpkin
]

winter_palette = [
    Color(r=180, g=220, b=255),   # icy blue
    Color(r=220, g=240, b=255),   # cold white
    Color(r=120, g=180, b=255),   # winter sky
]

def spring_mood():
