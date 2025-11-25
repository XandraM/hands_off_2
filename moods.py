import tuke_openlab
from threading import Thread
from tuke_openlab.lights import Color
import time

env = tuke_openlab.production_env()
openlab = tuke_openlab.Controller(env)

# -----------------------------
# GLOBAL CONTROL FLAG
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
# NEW SEQUENTIAL EFFECT
# -----------------------------
def seq_all_rows(palette, start, end, is_running):
    while is_running():
        for color in palette:
            if not is_running():
                return

            # ideme od start po end
            for led_id in range(start, end + 1):
                if not is_running():
                    return
                openlab.lights.set_color(led_id, color)
                time.sleep(0.08)  # rýchlosť prechodu


# -----------------------------
# EFFECT FUNCTIONS (updated)
# -----------------------------
def run_spring_pulse(openlab, is_running):
    t1 = Thread(target=seq_all_rows, args=(spring_palette, 1, 27, is_running))
    t2 = Thread(target=seq_all_rows, args=(spring_palette, 28, 54, is_running))
    t3 = Thread(target=seq_all_rows, args=(spring_palette, 55, 81, is_running))
    t1.start(); t2.start(); t3.start()
    t1.join(); t2.join(); t3.join()


def run_summer_pulse(openlab, is_running):
    t1 = Thread(target=seq_all_rows, args=(summer_palette, 1, 27, is_running))
    t2 = Thread(target=seq_all_rows, args=(summer_palette, 28, 54, is_running))
    t3 = Thread(target=seq_all_rows, args=(summer_palette, 55, 81, is_running))
    t1.start(); t2.start(); t3.start()
    t1.join(); t2.join(); t3.join()


def run_autumn_pulse(openlab, is_running):
    t1 = Thread(target=seq_all_rows, args=(autumn_palette, 1, 27, is_running))
    t2 = Thread(target=seq_all_rows, args=(autumn_palette, 28, 54, is_running))
    t3 = Thread(target=seq_all_rows, args=(autumn_palette, 55, 81, is_running))
    t1.start(); t2.start(); t3.start()
    t1.join(); t2.join(); t3.join()


def run_winter_pulse(openlab, is_running):
    t1 = Thread(target=seq_all_rows, args=(winter_palette, 1, 27, is_running))
    t2 = Thread(target=seq_all_rows, args=(winter_palette, 28, 54, is_running))
    t3 = Thread(target=seq_all_rows, args=(winter_palette, 55, 81, is_running))
    t1.start(); t2.start(); t3.start()
    t1.join(); t2.join(); t3.join()


# default mode
def day_mood():
    openlab.lights.set_all(Color(204, 255, 255))
