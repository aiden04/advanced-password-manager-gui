import PySimpleGUI as sg
import random
import array

f = open('passwords.txt', 'r')

passwords_txt = f.read()

MAX_LEN = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPCASE_CHARACHTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', ';', ':', ',', '<', '.', '>', '/', '?']

COMBINED_LIST = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACHTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACHTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbole = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbole

for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
    password = password + x

sg.theme('DefaultNoMoreNagging')

def generated():

    layout = [
    [sg.ProgressBar(1)],
    [sg.Text(f' - Your generated password is "{password}"')], 
    [sg.Text(' - Information Saved Under "passwords.txt"')],
    [sg.ProgressBar(1)],
    [sg.Button('Done')]]
    window = sg.Window('Password Generated!', layout, modal=False)
    choice = None

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Done':
            window.hide()
            main()

    window.close()
    
def saved():

    layout = [
    [sg.ProgressBar(1)],
    [sg.Text(' - Information saved under "passwords.txt"', key="new")],
    [sg.ProgressBar(1)],
    [sg.Button('Done')]]
    window = sg.Window('Password Saved!', layout, modal=False)
    choice = None

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Done':
            window.hide()
            main()
    window.close()

def open_window():

    layout = [[sg.Text("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░░░░░░
░██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗░░░░░░
░██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║░░░░░░
░██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║░░░░░░
░██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝░░░░░░
░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░░
░██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗░
░██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝░
░██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗░
░╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║░
░░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""", key="new")], 
    [sg.Text(' - Please enter your requested information below.')],
    [sg.ProgressBar(1, size =(63,1))],
    [sg.Text('Username', size =(10,1)), sg.Input('', key='Username')], 
    [sg.Text('Email', size =(10,1)), sg.Input('', key='Email')], 
    [sg.Text('Website', size =(10,1)), sg.Input('', key='Website')],
    [sg.ProgressBar(1, size =(63,1))],    
    [sg.Button('Done'), sg.Button('Main Menu')]]
    window = sg.Window("Password Generator", layout, modal=False)
    choice = None

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Main Menu':
            window.hide()
            main()
            
        if event == 'Done':
            
            userName = (values['Username'])
            email = (values['Email'])
            website = (values['Website'])
            
            file = open("passwords.txt", 'a')
            
            usrnm = "UserName: " + userName + "\n"
            mail = "Email: " + email + "\n"
            web = "Website: " + website + "\n"
            pwd = "Password: " + password + "\n"
    
            file.write("===============================================\n")
            file.write(usrnm)
            file.write(mail)
            file.write(pwd)
            file.write(web)
            file.write("===============================================\n")
            file.write("\n")
            file.close
            
            window.hide()
            generated()

    window.close()

def enter():
    layout = [[sg.Text("""    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░
░██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗░
░██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║░
░██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║░
░██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝░
░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░░
░░██████╗░█████╗░██╗░░░██╗██╗███╗░░██╗░██████╗░░░░░░░░░░░░░░░░░░░░░░░░░░
░██╔════╝██╔══██╗██║░░░██║██║████╗░██║██╔════╝░░░░░░░░░░░░░░░░░░░░░░░░░░
░╚█████╗░███████║╚██╗░██╔╝██║██╔██╗██║██║░░██╗░░░░░░░░░░░░░░░░░░░░░░░░░░
░░╚═══██╗██╔══██║░╚████╔╝░██║██║╚████║██║░░╚██╗░░░░░░░░░░░░░░░░░░░░░░░░░
░██████╔╝██║░░██║░░╚██╔╝░░██║██║░╚███║╚██████╔╝░░░░░░░░░░░░░░░░░░░░░░░░░
░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""", key="new")], 
    [sg.Text(' - Please enter the requested information below.')], 
    [sg.ProgressBar(1, size =(59,1))],
    [sg.Text('Username', size =(10,1)), sg.Input('', key='Username')], 
    [sg.Text('Email', size =(10,1)), sg.Input('', key='Email')], 
    [sg.Text('Password', size =(10,1)), sg.Input('', key='Password')], 
    [sg.Text('Website', size =(10,1)), sg.Input('', key='Website')], 
    [sg.ProgressBar(1, size =(59,1))],
    [sg.Button('Done'), sg.Button('Main Menu')]]
    window = sg.Window("Password Saver", layout, modal=False)
    choice = None

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Main Menu':
            window.hide()
            main()
        if event == "Done":
            
            UserName = (values['Username'])
            eMail = (values['Email'])
            PaSSword = (values['Password'])
            Website = (values['Website'])
            
            file = open('passwords.txt', 'a')
            
            usern = "Username: " + UserName + "\n"
            Email = "Email: " + eMail + "\n"
            pswd = "Password: " + PaSSword + "\n"
            webURL = "Website: " + Website + "\n"
            
            file.write("===============================================\n")
            file.write(usern)
            file.write(Email)
            file.write(pswd)
            file.write(webURL)
            file.write("===============================================\n")
            file.write("\n")
            file.close
            
            window.hide()
            saved()
            main()
        
    window.close()

def pass_list():
    
    layout = [
    [sg.Text('''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░██████╗░
░██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝░
░██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║╚█████╗░░
░██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║░╚═══██╗░
░██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝██████╔╝░
░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░╚═════╝░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')],
    [sg.ProgressBar(1, size =(66,1))],
    [sg.Text(passwords_txt)],
    [sg.ProgressBar(1, size =(66,1))],
    [sg.Button('Main Menu')]
    ]
    passwords = sg.Window('Password List!', layout, modal=False)
    choice = None

    while True:
        event, values = passwords.read()
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Main Menu':
            passwords.hide()
            main()

    passwords.close()

def Themes():
    layout = [
    [sg.Text('Theme Changer')],
    [sg.Text('Theme Name', size =(10,1)), sg.Input()],
    [sg.Button('Theme Previewer'), sg.Button('Change Theme'), sg.Button('Main Menu')]]
    
    Main = sg.Window('Theme Changer', layout, modal=False)
    
    while True:
        event, values = Main.read()
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Theme Previewer':
            sg.theme_previewer()
            Themes()
        if event == 'Change Theme':
            sg.theme(values[0])
            Main.hide()
            main()
        if event == 'Main Menu':
            Main.hide()
            main()
        Main.close()

def main():
    layout = [[sg.Text('''    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░░
░██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗░
░██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║░
░██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║░
░██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝░
░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░░░░░░░░░░░
░████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗░░░░░░░░░░
░██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝░░░░░░░░░░
░██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗░░░░░░░░░░
░██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║░░░░░░░░░░
░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')],
    [sg.ProgressBar(1, size =(59,1))],
    [sg.Text(' - Welcome to Advanced Password Manager GUI!')],
    [sg.Text(' - This password manager allows you to save your own passwords or get a generated password using pythons')],
    [sg.Text('generating tools.')],
    [sg.Text(' - Get started by selection one of the options below!')],
    [sg.Text(' - To updated Passwords page, you must restart Advanced Password Manager GUI.')],
    [sg.ProgressBar(1, size =(59,1))],
    [sg.Button('Generate Password'), sg.Button('Enter Password'), sg.Button('Passwords'), sg.Button('Change Theme'), sg.Button('Exit')]]
    window = sg.Window("Main Menu", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            exit()
        if event == "Generate Password":
            window.hide()
            open_window()
        if event == "Enter Password":
            window.hide()
            enter()
        if event == 'Passwords':
            window.hide()
            pass_list()
        if event == 'Change Theme':
            window.hide()
            Themes()
    window.close()



if __name__ == "__main__":

    main()
