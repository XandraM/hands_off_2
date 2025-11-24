import tuke_openlab
from moods import (
    run_spring_pulse, run_summer_pulse, run_autumn_pulse, run_winter_pulse,
    day_mood, set_enabled, is_enabled
)
import threading

openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("mg383jw"))

# -------- CURRENT RUNNING THREAD ----------
current_thread = None


# ---------------------------------------------------
# STOP FUNCTION – zastaví animáciu
# ---------------------------------------------------
def stop_effect():
    global current_thread
    set_enabled(False)      # zastaviť slučky
    openlab.lights.turn_off()

    if current_thread and current_thread.is_alive():
        current_thread.join(timeout=0.1)

    current_thread = None


# ---------------------------------------------------
# RUN NEW EFFECT SAFELY
# ---------------------------------------------------
def start_new_effect(target_fn):
    global current_thread

    stop_effect()           # stop before starting new
    set_enabled(True)       # povoliť beh efektu

    current_thread = threading.Thread(target=target_fn)
    current_thread.start()


# ---------------------------------------------------
# SPEECH LOGIC
# ---------------------------------------------------
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

    elif text == "deň" or text == "default":
        stop_effect()
        day_mood()


openlab.voice_recognition.on_recognized(on_speech)

# keep program running
while True:
    pass
