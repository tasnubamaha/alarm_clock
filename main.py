from playsound import playsound
import time
import os
import platform


CLEAR_AND_RETURN = "\033[H" if platform.system() != 'Windows' else ''

def clear_screen():
    # Clear screen based on OS
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def alarm(seconds):
    time_elapsed = 0
    clear_screen()

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}", end='')

    # Make sure the audio file path is correct
    try:
        playsound("alarm.mp3")
    except Exception as e:
        print("\nError playing sound:", e)

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)

