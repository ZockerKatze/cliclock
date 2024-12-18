import sys
import datetime
import os
import time
import shutil
from datetime import date
from colorama import Back, Fore, Style
import random
from pyfiglet import figlet_format
from termcolor import colored

levl_update_frequency = 3
time_format = '%H ⋮ %M ⋮ %S'
last_levl_update = time.time()
update_frequency = 1
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=12, cols=41))  # Resize terminal (yanked this from stackoverflow ofc :3)

rainbow_colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
timevar = str(date.today())

def rainbow_text(text):
    colored_text = ""
    for i, char in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        colored_text += colored(char, color)
    return colored_text

def sl():
    return random.randint(1, 100)

def get_levl_color(levl):
    if levl < 50:
        return Back.LIGHTGREEN_EX + Fore.BLACK
    elif 50 <= levl < 70:
        return Back.YELLOW + Fore.BLACK
    else:
        return Back.RED + Fore.BLACK

# Main Loop
levl = 0

while True:
    # Clear screen
    os.system('clear' if os.name == 'posix' else 'cls')
    
    terminal_width = shutil.get_terminal_size().columns
   
        #FIGLET TEXT

    time_string = datetime.datetime.now().strftime(time_format)
    figlet_string = figlet_format(time_string)
    colored_ascii = '\n'.join(rainbow_text(line) for line in figlet_string.split('\n'))
    centered_ascii = '\n'.join(line.center(terminal_width) for line in colored_ascii.split('\n'))
    
        # UPDATE LEVL VAR

    if time.time() - last_levl_update >= levl_update_frequency:
        levl = sl()
        last_levl_update = time.time()
    
    print(centered_ascii)
    print("Today is ➪ ", Back.LIGHTGREEN_EX + Fore.BLACK + timevar, Style.RESET_ALL + "\n")
   
        # LEVL VARIABLE PRINTING

    levl_color = get_levl_color(levl)
    print("Schizolevel -->", levl_color + f" {levl}% " + Style.RESET_ALL + "\n")
    
    time.sleep(update_frequency)
