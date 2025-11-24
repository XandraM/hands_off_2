import threading
import time
from tuke_openlab import Controller, simulation_env
from moods import *

# ---------- OPENLAB ----------
env = simulation_env("mg383jw")  # simulované prostredie
openlab = Controller(env)

# CURRENT THREAD + AUDIO
current_thread = None
current_audio = [None]  # uloží sa AudioObject

# ---------- CONTROL FUNCTIONS ----------
def stop_effect():
    global current_thread
    set_enabled(False)
    openlab.lights.turn_off()
    if current_audio[0] is not None and current_audio[0].is_playing():
        current_audio[0].stop()
    if current_thread and current_thread.is_alive():
        current_thread.join(timeout=0.1)
    current_thread = None

def start_new_effect(target_fn, *args):
    global current_thread
    stop_effect()
    current_thread = threading.Thread(target=target_fn, args=args)
    current_thread.start()

# ---------- SPEECH HANDLER ----------
def on_speech(text: str):
    text = text.lower().strip()
    if text in ["koniec", "stop"]:
        stop_effect()
        return
    elif text == "jar":
        start_new_effect(run_effect, openlab, spring_palette, "jar.mp3", current_audio)
    elif text == "leto":
        start_new_effect(run_effect, openlab, summer_palette, "leto.mp3", current_audio)
    elif text == "jeseň":
        start_new_effect(run_effect, openlab, autumn_palette, "jesen.mp3", current_audio)
    elif text == "zima":
        start_new_effect(run_effect, openlab, winter_palette, "zima.mp3", current_audio)
    elif text in ["deň", "default"]:
        stop_effect()
        day_mood(openlab)

# ---------- VOICE RECOGNITION ----------
openlab.voice_recognition.on_recognized(on_speech)

# ---------- KEEP RUNNING ----------
while True:
    time.sleep(0.1)
