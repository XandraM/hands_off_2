import tuke_openlab
from threading import Thread
from tuke_openlab.lights import Color
import time

openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("mg383jw"))

# -----------------------------
# GLOBAL CONTROL FLAG
# -----------------------------
lights_enabled = True

def set_enabled(state: bool):
    global lights_enabled
    lights_enabled = state

def is_enabled():
    return lights_enabled

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
# EFFECT FUNCTIONS
# -----------------------------
def pulse_all_rows(palette, start, end):
    while is_enabled():
        for color in palette:
            if not is_enabled():
                return
            for i in range(start, end + 1):
                if not is_enabled():
                    return
                openlab.lights.set_color(i, color)
            time.sleep(0.2)


def run_spring_pulse():
    threads = [
        Thread(target=pulse_all_rows, args=(spring_palette, 1, 27)),
        Thread(target=pulse_all_rows, args=(spring_palette, 28, 54)),
        Thread(target=pulse_all_rows, args=(spring_palette, 55, 81)),
    ]
    for t in threads: t.start()
    for t in threads: t.join()


def run_summer_pulse():
    threads = [
        Thread(target=pulse_all_rows, args=(summer_palette, 1, 27)),
        Thread(target=pulse_all_rows, args=(summer_palette, 28, 54)),
        Thread(target=pulse_all_rows, args=(summer_palette, 55, 81)),
    ]
    for t in threads: t.start()
    for t in threads: t.join()


def run_autumn_pulse():
    threads = [
        Thread(target=pulse_all_rows, args=(autumn_palette, 1, 27)),
        Thread(target=pulse_all_rows, args=(autumn_palette, 28, 54)),
        Thread(target=pulse_all_rows, args=(autumn_palette, 55, 81)),
    ]
    for t in threads: t.start()
    for t in threads: t.join()


def run_winter_pulse():
    threads = [
        Thread(target=pulse_all_rows, args=(winter_palette, 1, 27)),
        Thread(target=pulse_all_rows, args=(winter_palette, 28, 54)),
        Thread(target=pulse_all_rows, args=(winter_palette, 55, 81)),
    ]
    for t in threads: t.start()
    for t in threads: t.join()


# Default mode
def day_mood():
    openlab.lights.set_all(Color(204, 255, 255))
