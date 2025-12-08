import time
from tuke_openlab.lights import Color

_enabled = False

def set_enabled(val: bool):
    global _enabled
    _enabled = val

def is_enabled():
    return _enabled


triplets = [
    (1, 28, 55), (2, 29, 56), (3, 30, 57), (4, 31, 58), (5, 32, 59),
    (6, 33, 60), (7, 34, 61), (8, 35, 62), (9, 36, 63), (10, 37, 64),
    (11, 38, 65), (12, 39, 66), (13, 40, 67), (14, 41, 68), (15, 42, 69),
    (16, 43, 70), (17, 44, 71), (18, 45, 72), (19, 46, 73), (20, 47, 74),
    (21, 48, 75), (22, 49, 76), (23, 50, 77), (24, 51, 78), (25, 52, 79),
    (26, 53, 80), (27, 54, 81)
]

# COLOR palettes
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

DAY = Color(255, 255, 255)



# main effect — goes exactly in triplet order
def move_triplets_in_order(openlab, palette):
    n = len(palette)
    while is_enabled():
        for i, trio in enumerate(triplets):
            if not is_enabled():
                return
            color = palette[i % n]  # cyklus cez paletu
            openlab.lights.set_color(list(trio), color)
            time.sleep(0.25)  # rýchlosť animácie
        time.sleep(0.1)


# modes
def run_spring_pulse(openlab, is_running):
    move_triplets_in_order(openlab, spring_palette)

def run_summer_pulse(openlab, is_running):
    move_triplets_in_order(openlab, summer_palette)

def run_autumn_pulse(openlab, is_running):
    move_triplets_in_order(openlab, autumn_palette)

def run_winter_pulse(openlab, is_running):
    move_triplets_in_order(openlab, winter_palette)



def day_mood(openlab):
    openlab.lights.set_all(DAY)
