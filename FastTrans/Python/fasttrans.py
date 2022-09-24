from google_help import *
from translate_google import *
from infos import *
from subprocess import call
from time import sleep


print("""

                            ████████████████████████████████████████████████████████████████
                            █▄─▄▄─██▀▄─██─▄▄▄▄█─▄─▄─█▀▀▀▀▀██─▄─▄─█▄─▄▄▀██▀▄─██▄─▀█▄─▄█─▄▄▄▄█
                            ██─▄████─▀─██▄▄▄▄─███─████████████─████─▄─▄██─▀─███─█▄▀─██▄▄▄▄─█
                            ▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▀▀▀▀▀▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀

Funktionen:

- Übersetze mit Google (command: übersetzen)
- Lasse dir alle möglichen Sprachen für den Google Übersetzer anzeigen (command: help)
- Informationen über das Programm (command: infos)

""")


letsstart = input('Was möchtest du tun?: ')

if letsstart == 'infos':
    ShowInfos() # Call the infos.py file and start the def of "ShowInfos()"
if letsstart == 'übersetzen':
    translateGoogle() # Call the translate_google.py file and start the def
if letsstart == 'help':
    GoogleHelp() # Call the goole_help.py file and start the def
else: # If the user input a false command he will come to this part
    print('Oh, es ist ein Fehler aufgetreten. Anscheinend wurde kein gültiger Befehl eingegeben... Probiers einfach nochmal')
    sleep(1.5)
    freshConsole()
    call(['python', 'fasttrans.py'])