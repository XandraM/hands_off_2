import time
import threading
from tuke_openlab import Controller
from tuke_openlab.lights import Color
import simpleaudio as sa

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
# LIGHT EFFECT
# ----------------------------------
def pulse_all_rows(openlab, palette, start, end):
    """Beží, kým je enabled = True"""
    for color in palette:
        if not is_enabled():
            return
        for i in range(start, end + 1):
            if not is_enabled():
                return
            openlab.lights[i].color = color  # správny spôsob pre OpenLab
            time.sleep(0.15)

# ----------------------------------
# AUDIO
# ----------------------------------
def play_wav(file_path, stop_event):
    """Prehrá WAV súbor a dá sa zastaviť cez stop_event"""
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    while play_obj.is_playing():
        if stop_event.is_set():
            play_obj.stop()
            break
        time.sleep(0.1)

# ----------------------------------
# EFFECT + SOUND TOGETHER
# ----------------------------------
def run_effect(openlab, palette, sound_file, stop_event):
    """Spustí svetlá a zvuk naraz"""
    # vlákno pre zvuk
    audio_thread = threading.Thread(target=play_wav, args=(sound_file, stop_event))
    audio_thread.start()

    # svetlá
    pulse_all_rows(openlab, palette, 1, 81)

    # po skončení zastav zvuk
    stop_event.set()
    audio_thread.join()

# ----------------------------------
# ROČNÉ OBDOBIA
# ----------------------------------
def run_spring(openlab, stop_event):
    run_effect(openlab, spring_palette, "jar.wav", stop_event)

def run_summer(openlab, stop_event):
    run_effect(openlab, summer_palette, "leto.wav", stop_event)

def run_autumn(openlab, stop_event):
    run_effect(openlab, autumn_palette, "jesen.wav", stop_event)

def run_winter(openlab, stop_event):
    run_effect(openlab, winter_palette, "zima.wav", stop_event)

def day_mood(openlab):
    """Default farba"""
    openlab.lights.set_all(Color(204, 255, 255))
