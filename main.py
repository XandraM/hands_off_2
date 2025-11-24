import tuke_openlab
from tuke_openlab.lights import Color
import time
from moods import run_spring_pulse, run_summer_pulse, run_winter_pulse, run_autumn_pulse, day_mood
from threading import Thread

openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("mg383jw"))

lights_enabled = True  # kontrola, či svetlá môžu bežať

def stop_lights():
    global lights_enabled
    lights_enabled = False
    openlab.lights.turn_off()

def run_pulse_with_stop(pulse_function):
    global lights_enabled
    lights_enabled = True
    pulse_function(openlab, lambda: lights_enabled)  # posielame vlákno kontrolu

def on_speech(text: str):
    global lights_enabled

    if text in ["stop", "koniec"]:
        stop_lights()
        return

    if text == "jar":
        Thread(target=run_pulse_with_stop, args=(run_spring_pulse,)).start()
    elif text == "leto":
        Thread(target=run_pulse_with_stop, args=(run_summer_pulse,)).start()
    elif text == "jeseň":
        Thread(target=run_pulse_with_stop, args=(run_autumn_pulse,)).start()
    elif text == "zima":
        Thread(target=run_pulse_with_stop, args=(run_winter_pulse,)).start()

openlab.voice_recognition.on_recognized(on_speech)

while True:
    time.sleep(0.1)
