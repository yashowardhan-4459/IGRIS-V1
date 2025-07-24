# soul.py

from body.auth import retina_scan
from body.ears import listen_for_command
from body.voice import speak
from body.senses import detect_wake_word
from body.hands import execute_command
from body.spine import handle_system_action

import time

def soul():
    speak("IGRIS is online, awaiting your command.")

    while True:
        print("Listening for wake word...")
        if detect_wake_word():
            if retina_scan():  # Ensure it's only you
                speak("What is your command, master?")
                command = listen_for_command()

                if command:
                    if command in ["shutdown", "restart", "sleep"]:
                        handle_system_action(command)
                    else:
                        execute_command(command)
            else:
                speak("Access denied. Unauthorized user.")
                time.sleep(2)

if __name__ == "__main__":
    soul()
