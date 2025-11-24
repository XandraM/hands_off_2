import threading
from moods import *

current_thread = None

# STOP FUNCTION
def stop_effect():
    global current_thread
    set_enabled(False)
    openlab.lights.turn_off()
    if current_thread and current_thread.is_alive():
        current_thread.join(timeout=0.1)
    current_thread = None

# START NEW EFFECT
def start_new_effect(target_fn):
    global current_thread
    stop_effect()
    set_enabled(True)
    current_thread = threading.Thread(target=target_fn)
    current_thread.start()

# SPEECH LOGIC
def on_speech(text: str):
    text = text.lower().strip()
    if text in ["koniec", "stop"]:
        stop_effect()
        return
    elif text == "jar":
        start_new_effect(run_spring_pulse)
    elif text == "leto":
        start_new_effect(run_summer_pulse)
    elif text == "jeseň":
        start_new_effect(run_autumn_pulse)
    elif text == "zima":
        start_new_effect(run_winter_pulse)
    elif text in ["deň", "default"]:
        stop_effect()
        day_mood()

# VOICE RECOGNITION
openlab.voice_recognition.on_recognized(on_speech)

# KEEP PROGRAM RUNNING
while True:
    pass
