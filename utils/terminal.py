import os

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    elif os.getenv("TERM"):
        os.system("clear")