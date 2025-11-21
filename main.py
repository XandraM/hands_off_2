import sys
import tuke_openlab
from tuke_openlab import lights
from tuke_openlab.lights import Color
import time

# lights
openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("am720fg"))
# or production:
# openlab = tuke_openlab.Controller(tuke_openlab.production_env())

running = True

def red_lights():
    openlab.lights.turn_on()
    openlab.lights.set_all(Color(255,0,0,0))
    time.sleep(5)
    openlab.lights.turn_off()

def exit_lights():

    openlab.lights.turn_off()

def on_speech(text: str):
    # stopping the program
    if text == "stop" or text == "koniec":
        sys.exit(0)

    elif text == "jar":
        openlab.sound.say("jar")

openlab.voice_recognition.on_recognized(on_speech)

while running:
    pass