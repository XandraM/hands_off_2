import tuke_openlab
from threading import Thread
from tuke_openlab.lights import Color
import time

from moods import *

env = tuke_openlab.simulation_env("mg383jw")
# env= tuke_openlab.production_env()
openlab = tuke_openlab.Controller(env)

# Premenná bude pripojená na moods.lights_enabled
import moods


def stop_all():
    moods._enabled = False
    openlab.lights.turn_off()


def start_effect(effect_func):
    moods._enabled = True
    Thread(target=effect_func, args=(openlab, lambda: moods._enabled)).start()


def on_speech(text: str):
    text = text.lower()

    if text in ["stop", "koniec"]:
        stop_all()
        return

    if text == "jar":
        start_effect(run_spring_pulse)

    elif text == "leto":
        start_effect(run_summer_pulse)

    elif text == "jeseň" or text == "jesen":
        start_effect(run_autumn_pulse)

    elif text == "zima":
        start_effect(run_winter_pulse)

# env.mqtt.publish("openlab/audio", {"say": "Vyber si ročné obdobie"})
env.mqtt.subscribe_to("openlab/voice/recognition", on_speech)

openlab.voice_recognition.on_recognized(on_speech)

while True:
    time.sleep(0.1)
