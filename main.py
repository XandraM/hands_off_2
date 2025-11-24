import threading
import tuke_openlab
from moods import (
    run_effect, set_enabled, is_enabled
)

openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("mg383jw"))

# -----------------------------
# GLOBAL THREADS
# -----------------------------
current_thread = None
current_thread_audio = None

def set_current_audio(play_obj):
    global current_thread_audio
    current_thread_audio = play_obj

# -----------------------------
# STOP FUNCTION
# -----------------------------
def stop_effect():
    global current_thread
    set_enabled(False)
    openlab.lights.turn_off()

    if current_thread and current_thread.is_alive():
        current_thread.join(timeout=0.1)

    # Stop audio
    global current_thread_audio
    if current_thread_audio is not None and current_thread_audio.is_playing():
        current_thread_audio.stop()
        current_thread_audio = None

    current_thread = None
    set_enabled(True)  # pripravené na nový efekt

# -----------------------------
# RUN NEW EFFECT
# -----------------------------
def start_new_effect(palette, audio_file):
    global current_thread
    stop_effect()  # zastaví predchádzajúci efekt
    current_thread = threading.Thread(target=lambda: run_effect(palette, audio_file))
    current_thread.start()

# -----------------------------
# SPEECH HANDLER
# -----------------------------
def on_speech(text: str):
    text = text.lower().strip()

    if text in ["koniec", "stop"]:
        stop_effect()
    elif text == "jar":
        start_new_effect(moods.spring_palette, "jar.mp3")
    elif text == "leto":
        start_new_effect(moods.summer_palette, "leto.mp3")
    elif text == "jeseň":
        start_new_effect(moods.autumn_palette, "jesen.mp3")
    elif text == "zima":
        start_new_effect(moods.winter_palette, "zima.mp3")
    elif text in ["deň", "default"]:
        stop_effect()
        openlab.lights.set_all(tuke_openlab.lights.Color(204,255,255))

# -----------------------------
# ACTIVATE VOICE RECOGNITION
# -----------------------------
openlab.voice_recognition.on_recognized(on_speech)

# -----------------------------
# KEEP RUNNING
# -----------------------------
while True:
    pass
