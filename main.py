import tuke_openlab
from moods import (
    run_spring_pulse, run_summer_pulse, run_autumn_pulse, run_winter_pulse,
    day_mood, set_enabled, is_enabled
)
import threading
import simpleaudio as sa
import os

# -----------------------------
# OPENLAB CONTROLLER
# -----------------------------
openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("mg383jw"))

# -----------------------------
# GLOBAL THREADS
# -----------------------------
current_thread = None
sound_thread = None
sound_playing = False

# -----------------------------
# SOUND FUNCTIONS
# -----------------------------
def play_sound_file(filename):
    global sound_thread, sound_playing
    if not os.path.exists(filename):
        print(f"Zvuk nenájdený: {filename}")
        return

    stop_sound()  # zastaví predchádzajúci zvuk

    def sound_loop():
        global sound_playing
        sound_playing = True
        while sound_playing:
            wave_obj = sa.WaveObject.from_wave_file(filename)
            play_obj = wave_obj.play()
            play_obj.wait_done()

    sound_thread = threading.Thread(target=sound_loop)
    sound_thread.start()

def stop_sound():
    global sound_playing, sound_thread
    sound_playing = False
    if sound_thread and sound_thread.is_alive():
        sound_thread.join(timeout=0.1)

# -----------------------------
# IMAGE FUNCTION
# -----------------------------
def show_image(filename):
    path = f"images/{filename}"
    if not os.path.exists(path):
        print(f"Obrázok nenájdený: {filename}")
        return
    try:
        openlab.screens.show_static_image(path)
    except Exception as e:
        print(f"Chyba pri zobrazovaní obrázka: {e}")

# -----------------------------
# LIGHT EFFECT CONTROL
# -----------------------------
def stop_effect():
    global current_thread
    set_enabled(False)
    openlab.lights.turn_off()
    stop_sound()
    if current_thread and current_thread.is_alive():
        current_thread.join(timeout=0.1)
    current_thread = None

def start_new_effect(target_fn):
    global current_thread
    stop_effect()
    set_enabled(True)
    current_thread = threading.Thread(target=lambda: target_fn(openlab))
    current_thread.start()

# -----------------------------
# SPEECH RECOGNITION
# -----------------------------
def on_speech(text: str):
    text = text.lower().strip()

    if text in ["koniec", "stop"]:
        stop_effect()
        return

    elif text == "jar":
        play_sound_file("sounds/jar.wav")
        show_image("jar.png")
        start_new_effect(run_spring_pulse)

    elif text == "leto":
        play_sound_file("sounds/leto.wav")
        show_image("leto.png")
        start_new_effect(run_summer_pulse)

    elif text in ["jeseň", "jesen"]:
        play_sound_file("sounds/jesen.wav")
        show_image("jesen.png")
        start_new_effect(run_autumn_pulse)

    elif text == "zima":
        play_sound_file("sounds/zima.wav")
        show_image("zima.png")
        start_new_effect(run_winter_pulse)

    elif text in ["deň", "default"]:
        stop_effect()
        day_mood(openlab)

# -----------------------------
# REGISTER SPEECH HANDLER
# -----------------------------
openlab.voice_recognition.on_recognized(on_speech)

# -----------------------------
# KEEP PROGRAM RUNNING
# -----------------------------
while True:
    pass
