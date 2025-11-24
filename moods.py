import threading
import time
import simpleaudio as sa
from tuke_openlab.lights import Color
import tuke_openlab

# -----------------------------
# GLOBAL FLAGS
# -----------------------------
lights_enabled = True

# -----------------------------
# PALETTES
# -----------------------------
spring_palette = [
    Color(r=200, g=255, b=200),
    Color(r=255, g=220, b=240),
    Color(r=255, g=255, b=180),
]

summer_palette = [
    Color(r=0, g=200, b=255),
    Color(r=255, g=255, b=0),
    Color(r=0, g=120, b=255),
]

autumn_palette = [
    Color(r=255, g=140, b=0),
    Color(r=180, g=60, b=20),
    Color(r=255, g=80, b=20),
]

winter_palette = [
    Color(r=180, g=220, b=255),
    Color(r=220, g=240, b=255),
    Color(r=120, g=180, b=255),
]

# -----------------------------
# CONTROL FUNCTIONS
# -----------------------------
def set_enabled(value: bool):
    global lights_enabled
    lights_enabled = value

def is_enabled():
    return lights_enabled

# -----------------------------
# LIGHT EFFECTS
# -----------------------------
def pulse_all_rows(palette, start, end, is_running, openlab):
    for color in palette:
        if not is_running():
            return
        for i in range(start, end + 1):
            if not is_running():
                return
            openlab.lights[i].set_color(color)
            time.sleep(0.2)

def run_spring_pulse(openlab):
    t1 = threading.Thread(target=pulse_all_rows, args=(spring_palette, 1, 27, is_enabled, openlab))
    t2 = threading.Thread(target=pulse_all_rows, args=(spring_palette, 28, 54, is_enabled, openlab))
    t3 = threading.Thread(target=pulse_all_rows, args=(spring_palette, 55, 81, is_enabled, openlab))
    t1.start(); t2.start(); t3.start()
    t1.join(); t2.join(); t3.join()

def run_summer_pulse(openlab):
    t1 = threading.Thread(target=pulse_all_rows, args=(summer_palette, 1, 27, is_enabled, openlab))
    t2 = threading.Thread(target=pulse_all_rows, args=(summer_palette, 28, 54, is_enabled, openlab))
    t3 = threading.Thread(target=pulse_all_rows, args=(summer_palette, 55, 81, is_enabled, openlab))
    t1.start(); t2.start(); t3.start()
    t1.join(); t2.join(); t3.join()

def run_autumn_pulse(openlab):
    t1 = threading.Thread(target=pulse_all_rows, args=(autumn_palette, 1, 27, is_enabled, openlab))
    t2 = threading.Thread(target=pulse_all_rows, args=(autumn_palette, 28, 54, is_enabled, openlab))
    t3 = threading.Thread(target=pulse_all_rows, args=(autumn_palette, 55, 81, is_enabled, openlab))
    t1.start(); t2.start(); t3.start()
    t1.join(); t2.join(); t3.join()

def run_winter_pulse(openlab):
    t1 = threading.Thread(target=pulse_all_rows, args=(winter_palette, 1, 27, is_enabled, openlab))
    t2 = threading.Thread(target=pulse_all_rows, args=(winter_palette, 28, 54, is_enabled, openlab))
    t3 = threading.Thread(target=pulse_all_rows, args=(winter_palette, 55, 81, is_enabled, openlab))
    t1.start(); t2.start(); t3.start()
    t1.join(); t2.join(); t3.join()

# -----------------------------
# DEFAULT DAY LIGHTS
# -----------------------------
def day_mood(openlab):
    openlab.lights.set_all(Color(204, 255, 255))
