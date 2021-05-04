import PySimpleGUI as sg
import random
import array
import os, time
import subprocess
import sys
import logging
import os

ttk_style = 'calm'
sg.SetOptions(icon='Data/icon.ico')

c = open('Data/theme', 'r')
theme_var = c.read()

t = open('Data/output', 'r')
stationary = t.read()
g = open(stationary, 'r')
output = g.read()

clear = lambda: os.system('cls')

current_path = os.path.abspath('start.cmd')

clear()
print(f'console: theme = {theme_var}')

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

sg.theme(theme_var)

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
            print('console: EXIT CODE "sg.WIN_CLOSED"')
            exit()
        if event == 'Done':
            print('console: returning "main()"')
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
            print('console: EXIT CODE "sg.WIN_CLOSED"')
            exit()
        if event == 'Done':
            print('console: returning "main()"')
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
    [sg.Button('Done', use_ttk_buttons=True), sg.Button('Main Menu', use_ttk_buttons=True)]]
    window = sg.Window("Password Generator", layout, modal=False)
    choice = None

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            print('console: EXIT CODE "sg.WIN_CLOSED"')
            exit()
        if event == 'Main Menu':
            print('console: returning "main()"')
            window.hide()
            main()
            
        if event == 'Done':
        
            print('console: generating password')
            print(f'console: generated password {password}')
            print('console: Saving values[Username, Email, Password, Website], output = passwords.txt')            
            
            userName = (values['Username'])
            email = (values['Email'])
            website = (values['Website'])
            
            file = open(f'{stationary}', 'a')
            
            usrnm = "Username: " + userName + "\n"
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
            
            print(f'console: Username = {userName}')
            print(f'console: Email = {email}')
            print(f'console: Password = {password}')
            print(f'console: Website = {website}')
            print('console: Saved values[Username, Email, Password, Website], output = passwords.txt')
            print('console: opening "generated()"')
            
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
    [sg.Button('Done', use_ttk_buttons=True), sg.Button('Main Menu', use_ttk_buttons=True)]]
    window = sg.Window("Password Saver", layout, modal=False)
    choice = None

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            print('console: EXIT CODE "sg.WIN_CLOSED"')
            exit()
        if event == 'Main Menu':
            print('console: returning "main()"')
            window.hide()
            main()
        if event == "Done":
            print('console: Saving values[Username, Email, Password, Website], output = passwords.txt')
            
            UserName = (values['Username'])
            eMail = (values['Email'])
            PaSSword = (values['Password'])
            Website = (values['Website'])
            
            file = open(f'{stationary}', 'a')
            
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
            
            print(f'console: Username = {UserName}')
            print(f'console: Email = {eMail}')
            print(f'console: Password = {PaSSword}')
            print(f'console: Website = {Website}')
            
            print('console: Saved values[Username, Email, Password, Website], output = passwords.txt')
            print('console: opening "saved()"')
            window.hide()
            saved()
            main()
        
    window.close()

def pass_list():

    print('console: opening "passwords.txt"')
    print('console: reading "passwords.txt"')
    print('console: printing "passwords.txt"')
    print('console: passwords.txt sucssefully printed!')
    
    b = open('Data/passwords.txt')
    pass_reload = b.read()


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
    [sg.Text(pass_reload)],
    [sg.ProgressBar(1, size =(66,1))],
    [sg.Button('Clear Passwords', use_ttk_buttons=True), sg.Button('Main Menu', use_ttk_buttons=True)]
    ]
    passwords = sg.Window('Password List!', layout, modal=False)
    choice = None

    while True:
        event, values = passwords.read()
        if event == sg.WIN_CLOSED:
            print('console: EXIT CODE "sg.WIN_CLOSED"')
            exit()
        if event == 'Main Menu':
            print('console: returning "main()"')
            passwords.hide()
            main()
        if event == 'Clear Passwords':
            g = open(stationary, 'a')
            print('console: clearing "passwords.txt"')
            g.truncate(0)
            print('console: Cleared, please restart to update "Passwords" page')
            open('Data/passwords.txt', 'a')
            sg.popup(' - passwords.txt has been cleared, please restart Advanced Password Manager to refresh Passwords page.')
        
    passwords.close()

