import tuke_openlab
from threading import Thread
from tuke_openlab.lights import Color
import time

lights_enabled = True

spring_palette = [Color(200, 255, 200), Color(255, 220, 240), Color(255, 255, 180)]
summer_palette = [Color(0, 200, 255), Color(255, 255, 0), Color(0, 120, 255)]
autumn_palette = [Color(255, 140, 0), Color(180, 60, 20), Color(255, 80, 20)]
winter_palette = [Color(180, 220, 255), Color(220, 240, 255), Color(120, 180, 255)]

def set_enabled(value: bool):
    global lights_enabled
    lights_enabled = value

def is_enabled():
    return lights_enabled

def pulse_all_rows(openlab, palette, start, end):
    global lights_enabled
    for color in palette:
        if not lights_enabled:
            return
        for i in range(start, end + 1):
            if not lights_enabled:
                return
            openlab.lights.set_color(i, color)
            time.sleep(0.2)

def run_spring_pulse(openlab):
    Thread(target=pulse_all_rows, args=(openlab, spring_palette, 1, 27)).start()
    Thread(target=pulse_all_rows, args=(openlab, spring_palette, 28, 54)).start()
    Thread(target=pulse_all_rows, args=(openlab, spring_palette, 55, 81)).start()

def run_summer_pulse(openlab):
    Thread(target=pulse_all_rows, args=(openlab, summer_palette, 1, 27)).start()
    Thread(target=pulse_all_rows, args=(openlab, summer_palette, 28, 54)).start()
    Thread(target=pulse_all_rows, args=(openlab, summer_palette, 55, 81)).start()

def run_autumn_pulse(openlab):
    Thread(target=pulse_all_rows, args=(openlab, autumn_palette, 1, 27)).start()
    Thread(target=pulse_all_rows, args=(openlab, autumn_palette, 28, 54)).start()
    Thread(target=pulse_all_rows, args=(openlab, autumn_palette, 55, 81)).start()

def run_winter_pulse(openlab):
    Thread(target=pulse_all_rows, args=(openlab, winter_palette, 1, 27)).start()
    Thread(target=pulse_all_rows, args=(openlab, winter_palette, 28, 54)).start()
    Thread(target=pulse_all_rows, args=(openlab, winter_palette, 55, 81)).start()

def day_mood(openlab):
    openlab.lights.set_all(Color(204, 255, 255))
