import shutil
import os


# cleans terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# horizontal alignment input on terminal
def center_input(input):
    terminal_width = shutil.get_terminal_size().columns
    padding = (terminal_width - len(input)) // 2
    centered_prompt = " " * padding + input
    return centered_prompt


# horizontal alignment strings on terminal
def print_center(text):
    terminal_width = shutil.get_terminal_size().columns
    lines = text.split("\n")
    for line in lines:
        padding = (terminal_width - len(line)) // 2
        print(" " * padding + line)
