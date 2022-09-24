import os
from deep_translator import GoogleTranslator
from subprocess import call
from time import sleep

def translateGoogle(): # Def to translate the text with Google translator
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear') # Command to clear the Consoles
    clearConsole()
    textquest = input('Bitte gebe den zu Übersetzenden Text ein: ')
    to_translate = textquest
    languageqe = input('In welche Sprache soll übersetzt werden?: ')


    translated = GoogleTranslator(source='auto', target=languageqe).translate(to_translate)
    print('')
    print(f'Die Übersetzung lautet: {translated}')
    print('')
    startpagequest2 = input('Möchtest du wieder auf die Startseite zurück? (j/n): ')
    
    # End of .py
    if startpagequest2 == 'j':
        clearConsole()
        call(['python', 'fasttrans.py'])
    if startpagequest2 == 'n':
        print('Das Programm wird sich in 3 Sekunden Automatisch beenden')
        sleep(3)
        quit()

# the Def for the other files to clear the console
def freshConsole():
    clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clear()