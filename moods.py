import time
from threading import Thread
from tuke_openlab.lights import Color

# -----------------------------
# GLOBAL FLAG
# -----------------------------
lights_enabled = True

# -----------------------------
# PALETTES
# -----------------------------
spring_palette = [Color(200,255,200), Color(255,220,240), Color(255,255,180)]
summer_palette = [Color(0,200,255), Color(255,255,0), Color(0,120,255)]
autumn_palette = [Color(255,140,0), Color(180,60,20), Color(255,80,20)]
winter_palette = [Color(180,220,255), Color(220,240,255), Color(120,180,255)]

# -----------------------------
# FLAG CONTROL
# -----------------------------
def set_enabled(val: bool):
    global lights_enabled
    lights_enabled = val

def is_enabled():
    return lights_enabled

# -----------------------------
# LIGHT EFFECTS
# -----------------------------
def pulse_all_rows(openlab, palette, start, end, is_running):
    for color in palette:
        if not is_running():
            return
        for i in range(start, end+1):
            if not is_running():
                return
            openlab.lights.set_color(i, color)
            time.sleep(0.2)

def run_spring_pulse(openlab, is_running):
    threads = [
        Thread(target=pulse_all_rows, args=(openlab, spring_palette, 1, 27, is_running)),
        Thread(target=pulse_all_rows, args=(openlab, spring_palette, 28, 54, is_running)),
        Thread(target=pulse_all_rows, args=(openlab, spring_palette, 55, 81, is_running))
    ]
    for t in threads: t.start()
    for t in threads: t.join()

def run_summer_pulse(openlab, is_running):
    threads = [
        Thread(target=pulse_all_rows, args=(openlab, summer_palette, 1, 27, is_running)),
        Thread(target=pulse_all_rows, args=(openlab, summer_palette, 28, 54, is_running)),
        Thread(target=pulse_all_rows, args=(openlab, summer_palette, 55, 81, is_running))
    ]
    for t in threads: t.start()
    for t in threads: t.join()

def run_autumn_pulse(openlab, is_running):
    threads = [
        Thread(target=pulse_all_rows, args=(openlab, autumn_palette, 1, 27, is_running)),
        Thread(target=pulse_all_rows, args=(openlab, autumn_palette, 28, 54, is_running)),
        Thread(target=pulse_all_rows, args=(openlab, autumn_palette, 55, 81, is_running))
    ]
    for t in threads: t.start()
    for t in threads: t.join()

def run_winter_pulse(openlab, is_running):
    threads = [
        Thread(target=pulse_all_rows, args=(openlab, winter_palette, 1, 27, is_running)),
        Thread(target=pulse_all_rows, args=(openlab, winter_palette, 28, 54, is_running)),
        Thread(target=pulse_all_rows, args=(openlab, winter_palette, 55, 81, is_running))
    ]
    for t in threads: t.start()
    for t in threads: t.join()

# -----------------------------
# DEFAULT LIGHT MODE
# -----------------------------
def day_mood(openlab):
    openlab.lights.set_all(Color(204,255,255))
