import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=11, cols=35)) ##yanked from so!
import datetime
import os     
import time 
import shutil
from datetime import date # idk wtf
from colorama import Back , Fore , Style

try:
    from pyfiglet import figlet_format  
    from termcolor import colored
except ImportError:
    print('Error, modules pyfiglet and termcolor are required. Run: pip install pyfiglet termcolor')
    exit(1)

font_name = 'slant' 

time_format = '%H:%M:%S'

update_frequency = 1

rainbow_colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']


timevar = str(date.today())

def rainbow_text(text):
    colored_text = ""
    for i, char in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        colored_text += colored(char, color)
    return colored_text

while True:
    os.system('clear' if os.name == 'posix' else 'cls')
    terminal_width = shutil.get_terminal_size().columns
    time_string = datetime.datetime.now().strftime(time_format)
    figlet_string = figlet_format(time_string, font=font_name)
    
    colored_ascii = '\n'.join(rainbow_text(line) for line in figlet_string.split('\n'))
    centered_ascii = '\n'.join(line.center(terminal_width) for line in colored_ascii.split('\n'))
    
    print(centered_ascii)
    print("╠Heute ist ➪ ", Back.GREEN + Fore.BLACK + timevar, Style.RESET_ALL + "╣\n")
    print(Style.RESET_ALL)
    time.sleep(update_frequency)
