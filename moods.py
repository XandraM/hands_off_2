import tuke_openlab
from threading import Thread
from tuke_openlab.lights import  Color
import time

openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("am720fg"))

spring_palette = [
    Color(r=200, g=255, b=200),   # mint green
    Color(r=255, g=220, b=240),   # soft pink
    Color(r=255, g=255, b=180),   # spring yellow
]

summer_palette = [
    Color(r=0, g=200, b=255),     # turquoise
    Color(r=255, g=255, b=0),     # sun yellow
    Color(r=0, g=120, b=255),     # sea blue
]

autumn_palette = [
    Color(r=255, g=140, b=0),     # orange
    Color(r=180, g=60, b=20),     # dark amber
    Color(r=255, g=80, b=20),     # pumpkin
]

winter_palette = [
    Color(r=180, g=220, b=255),   # icy blue
    Color(r=220, g=240, b=255),   # cold white
    Color(r=120, g=180, b=255),   # winter sky
]

ROWS = 3
COLUMNS = 27

def pulse(color, start, COLUMNS):
    pulse_length = 3
    openlab.lights.turn_off()
    black = Color()
    for i in range(start, COLUMNS+pulse_length+1):
        if i > pulse_length:
            # print(i)
            openlab.lights.set_color((i-pulse_length), black, 1500)
        if i <= COLUMNS:
            # print(i)
            openlab.lights.set_color(i, color, 500)
        time.sleep(0.1)
    # start += 27

def pulse_all_rows(palette, start, COLUMNS):


    # rows = {1, 28, 55}
    # for rows in range(3):
    #     for color in spring_palette:
    #         pulse(color)
    #         time.sleep(0.2)
    #start = 1
    #COLUMNS = 27
    #for row in range(3):
        for color in palette:
            pulse(color, start, COLUMNS)
        #start += 27
        #COLUMNS += 27
        time.sleep(0.25)



def run_spring_pulse(openlab):
    pulse_all_rows(spring_palette, 1, 27)
    # Thread(target=pulse_all_rows, args=(spring_palette,)).start()

def run_autumn_pulse(openlab):
    t1 =  Thread(target=pulse_all_rows, args=(autumn_palette, 1, 27))
    t2 = Thread(target=pulse_all_rows, args=(autumn_palette, 28, 54))
    t3 = Thread(target=pulse_all_rows, args=(autumn_palette, 55, 81))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()




def run_winter_pulse(openlab):
    Thread(target=pulse_all_rows, args=(winter_palette,1,27)).start()

def run_summer_pulse(openlab):
    Thread(target=pulse_all_rows, args=(summer_palette,1, 27)).start()


# default day

def day_mood():
    openlab.lights.set_all(Color(204, 255, 255))