import threading
import time
from tuke_openlab.lights import Color
from tuke_openlab import Controller
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio as play_audio  # prehrá MP3

openlab = Controller(Controller.simulation_env("mg383jw"))

# ----------------------------------
# GLOBAL FLAG
# ----------------------------------
_enabled = True

def is_enabled():
    return _enabled

def set_enabled(value: bool):
    global _enabled
    _enabled = value

# ----------------------------------
# PALETTES
# ----------------------------------
spring_palette = [Color(200,255,200), Color(255,220,240), Color(255,255,180)]
summer_palette = [Color(0,200,255), Color(255,255,0), Color(0,120,255)]
autumn_palette = [Color(255,140,0), Color(180,60,20), Color(255,80,20)]
winter_palette = [Color(180,220,255), Color(220,240,255), Color(120,180,255)]

# ----------------------------------
# EFFECTS
# ----------------------------------
def pulse_all_rows(palette, start, end):
    """Beží, kým je _enabled = True"""
    for color in palette:
        if not is_enabled():
            return
        for i in range(start, end + 1):
            if not is_enabled():
                return
            openlab.lights[i].set_color(color)
            time.sleep(0.15)

def run_effect(palette, audio_file):
    """Spustí svetlá + zvuk"""
    from main import current_thread_audio  # dynamicky sa ukončí predchádzajúci zvuk

    # Stop predchádzajúci zvuk
    if current_thread_audio is not None and current_thread_audio.is_playing():
        current_thread_audio.stop()

    # spusti zvuk
    song = AudioSegment.from_file(audio_file, format="mp3")
    play_obj = play_audio(song)
    from main import set_current_audio
    set_current_audio(play_obj)

    # spusti svetlá vo vlákne
    pulse_all_rows(palette, 1, 81)
