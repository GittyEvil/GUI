#importerar moduler
import PySimpleGUI as sg

total = []
cash = 0
saldo = 1000
användarnamn=''
lösenord=''

#Detta är tänkt att vara en bank app där man kan skapa konto som ska lagras och kunna användas igen men även logga in och hantera sitt konto,
#där man kan sätta in och ta ut pengar samt kolla saldo.

#sparar användarnamn i txt fil som används för att logga in
def spara_användarnamn(användarnamn):
    with open('användarnamn.txt','a+', encoding=('utf-8')) as f:
        f.write(användarnamn)
        f.write("\n")
#sparar lösenordi txt fil som används för att logga in
def spara_lösenord(lösenord):
    with open('lösenord.txt','a+', encoding=('utf-8')) as f:
        f.write(lösenord)
        f.write("\n")

def läsa_användarnamn(användarnam):
    with open('användarnamn.txt','r',encoding=('utf-8')) as f:
        f.read(användarnam)
def läsa_lösenord(lösenord):
    with open('lösenord.txt','r',encoding=('utf-8')) as f:
        f.read(lösenord)


#theme för layout
sg.theme('dark blue')

#layout för själva appen
def bank_app():
    global saldo
    layout =  [
        [sg.Text('Bank app')],
        [sg.Button('1. sätta in pengar?',key=('-SET-'))],
        [sg.Input('',key=('-INPUT1-'))],
        [sg.Button('2. ta ut pengar?',key=('-TAKE-'))],
        [sg.Input('',key=('-INPUT2-'))],
        [sg.Button('3. se ditt saldo?',key=('-SALDO-'))],
        [sg.Text('Output:',key=('-OUTPUT-'))],
        [sg.Button('Submit'),sg.Button('Exit')]  
        ]

    #om jag inte stänger så håller den sig uppe
    window = sg.Window('Bank applikation',layout, margins=(100,100))

    #alla kommandon man kan göra
    while True:
        event, values = window.read()
        #passwords.konto()

        if event == sg.WIN_CLOSED:
            break
        if event == 'Exit':
            break

        #sätta in pengar
        if event == '-SET-':
            valuta=values['-INPUT1-']
            total.append(valuta)
            
            if valuta.isnumeric():
                output=valuta
                saldo=saldo+int(output)
                window['-OUTPUT-'].update(f'du har nu satt in {output}kr på ditt konto.')

        #kollar saldot på ett konto
        if event == '-SALDO-':
            window['-OUTPUT-'].update(f'du har {saldo} kr på ditt konto.')

        #ta ut pengar(scuffed atm)
        if event == '-TAKE-':
            ta_ut=values['-INPUT2-']
            total.append(ta_ut)

            if ta_ut.isnumeric():
                saldo=saldo-int(ta_ut)
                window['-OUTPUT-'].update(f'du har tagit ut {ta_ut} och du har kvar {saldo} på ditt konto.')
        if event == 'Logga in':
            inloggning()    
    window.close()  

#välja mellan skapa ett konto om du inte redan har ett eller direkt logga in
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
            inloggning()
        if event == 'Skapa konto':
            skapa_konto()
        layout.close()

#skapa ett konto innan du kan logga in
def skapa_konto():
    global användarnamn,lösenord
    skapa = [
        [sg.Text('Skapa ett konto för att kunna logga in.')],
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

        if event =='Submit':
            användarnamn=values['-ANVÄNDARE-']
            lösenord=values['-LÖSEN-']
            spara_användarnamn(användarnamn)
            spara_lösenord(lösenord)
            inloggning()
        return användarnamn, lösenord
    skapa.close()
 

#Logga in på ditt konto
def inloggning():
    global användarnamn,lösenord
    acc_layout = [
        [sg.Text('Användarnamn')],
        [sg.Input('',key=('-NAME-'))],
        [sg.Text('lösenord')],
        [sg.Input('',key=('-PASS-'))],
        [sg.Button('logga in'),sg.Button('Exit')]
    ]

    acc_layout = sg.Window('BankAppliktaion', acc_layout,margins=(100,100))

    while True:
        #läser av layouten för att logga in
        event,values = acc_layout.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Exit':
            break
        #om knappen tryckts och info stämmer öppnas bank appen
        if event == 'logga in' and values['-NAME-'] == användarnamn and values['-PASS-'] == lösenord:
            bank_app()
        elif event == 'logga in' and values['-NAME-'] != användarnamn or values['-PASS-'] != lösenord:
            sg.popup('Något gick fel försök igen')
            continue
    acc_layout.close()

#för att starta hela appen
logga_in_eller_skapa_konto()
#skapa_konto()