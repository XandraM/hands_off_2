import time

# globálny prepínač zapnutia efektov
_enabled = False

def set_enabled(val: bool):
    global _enabled
    _enabled = val

# jednoduché farby ako tuple (R, G, B)
# OpenLab akceptuje aj tuple
SPRING = (255, 120, 180)
SUMMER = (255, 255, 0)
AUTUMN = (255, 100, 0)
WINTER = (150, 200, 255)
DAY = (255, 255, 255)

# všetky efekty pracujú rovnako:
# stále dookola nastavujú farbu
# a čakajú 0.1 sekundy
def pulse(openlab, color):
    while _enabled:
        openlab.lights.set_color(color)
        time.sleep(0.1)


# --- jednotlivé módy (iba zabalíme pulse s farbou) ---

def run_spring_pulse():
    from main import openlab
    pulse(openlab, SPRING)

def run_summer_pulse():
    from main import openlab
    pulse(openlab, SUMMER)

def run_autumn_pulse():
    from main import openlab
    pulse(openlab, AUTUMN)

def run_winter_pulse():
    from main import openlab
    pulse(openlab, WINTER)

def day_mood():
    from main import openlab
    openlab.lights.set_color(DAY)
