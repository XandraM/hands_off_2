import tuke_openlab
from moods import (
    run_spring_pulse, run_summer_pulse, run_autumn_pulse, run_winter_pulse,
    day_mood, set_enabled, is_enabled
)
import threading
import os

# -----------------------------
# OpenLab controller
# -----------------------------
openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("mg383jw"))
current_thread = None

# -----------------------------
# Zvuk
# -----------------------------
def play_sound(filename):
    if not os.path.exists(filename):
        print(f"Zvuk nenájdený: {filename}")
        return
    try:
        openlab.sounds.play_sound(filename, loop=True)
    except Exception as e:
        print("Chyba pri prehrávaní zvuku:", e)

def stop_sound():
    try:
        openlab.sounds.stop_all()
    except:
        pass

# -----------------------------
# Obrázky
# -----------------------------
def show_image(filename):
    if not os.path.exists(filename):
        print(f"Obrázok nenájdený: {filename}")
        return
    try:
        openlab.screens.show_image(filename)
    except Exception as e:
        print("Chyba pri zobrazovaní obrázka:", e)

def clear_screen():
    try:
        openlab.screens.clear()
    except:
        pass

# -----------------------------
# Stop všetkého
# -----------------------------
def stop_effect():
    global current_thread
    set_enabled(False)
    openlab.lights.turn_off()
    stop_sound()
    clear_screen()
    if current_thread and current_thread.is_alive():
        current_thread.join(timeout=0.1)
    current_thread = None

# -----------------------------
# Spusti novú animáciu bezpečne
# -----------------------------
def start_new_effect(target_fn):
    global current_thread
    stop_effect()
    set_enabled(True)
    current_thread = threading.Thread(target=target_fn)
    current_thread.start()

# -----------------------------
# Hlasové príkazy
# -----------------------------
def on_speech(text: str):
    text = text.lower().strip()

    if text in ["koniec", "stop"]:
        stop_effect()
        return

    elif text == "jar":
        play_sound("jar.mp3")     # alebo jar.wav
        show_image("jar.png")
        start_new_effect(lambda: run_spring_pulse(openlab, is_enabled))

    elif text == "leto":
        play_sound("leto.mp3")
        show_image("leto.png")
        start_new_effect(lambda: run_summer_pulse(openlab, is_enabled))

    elif text in ["jeseň", "jesen"]:
        play_sound("jesen.mp3")
        show_image("jesen.png")
        start_new_effect(lambda: run_autumn_pulse(openlab, is_enabled))

    elif text == "zima":
        play_sound("zima.mp3")
        show_image("zima.png")
        start_new_effect(lambda: run_winter_pulse(openlab, is_enabled))

    elif text in ["deň", "default"]:
        stop_effect()
        day_mood(openlab)

# -----------------------------
# Pripoj hlasové rozpoznávanie
# -----------------------------
openlab.voice_recognition.on_recognized(on_speech)

# -----------------------------
# Keep program running
# -----------------------------
while True:
    pass
