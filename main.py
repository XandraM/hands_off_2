import tuke_openlab
from moods import (
    run_spring_pulse, run_summer_pulse, run_autumn_pulse, run_winter_pulse,
    day_mood, set_enabled, is_enabled
)
import threading
import pygame
import base64
import os

# -----------------------------
# OpenLab controller
# -----------------------------
openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("mg383jw"))
current_thread = None

# -----------------------------
# Initialize Pygame for MP3
# -----------------------------
pygame.mixer.init()

def play_sound(filename):
    if not os.path.exists(filename):
        print(f"Zvukový súbor nenájdený: {filename}")
        return
    def _play():
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
    threading.Thread(target=_play, daemon=True).start()

def stop_sound():
    pygame.mixer.music.stop()

# -----------------------------
# Load and show image as Base64
# -----------------------------
def show_image(filename):
    if not os.path.exists(filename):
        print(f"Obrázok nenájdený: {filename}")
        return
    with open(filename, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
    # vymaže a zobrazí nový obrázok
    try:
        openlab.screens.show_static_image(img_b64)
    except Exception as e:
        print("Chyba pri zobrazovaní obrázka:", e)

# -----------------------------
# Stop all effects
# -----------------------------
def stop_effect():
    global current_thread
    set_enabled(False)
    openlab.lights.turn_off()
    try:
        openlab.screens.show_static_image("")  # vymaže obrazovku
    except:
        pass
    stop_sound()
    if current_thread and current_thread.is_alive():
        current_thread.join(timeout=0.1)
    current_thread = None

# -----------------------------
# Start new effect safely
# -----------------------------
def start_new_effect(target_fn):
    global current_thread
    stop_effect()
    set_enabled(True)
    current_thread = threading.Thread(target=target_fn)
    current_thread.start()

# -----------------------------
# Speech recognition callback
# -----------------------------
def on_speech(text: str):
    try:
        text = text.lower().strip()

        if text in ["koniec", "stop"]:
            stop_effect()
            return

        elif text == "jar":
            play_sound("jar.mp3")
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
            day_mood()

    except Exception as e:
        print("Chyba v on_speech:", e)

# -----------------------------
# Attach callback
# -----------------------------
openlab.voice_recognition.on_recognized(on_speech)

# -----------------------------
# Keep program running
# -----------------------------
while True:
    pass
