#importerar moduler
import PySimpleGUI as sg
import passwords

total = []
cash = 0
users = []
passwords = []


#theme för layout
sg.theme('dark blue')

#layout för själva appen
def bank_app():
    layout =  [
        [sg.Text('Bank app')],
        [sg.Button('1. sätta in pengar?',key=('-SET-'))],
        [sg.Input('',key=('-INPUT1-'))],
        [sg.Button('2. ta ut pengar?',key=('-TAKE-'))],
        [sg.Input('',key=('-INPUT2-'))],
        [sg.Button('3. se ditt saldo?',key=('-SALDO-'))],
        [sg.Text('Output:',key=('-OUTPUT-'))],
        [sg.Submit(),]  
        ]

    #om jag inte stänger så håller den sig uppe
    window = sg.Window('Bank applikation',layout, margins=(100,100))

    #alla kommandon man kan göra
    while True:
        event, values = window.read()
        #passwords.konto()

        if event == sg.WIN_CLOSED:
            break

        #sätta in pengar
        if event == '-SET-':
            valuta=values['-INPUT1-']
            total.append(valuta)
            

            if valuta.isnumeric():
                output=valuta
                window['-OUTPUT-'].update(f'du har nu satt in {output}kr på ditt konto.')

        #kollar saldot på ett konto
        if event == '-SALDO-':
            window['-OUTPUT-'].update(f'du har {total} kr på ditt konto.')

        #ta ut pengar(scuffed atm)
        if event == '-TAKE-':
            ta_ut=values['-INPUT2-']
            total.append(ta_ut)

            if ta_ut.isnumeric():
                total.remove(ta_ut)
                window['-OUTPUT-'].update(f'du har tagit ut {ta_ut} och du har kvar {total} på ditt konto.')
        if event == 'Logga in':
            inloggning()
            

#Logga in på ditt konto
def inloggning():
    acc_layout = [
        [sg.Text('Användarnamn')],
        [sg.Input('',key=('-NAME-'))],
        [sg.Text('lösenord')],
        [sg.Input('',key=('-PASS-'))],
        [sg.Button('logga in')]
    ]

    acc_layout = sg.Window('BankAppliktaion', acc_layout,margins=(100,100))
    #alla kommandon
    while True:
        #läser av layouten för att logga in
        event,values = acc_layout.read()
        if event == sg.WIN_CLOSED:
            break
        #om knappen tryckts öppnas bank appen
        if event == 'logga in':
            bank_app()
            
        #sparar användarnamn och lösen på ett snabbt sätt
        användarnamn=values['-NAME-']
        users.append(användarnamn)
        print(users)

        lösenord=values['-PASS-']
        passwords.append(lösenord)
        print(passwords)

#skapa ett konto innan du kan logga in
def skapa_konto():
    skapa = [
        [sg.Text('Välj användarnamn:'), sg.InputText('',key=('-ANVÄNDARE-'))],
        [sg.Text('Välj lösenord:'), sg.InputText('',key=('-LÖSEN-'))],
        [sg.Button('Submit'),sg.Button('Exit')]
    ]

    skapa = sg.Window('Skapa konto',skapa,margins=(100,100))
    while True:
        event,values = skapa.read()

        if event == sg.WIN_CLOSED:
            break
        if event == 'Exit':
            break
        
        

        
#inloggning()
skapa_konto()



