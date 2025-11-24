import threading
from moods import (
    run_effect, day_mood, set_enabled, is_enabled,
    spring_palette, summer_palette, autumn_palette, winter_palette
)

# uchováva aktuálne prehrávaný zvuk
current_audio_obj = [None]

# vlákno pre efekt
current_thread = None

# -----------------------------
# STOP EFFECT
# -----------------------------
def stop_effect():
    global current_thread
    set_enabled(False)  # zastav svetlá

    if current_audio_obj[0] is not None and current_audio_obj[0].is_playing():
        current_audio_obj[0].stop()

    if current_thread and current_thread.is_alive():
        current_thread.join(timeout=0.1)
    current_thread = None

# -----------------------------
# RUN NEW EFFECT
# -----------------------------
def start_new_effect(palette, audio_file):
    global current_thread
    stop_effect()
    set_enabled(True)

    current_thread = threading.Thread(target=run_effect, args=(palette, audio_file, current_audio_obj))
    current_thread.start()

# -----------------------------
# SPEECH HANDLER
# -----------------------------
def on_speech(text: str):
    text = text.lower().strip()
    if text in ["koniec", "stop"]:
        stop_effect()
        return
    elif text == "jar":
        start_new_effect(spring_palette, "jar.mp3")
    elif text == "leto":
        start_new_effect(summer_palette, "leto.mp3")
    elif text == "jeseň":
        start_new_effect(autumn_palette, "jesen.mp3")
    elif text == "zima":
        start_new_effect(winter_palette, "zima.mp3")
    elif text in ["deň", "default"]:
        stop_effect()
        day_mood()

# -----------------------------
# PRIPOJENIE SPEECH RECOGNITION
# -----------------------------
from tuke_openlab import Controller
openlab = Controller(Controller.simulation_env("mg383jw"))
openlab.voice_recognition.on_recognized(on_speech)

# -----------------------------
# KEEP PROGRAM RUNNING
# -----------------------------
while True:
    pass
