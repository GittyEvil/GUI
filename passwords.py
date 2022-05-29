import PySimpleGUI as sg
import hashlib

from bankapplikation import bank_app

sg.theme('dark blue')

def konto():
    layout = [
        [sg.Text('Skriv ditt användarnamn:'),sg.Input(key='-USER-',do_not_clear=False,)],
        [sg.Text('Skriv ditt lösenord:',)],
        [sg.InputText('',key=('-PASS-'),password_char='*')],
        [sg.Button('Submit'),sg.Button('Exit')]
    ]

    inlogg_window = sg.Window('inlogg',layout, modal=True,margins=(100,100))

    def verifiera_lösen(lösenord):
        hash = '9d42b8d31e5ceef9bacd5d064be884128d403ec199b9c9b33ea94572c7688cbb'
        lösenord_utf = lösenord.encode('utf-8')
        lösenord_hash = hashlib.sha256(lösenord_utf).hexdigest()
        if hash == lösenord_hash:
            return True
        return False
        

    def verifiera_användare(användare):
        verifiera_användare=['adrianstude@gmail.com','johhny112@gmail.com','feten@gmail.com']
        if användare in verifiera_användare:
            return True
        return False


    while True:
        event,Values = inlogg_window.read()
        if event == 'Exit' or event == sg.WINDOW_CLOSED:
            exit()
        if event == 'Submit':
            användare = Values['-USER-']
            lösenord = Values['-PASS-']
            if verifiera_lösen(lösenord) and verifiera_användare(användare):
                bank_app()
            else:
                continue
        inlogg_window.close()
