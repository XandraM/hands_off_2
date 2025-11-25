# moods.py
import time

# -------------------------------------
# GLOBÁLNY PREPÍNAČ EFEKTOV
# -------------------------------------
_enabled = False

def set_enabled(val: bool):
    global _enabled
    _enabled = val

def is_enabled():
    return _enabled


# -------------------------------------
# FARBY (ako RGB tuple)
# -------------------------------------
SPRING = (255, 120, 180)
SUMMER = (255, 255, 0)
AUTUMN = (255, 100, 0)
WINTER = (150, 200, 255)
DAY = (255, 255, 255)

color_values = {
    "spring": SPRING,
    "summer": SUMMER,
    "autumn": AUTUMN,
    "winter": WINTER
}


# -------------------------------------
# ZÁKLADNÁ FUNKCIA: pulse
# -------------------------------------
def pulse(openlab, color):
    while is_enabled():
        openlab.lights.set_color(color)   # nastav všetky svetlá naraz
        time.sleep(0.1)


# -------------------------------------
# TVOJE NOVÉ PUTUJUCE SVETLO CEZ PANEL
# -------------------------------------
def move_light_across(openlab, color_name):
    triplets = [
        (1, 28, 55), (2, 29, 56), (3, 30, 57), (4, 31, 58), (5, 32, 59),
        (6, 33, 60), (7, 34, 61), (8, 35, 62), (9, 36, 63), (10, 37, 64),
        (11, 38, 65), (12, 39, 66), (13, 40, 67), (14, 41, 68), (15, 42, 69),
        (16, 43, 70), (17, 44, 71), (18, 45, 72), (19, 46, 73), (20, 47, 74),
        (21, 48, 75), (22, 49, 76), (23, 50, 77), (24, 51, 78), (25, 52, 79),
        (26, 53, 80), (27, 54, 81)
    ]

    for triplet in reversed(triplets):
        if not is_enabled():
            break

        # nastav len tieto 3 LED-ky
        openlab.lights.set_color(list(triplet), color_values[color_name])

        time.sleep(0.4)


# -------------------------------------
# REŽIMY – tieto voláš z main.py
# -------------------------------------
def run_spring_pulse(openlab):
    pulse(openlab, SPRING)

def run_summer_pulse(openlab):
    pulse(openlab, SUMMER)

def run_autumn_pulse(openlab):
    pulse(openlab, AUTUMN)

def run_winter_pulse(openlab):
    pulse(openlab, WINTER)

def run_spring_move(openlab):
    move_light_across(openlab, "spring")

def run_summer_move(openlab):
    move_light_across(openlab, "summer")

def run_autumn_move(openlab):
    move_light_across(openlab, "autumn")

def run_winter_move(openlab):
    move_light_across(openlab, "winter")

def day_mood(openlab):
    openlab.lights.set_color(DAY)
