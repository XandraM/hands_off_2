import tuke_openlab
from tuke_openlab import lights
from tuke_openlab.lights import Color
import time
from moods import run_spring_pulse, run_summer_pulse, run_winter_pulse, run_autumn_pulse, day_mood

# lights
openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("mg383jw"))
# or production:
# openlab = tuke_openlab.Controller(tuke_openlab.production_env())

running = True
default = True



def exit_lights():

    openlab.lights.turn_off()

def on_speech(text: str):
    # stopping the program
    if text == "stop" or text == "koniec":
        openlab.lights.turn_off()

    elif text == "jar":
        default = False
        run_spring_pulse(openlab)

    elif text == "leto":
        default = False
        run_summer_pulse(openlab)
        default = True

    elif text == "jeseň":
        default = False
        run_autumn_pulse(openlab)

    elif text == "zima":
        default = False
        run_winter_pulse(openlab)

openlab.voice_recognition.on_recognized(on_speech)

while running:
    pass