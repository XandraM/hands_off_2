import time
import threading
from tuke_openlab import Controller
from tuke_openlab.lights import Color
import simpleaudio as sa
from pydub import AudioSegment

# GLOBAL FLAG
_enabled = True
def is_enabled():
    return _enabled
def set_enabled(value: bool):
    global _enabled
    _enabled = value

# PALETTES
spring_palette = [Color(200,255,200), Color(255,220,240), Color(255,255,180)]
summer_palette = [Color(0,200,255), Color(255,255,0), Color(0,120,255)]
autumn_palette = [Color(255,140,0), Color(180,60,20), Color(255,80,20)]
winter_palette = [Color(180,220,255), Color(220,240,255), Color(120,180,255)]

# AUDIO
def play_mp3(file_path):
    """Spustí MP3 a vráti objekt, ktorý sa dá zastaviť"""
    song = AudioSegment.from_file(file_path, format="mp3")
    play_obj = sa.play_buffer(
        song.raw_data,
        num_channels=song.channels,
        bytes_per_sample=song.sample_width,
        sample_rate=song.frame_rate
    )
    return play_obj

# LIGHTS
def pulse_all_rows(openlab, palette):
    """Prebehne svetlá 3x3 radenie, ukončí sa pri set_enabled(False)"""
    for color in palette:
        if not is_enabled():
            return
        for i in range(1, 82):  # OpenLab má 81 svetiel
            if not is_enabled():
                return
            openlab.lights[i].color = color
            time.sleep(0.15)

# EFFECTS
def run_effect(openlab, palette, audio_file, audio_ref):
    # Stop predchádzajúci zvuk
    if audio_ref[0] is not None and audio_ref[0].is_playing():
        audio_ref[0].stop()

    set_enabled(True)
    audio_ref[0] = play_mp3(audio_file)
    pulse_all_rows(openlab, palette)

def day_mood(openlab):
    set_enabled(False)
    openlab.lights.set_all(Color(204,255,255))
