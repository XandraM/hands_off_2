import tuke_openlab
import threading
from moods import *

import pygame
import os

# -----------------------------
# OpenLab controller
# -----------------------------
openlab = Controller(tuke_openlab.simulation_env("mg383jw"))
current_thread = None

# -----------------------------
# Initialize Pygame for MP3
# -----------------------------
pygame.mixer.init()

def play_sound(filename):
    """Spustí MP3 súbor na samostatnom vlákne"""
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
# Stop all effects
# -----------------------------
def stop_effect():
    global current_thread
    set_enabled(False)
    openlab.lights.turn_off()
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
            start_new_effect(run_spring_pulse)

        elif text == "leto":
            play_sound("leto.mp3")
            start_new_effect(run_summer_pulse)

        elif text in ["jeseň", "jesen"]:
            play_sound("jesen.mp3")
            start_new_effect(run_autumn_pulse)

        elif text == "zima":
            play_sound("zima.mp3")
            start_new_effect(run_winter_pulse)

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
