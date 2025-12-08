import time
import threading
from moods import *
import tuke_openlab

from moods import *

# env = tuke_openlab.simulation_env("mg383jw")
env= tuke_openlab.production_env()
openlab = tuke_openlab.Controller(env)

import moods

current_thread = None

def stop_all():
    moods._enabled = False
    openlab.lights.turn_off()
    if current_thread and current_thread.is_alive():
        current_thread.join(timeout=0.1)
    current_thread = None

def start_effect(effect_func):
    moods._enabled = False
    time.sleep(0.1)
    moods._enabled = True
    Thread(target=effect_func, args=(openlab, lambda: moods._enabled)).start()


def on_speech(text: str):
    text = text.lower().strip()
    if text in ["stop", "koniec"]:
        stop_effect()
        return

    if text == "jar":
        # stop_all()
        start_effect(run_spring_pulse)
    elif text == "leto":
        # stop_all()
        start_effect(run_summer_pulse)

    elif text == "jeseň" or text == "jesen":
        # stop_all()
        start_effect(run_autumn_pulse)
    elif text == "zima":
        # stop_all()
        start_effect(run_winter_pulse)
    elif text in ["deň","default"]:
        stop_effect()
        day_mood(openlab)

# env.mqtt.publish("openlab/audio", {"say": "Vyber si ročné obdobie"})
env.mqtt.subscribe_to("openlab/voice/recognition", on_speech)

openlab.voice_recognition.on_recognized(on_speech)

# keep alive
while True:
    time.sleep(0.1)