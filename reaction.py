import RPi.GPIO as GPIO
import time
import random

game_light = 4
player_one_light = 14
player_two_light = 15
player_one_button = 10
player_two_button = 11

def setup_gpios():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(game_light, GPIO.OUT)

    GPIO.setup(player_one_light, GPIO.OUT)
    GPIO.setup(player_two_light, GPIO.OUT)

    GPIO.setup(player_one_button, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(player_two_button, GPIO.IN, GPIO.PUD_UP)

def turn_on_game_light():
    time.sleep(random.uniform(5, 10))
    GPIO.output(game_light, 1)

def game_loop():
    while True:
        turn_on_game_light()


