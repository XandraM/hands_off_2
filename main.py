import tuke_openlab
from moods import (
    run_spring_pulse, run_summer_pulse, run_autumn_pulse, run_winter_pulse,
    day_mood, set_enabled, is_enabled
)
import threading
import pygame
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
        print(f"Zvuk nenájdený: {filename}")
        return
    stop_sound()
    def _play():
        try:
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play(-1)  # loop
        except Exception as e:
            print("Chyba pri prehrávaní zvuku:", e)
    threading.Thread(target=_play, daemon=True).start()

def stop_sound():
    pygame.mixer.music.stop()

# -----------------------------
# Load and show image
# -----------------------------
def show_image(filename):
    if not os.path.exists(filename):
        print(f"Obrázok nenájdený: {filename}")
        return
    try:
        openlab.screens.show_image(filename)  # priamo súbor PNG
    except Exception as e:
        print("Chyba pri zobrazovaní obrázka:", e)

def clear_screen():
    try:
        openlab.screens.clear()
    except:
        pass

# -----------------------------
# Stop all effects
# -------------------------