def Themes():
    layout = [
    [sg.Text('''
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░████████╗██╗░░██╗███████╗███╗░░░███╗███████╗░██████╗░
░╚══██╔══╝██║░░██║██╔════╝████╗░████║██╔════╝██╔════╝░
░░░░██║░░░███████║█████╗░░██╔████╔██║█████╗░░╚█████╗░░
░░░░██║░░░██╔══██║██╔══╝░░██║╚██╔╝██║██╔══╝░░░╚═══██╗░
░░░░██║░░░██║░░██║███████╗██║░╚═╝░██║███████╗██████╔╝░
░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')],
    [sg.Text(' - To change the theme, enter the exact name of the theme as shown in theme')],
    [sg.Text('previewer.')],
    [sg.Text(' - Otherwise leave blank for a random theme.')],
    [sg.ProgressBar(1, size =(44,1))],
    [sg.Text('Theme Name', size =(10,1)), sg.Input('', key='Theme')],
    [sg.ProgressBar(1, size =(44,1))],
    [sg.Button('Change Theme', use_ttk_buttons=True), sg.Button('Theme Previewer', use_ttk_buttons=True), sg.Button('Main Menu', use_ttk_buttons=True)]]
    
    Main = sg.Window('Theme Changer', layout, modal=False)
    
    while True:
        event, values = Main.read()
        if event == sg.WIN_CLOSED:
            print('console: EXIT CODE "sg.WIN_CLOSED"')
            exit()
        if event == 'Theme Previewer':
            print('console: launching "sg.theme_previewer()"')
            Main.hide()
            sg.theme_previewer()
            print('console: closing "sg.theme_previewer()"')
            Themes()
        if event == 'Change Theme':
        
            c = open('Data/theme', 'a')
            
            c.truncate(0)
            c.write(values['Theme'])
            
            theme = (values['Theme'])
            print(f'console: saving value {theme} to theme')
            print(f'console: setting sg.theme({theme})')
            sg.theme(values['Theme'])
            print('console: returning "main()"')
            Main.hide()
            main()
        if event == 'Main Menu':
            print('console: returning main()')
            Main.hide()
            main()

        Main.close()

def output_define():
    layout = [[sg.Text(' - Please locate text document')],
    [sg.In() ,sg.FileBrowse(file_types=(("Text Files", "*.txt"),), key='File')],
    [sg.Button('Done', use_ttk_buttons=True), sg.Button('Back', use_ttk_buttons=True), sg.Button('Main Menu', use_ttk_buttons=True)]]
    window = sg.Window('Password Output', layout, modal=False)
    
    while True:
        event, values = window.read()
        if event == 'Done':
            
            new_ouput = (values['File'])
            
            t = open('output', 'a')
            t.truncate(0)
            t.write(new_ouput)
            
            window.hide()
            Developer_Tools()
        if event == 'Back':
            window.hide()
            Developer_Tools()
        if event == 'Main Menu':
            window.hide()
            main()
        if event == sg.WIN_CLOSED:
            exit()

def Developer_Tools():
    layout = [[sg.Text(' - These are developer tools and can mess up the code')],
    [sg.Text(' - Proceed with cuation.')],
    [sg.Button('Clear Console', use_ttk_buttons=True), sg.Button('Set Output Path', use_ttk_buttons=True), sg.Button('Custom Theme', use_ttk_buttons=True), sg.Button('Main Menu', use_ttk_buttons=True)]]
    
    window = sg.Window('Developer Tools', layout, modal=False)
    
    while True:
        event, valuse = window.read()
        if event == sg.WIN_CLOSED:
            print('console: EXIT CODE "sg.WIN_CLOSED')
            exit()
        if event == 'Clear Console':
            clear()
            print('console: console cleared')
        if event == 'Main Menu':
            print('console: returning "main()"')
            window.hide()
            main()
        if event == 'Set Output Path':
            window.hide()
            output_define()
        if event == 'Custom Theme':
            print('Developer: Still in development')
            sg.popup('Still in development')
        
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
    [sg.Text('[+] Created By Aiden Tingler')],
    [sg.Text('[+] Welcome to Advanced Password Manager GUI!')],
    [sg.Text('[+] This password manager allows you to save your own passwords or get a generated password using pythons')],
    [sg.Text('generating tools.')],
    [sg.Text('[+] Get started by selection one of the options below!')],
    [sg.Text('[+] To updated Passwords page, you must restart Advanced Password Manager GUI.')],
    [sg.ProgressBar(1, size =(59,1))],
    [sg.Button('Generate Password', use_ttk_buttons=True), sg.Button('Enter Password', use_ttk_buttons=True), sg.Button('Passwords', use_ttk_buttons=True), sg.Button('Change Theme', use_ttk_buttons=True), sg.Button('Options', use_ttk_buttons=True), sg.Button('Restart', use_ttk_buttons=True), sg.Button('Exit', use_ttk_buttons=True)]]
    window = sg.Window("Main Menu", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            print('console: EXIT CODE "sg.WIN_CLOSED"')
            exit()
        if event == "Exit":
            print('console: closing')
            exit()
        if event == "Generate Password":
            print('console: opening "open_window()"')
            window.hide()
            open_window()
        if event == "Enter Password":
            print('console: opening "enter()"')
            window.hide()
            enter()
        if event == 'Passwords':
            print('console: opening "pass_list()"')
            window.hide()
            pass_list()
        if event == 'Change Theme':
            print('console: opening "Themes()"')
            window.hide()
            Themes()
        if event == 'Options':
            print('console: opening "Developer_Tools()"')
            window.hide()
            Developer_Tools()
        if event == 'Restart':
            window.hide()
            continue
    window.close()



if __name__ == "__main__":

    main()
