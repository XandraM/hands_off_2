import time
from tuke_openlab.lights import Color

_enabled = False

def set_enabled(val: bool):
    global _enabled
    _enabled = val

def is_enabled():
    return _enabled

# triplets – presne tvoje zoradenie LED
triplets = [
    (1, 28, 55), (2, 29, 56), (3, 30, 57), (4, 31, 58), (5, 32, 59),
    (6, 33, 60), (7, 34, 61), (8, 35, 62), (9, 36, 63), (10, 37, 64),
    (11, 38, 65), (12, 39, 66), (13, 40, 67), (14, 41, 68), (15, 42, 69),
    (16, 43, 70), (17, 44, 71), (18, 45, 72), (19, 46, 73), (20, 47, 74),
    (21, 48, 75), (22, 49, 76), (23, 50, 77), (24, 51, 78), (25, 52, 79),
    (26, 53, 80), (27, 54, 81)
]

# farby
spring_palette = [Color(200,255,200)]
summer_palette = [Color(0,200,255)]
autumn_palette = [Color(255,140,0)]
winter_palette = [Color(180,220,255)]
DAY = Color(255,255,255)

# efekt, presne podľa tripletov
def move_triplets_in_order(openlab, palette):
    while is_enabled():
        for color in palette:
            if not is_enabled():
                openlab.lights.turn_off()
                return
            for trio in triplets:
                if not is_enabled():
                    openlab.lights.turn_off()
                    return
                openlab.lights.set_color(list(trio), color)
                time.sleep(0.15)

# módy
def run_spring_pulse(openlab, is_running): move_triplets_in_order(openlab, spring_palette)
def run_summer_pulse(openlab, is_running): move_triplets_in_order(openlab, summer_palette)
def run_autumn_pulse(openlab, is_running): move_triplets_in_order(openlab, autumn_palette)
def run_winter_pulse(openlab, is_running): move_triplets_in_order(openlab, winter_palette)
def day_mood(openlab): openlab.lights.set_all(DAY)
