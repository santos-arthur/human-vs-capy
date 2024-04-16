
import os
import pyaudio
from colorama import Fore, Back, Style
import modules.core.config as config_module
import numpy as np
import keyboard
import time

def clear():
    print(Fore.WHITE + Back.RESET)
    os.system('cls' if os.name=='nt' else 'clear')

def beep(frequency: int, duration: float):

    sample_rate = 44100

    configs = config_module.get_configs()
    volume = configs['volume']/100

    samples = (np.sin(2 * np.pi * np.arange(sample_rate * duration) * frequency / sample_rate)).astype(np.float32)

    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    stream.write(volume * samples)

    time.sleep(duration)

def press_any_key():
    print('Aperte qualquer tecla para continuar.')
    while True:
        keyPressed = keyboard.read_event(suppress=True)
        if keyPressed.event_type == keyboard.KEY_UP:
            beep(800, 0.2)
            break

def centered_text_padding(text: str, max_width: int = 48) -> str:
    if len(str(text)) > max_width:
        return ""
    return " " * int( int(max_width/2) - int(len(str(text))/2))

def centered_print(text: str, max_width: int = 48):
    text_padding = centered_text_padding(text, max_width)
    print(text_padding + text)


def split_into_lines(text: str, max_width: int) -> str:
    lines = []
    current_line = ''
    
    words = text.split()
    
    for word in words:
        # If the next word fits into the current line
        if len(current_line) + len(word) + 1 <= max_width:
            if current_line:  # If the current line is not empty, add a space before the next word
                current_line += ' '
            current_line += word
        else:
            # If it doesn't fit, add the current line to the list of lines and start a new line with the word
            lines.append(current_line)
            current_line = word
    
    # Add the last line
    lines.append(current_line)
    
    return lines

def game_banner():
    banner = open("resources/banner.txt", "r")
    print(banner.read())

def show_congratulations():    
    congrats = open("resources/congratulations.txt", "r")
    print(congrats.read())

def show_level_up():    
    level_up = open("resources/level_up.txt", "r")
    print(level_up.read())

def show_lose():    
    lose = open("resources/lose.txt", "r")
    print(lose.read())

def soldier():
    soldier = open("resources/soldier.txt", "r")
    print(soldier.read())