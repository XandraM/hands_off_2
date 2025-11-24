import tuke_openlab
from threading import Thread
from tuke_openlab.lights import Color
import time

openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("mg383jw"))

# ---------------------------------------------------
# GLOBAL FLAG – bude sa nastavovať z main.py
# ---------------------------------------------------
lights_enabled = True

def set_enabled(value: bool):
    global lights_enabled
    lights_enabled = value

def is_enabled():
    return lights_enabled


# ---------------------------------------------------
# PALETTES
# ---------------------------------------------------
spring_palette = [
    Color(200, 255, 200),
    Color(255, 220, 240),
    Color(255, 255, 180),
]

summer_palette = [
    Color(0, 200, 255),
    Color(255, 255, 0),
    Color(0, 120, 255),
]

autumn_palette = [
    Color(255, 140, 0),
    Color(180, 60, 20),
    Color(255, 80, 20),
]

winter_palette = [
    Color(180, 220, 255),
    Color(220, 240, 255),
    Color(120, 180, 255),
]

# ---------------------------------------------------
# EFFECTS
# ---------------------------------------------------
def pulse_all_rows(palette, start, end):
    """Beží, kým je lights_enabled = True"""
    for color in palette:
        if not is_enabled():
            return
        for i in range(start, end + 1):
            if not is_enabled():
                return
            openlab.lights[i].set_color(color)  # <-- tu je oprava
            time.sleep(0.15)


def run_effect_for_palette(palette):
    """Spustí efekt paralelne pre všetky 3 riadky."""
    threads = [
        Thread(target=pulse_all_rows, args=(palette, 1, 27)),
        Thread(target=pulse_all_rows, args=(palette, 28, 54)),
        Thread(target=pulse_all_rows, args=(palette, 55, 81)),
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()


def run_spring_pulse():
    run_effect_for_palette(spring_palette)


def run_summer_pulse():
    run_effect_for_palette(summer_palette)


def run_autumn_pulse():
    run_effect_for_palette(autumn_palette)


def run_winter_pulse():
    run_effect_for_palette(winter_palette)


# DEFAULT
def day_mood():
    openlab.lights.set_all(Color(204, 255, 255))
