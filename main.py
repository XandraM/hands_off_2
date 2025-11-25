import time
import threading
from moods import *
import tuke_openlab

env = tuke_openlab.simulation_env("mg383jw")
openlab = tuke_openlab.Controller(env)

current_thread = None

def stop_effect():
    global current_thread
    set_enabled(False)
    openlab.lights.turn_off()
    if current_thread and current_thread.is_alive():
        current_thread.join(timeout=0.1)
    current_thread = None

def start_effect(effect_func):
    global current_thread
    stop_effect()               # stop predchádzajúci efekt
    set_enabled(True)
    current_thread = threading.Thread(target=effect_func, args=(openlab, lambda: _enabled))
    current_thread.start()

def on_speech(text: str):
    text = text.lower().strip()
    if text in ["stop", "koniec"]:
        stop_effect()
        return
    elif text == "jar":
        start_effect(run_spring_pulse)
    elif text == "leto":
        start_effect(run_summer_pulse)
    elif text in ["jeseň","jesen"]:
        start_effect(run_autumn_pulse)
    elif text == "zima":
        start_effect(run_winter_pulse)
    elif text in ["deň","default"]:
        stop_effect()
        day_mood(openlab)

# pripojenie hlasového rozpoznávania
openlab.voice_recognition.on_recognized(on_speech)

# keep alive
while True:
    time.sleep(0.1)
