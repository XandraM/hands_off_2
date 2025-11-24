import threading
from tuke_openlab import Controller
from moods import *
import time

openlab = Controller(Controller.simulation_env("mg383jw"))

current_thread = None
stop_event = threading.Event()

def stop_current_effect():
    global current_thread, stop_event
    set_enabled(False)
    stop_event.set()
    openlab.lights.turn_off()
    if current_thread and current_thread.is_alive():
        current_thread.join(timeout=0.1)
    current_thread = None
    stop_event.clear()  # pripravené na ďalšie spustenie
    set_enabled(True)

def start_new_effect(target_fn):
    global current_thread, stop_event
    stop_current_effect()
    stop_event.clear()
    set_enabled(True)
    current_thread = threading.Thread(target=target_fn, args=(openlab, stop_event))
    current_thread.start()

def on_speech(text: str):
    text = text.lower().strip()
    if text in ["koniec", "stop"]:
        stop_current_effect()
        return
    elif text == "jar":
        start_new_effect(run_spring)
    elif text == "leto":
        start_new_effect(run_summer)
    elif text == "jeseň":
        start_new_effect(run_autumn)
    elif text == "zima":
        start_new_effect(run_winter)
    elif text in ["deň", "default"]:
        stop_current_effect()
        day_mood(openlab)

# spusti rozpoznávanie hlasu
openlab.voice_recognition.on_recognized(on_speech)

# udrž program behom
while True:
    time.sleep(0.1)
