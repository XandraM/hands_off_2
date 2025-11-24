import tuke_openlab
from moods import (
    run_spring_pulse, run_summer_pulse, run_autumn_pulse, run_winter_pulse,
    day_mood, set_enabled, is_enabled
)
import threading
import base64

openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("mg383jw"))

# -------- CURRENT RUNNING THREAD ----------
current_thread = None


# -------------------------------------------
# LOAD IMAGE AS BASE64
# -------------------------------------------
def load_image_b64(filename):
    with open(filename, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


# -------------------------------------------
# SHOW IMAGE ON SCREEN
# -------------------------------------------
def show_image(filename):
    img_b64 = load_image_b64(filename)
    openlab.screens.show_image(img_b64)


# ---------------------------------------------------
# STOP FUNCTION – zastaví animáciu
# ---------------------------------------------------
def stop_effect():
    global current_thread
    set_enabled(False)
    openlab.lights.turn_off()

    if current_thread and current_thread.is_alive():
        current_thread.join(timeout=0.1)

    current_thread = None


# ---------------------------------------------------
# RUN NEW EFFECT SAFELY
# ---------------------------------------------------
def start_new_effect(target_fn):
    global current_thread

    stop_effect()
    set_enabled(True)

    current_thread = threading.Thread(target=target_fn)
    current_thread.start()


# ---------------------------------------------------
# SPEECH LOGIC
# ---------------------------------------------------
def on_speech(text: str):
    text = text.lower().strip()

    if text in ["koniec", "stop"]:
        stop_effect()
        openlab.screens.clear()
        return

    elif text == "jar":
        show_image("jar.png")
        start_new_effect(run_spring_pulse)

    elif text == "leto":
        show_image("leto.png")
        start_new_effect(run_summer_pulse)

    elif text == "jeseň":
        show_image("jesen.png")
        start_new_effect(run_autumn_pulse)

    elif text == "zima":
        show_image("zima.png")
        start_new_effect(run_winter_pulse)

    elif text == "deň" or text == "default":
        stop_effect()
        openlab.screens.clear()
        day_mood()


openlab.voice_recognition.on_recognized(on_speech)

# keep program running
while True:
    pass
