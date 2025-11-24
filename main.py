import tuke_openlab
from moods import *
import threading
import os
from playsound import playsound

openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("mg383jw"))
current_thread = None
sound_thread = None
sound_playing = False

# -----------------------------
# Zvuk
# -----------------------------
def play_sound_file(filename):
    global sound_playing
    if not os.path.exists(filename):
        print(f"Zvuk nenájdený: {filename}")
        return
    stop_sound()
    def sound_loop():
        global sound_playing
        sound_playing = True
        while sound_playing:
            playsound(filename)
    global sound_thread
    sound_thread = threading.Thread(target=sound_loop)
    sound_thread.start()

def stop_sound():
    global sound_playing
    sound_playing = False
    if sound_thread and sound_thread.is_alive():
        sound_thread.join(timeout=0.1)

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
        play_sound_file("jar.mp3")
        show_image("jar.png")
        start_new_effect(lambda: run_spring_pulse(openlab))

    elif text == "leto":
        play_sound_file("leto.mp3")
        show_image("leto.png")
        start_new_effect(lambda: run_summer_pulse(openlab))

    elif text in ["jeseň", "jesen"]:
        play_sound_file("jesen.mp3")
        show_image("jesen.png")
        start_new_effect(lambda: run_autumn_pulse(openlab))

    elif text == "zima":
        play_sound_file("zima.mp3")
        show_image("zima.png")
        start_new_effect(lambda: run_winter_pulse(openlab))

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
