from translate_google import freshConsole
from subprocess import call
from time import sleep

def ShowInfos(): # the def to show the informations about the program
    freshConsole()
    print("""
    Dieses Programm wurde erstellt von zlELo.

    Homepage zlELo: https://zlelo.github.io
    GitHub Account: https://github.com/zlELo

    Licens: GPL-2.0 Licens

    """)

    # End of .py
    startpagequest3 = input('Möchtest du wieder auf die Startseite zurück? (j/n): ')
    
    if startpagequest3 == 'j':
        freshConsole()
        call(['python', 'fasttrans.py'])
    if startpagequest3 == 'n':
        print('Das Programm wird sich in 3 Sekunden Automatisch beenden')
        sleep(3)
        quit()
