import tuke_openlab
from tuke_openlab import lights
from tuke_openlab.lights import Color

# lights
openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("am720fg"))
# or production:
# openlab = tuke_openlab.Controller(tuke_openlab.production_env())

def red_lights():
    openlab.lights.turn_on()
    openlab.lights.set_color(Color(255,0,0,0))
    openlab.lights.turn_off()

def on_speech(text: str):
    if text == "červená" or text == "red":
        openlab.lights.set_color(Color(255,0,0,0))

openlab.voice_recognition.on_recognized(on_speech)
