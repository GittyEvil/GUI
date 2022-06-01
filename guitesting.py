import PySimpleGUI as sg

def logga_in_eller_skapa_konto():

    layout = [
        [sg.Text('Logga in eller Skapa konto')],
        [sg.Button('Logga in'),sg.Button('Skapa konto')],
        [sg.Button('Exit')]
    ]

    layout = sg.Window('Skapa eller Logga in',layout,margins=(100,100))

    while True:
        event,values = layout.read()

        if event == sg.WIN_CLOSED:
            break
        if event == 'Exit':
            break
        if event == 'Logga in':
            pass
        if event == 'Skapa konto':
            pass
        
        layout.close()
logga_in_eller_skapa_konto()