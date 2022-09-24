import os
from subprocess import call
from time import sleep
import json

def GoogleHelp():
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') # Command to clear the Consoles
    clearConsole()

    # JSON File for Languages
    f = open('data.json') #Open the JSON file
    data = json.load(f) # Load all of the JSON file

    for i in data['languages']: # Print all languages
        print(i)

    f.close()
    # End of JSON


    # End of .py
    startpagequest = input('Möchtest du wieder auf die Startseite zurück? (j/n): ')
    
    if startpagequest == 'j':
        clearConsole()
        call(['python', 'fasttrans.py'])
    if startpagequest == 'n':
        print('Das Programm wird sich in 3 Sekunden Automatisch beenden')
        sleep(3)
        quit()