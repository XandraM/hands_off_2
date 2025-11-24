import time
import threading
from tuke_openlab import Controller
from tuke_openlab.lights import Color
from pydub import AudioSegment
import simpleaudio as sa

openlab = Controller(Controller.simulation_env("mg383jw"))

# -----------------------------
# GLOBAL FLAG
# -----------------------------
_enabled = True

def is_enabled():
    return _enabled

def set_enabled(value: bool):
    global _enabled
    _enabled = value

# -----------------------------
# PALETTES
# -----------------------------
spring_palette = [Color(200,255,200), Color(255,220,240), Color(255,255,180)]
summer_palette = [Color(0,200,255), Color(255,255,0), Color(0,120,255)]
autumn_palette = [Color(255,140,0), Color(180,60,20), Color(255,80,20)]
winter_palette = [Color(180,220,255), Color(220,240,255), Color(120,180,255)]

NUM_LIGHTS = 81

# -----------------------------
# LIGHTS EFFECT
# -----------------------------
def pulse_all_rows(palette):
    while is_enabled():
        for color in palette:
            if not is_enabled():
                return
            colors = [color for _ in range(NUM_LIGHTS)]
            openlab.lights.set(colors)
            time.sleep(0.15)

# -----------------------------
# AUDIO
# -----------------------------
def play_mp3(file_path):
    song = AudioSegment.from_file(file_path, format="mp3")
    play_obj = sa.play_buffer(
        song.raw_data,
        num_channels=song.channels,
        bytes_per_sample=song.sample_width,
        sample_rate=song.frame_rate
    )
    return play_obj

# -----------------------------
# RUN EFFECT (LIGHTS + SOUND)
# -----------------------------
def run_effect(palette, audio_file, current_audio_obj_ref):
    # Stop predchádzajúci zvuk
    if current_audio_obj_ref[0] is not None and current_audio_obj_ref[0].is_playing():
        current_audio_obj_ref[0].stop()

    # spusti zvuk
    play_obj = play_mp3(audio_file)
    current_audio_obj_ref[0] = play_obj

    # spusti svetlá
    pulse_all_rows(palette)

# -----------------------------
# DEFAULT MOOD
# -----------------------------
def day_mood():
    colors = [Color(204, 255, 255) for _ in range(NUM_LIGHTS)]
    openlab.lights.set(colors)
