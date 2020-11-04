import os
import sys
import time
import subprocess
os.system("pip3 install selenium")
os.system('clear')
import selenium

# help('modules')
list_of_commands = ['Help', 'Off', 'Home']


def check_output_login():
    try:
        value = subprocess.check_output("wtc-lms login", shell=True)
    except subprocess.CalledProcessError as e:
        print("Authentication Failed! Please try again")
        value = check_output()
    return value


def clear():
    os.system("clear")


def register():
    os.system("""wtc-lms register""")


def get_username():
    username = input("Username: ")
    clear()
    return username


def initializing():
    username = get_username()
    if os.path.exists(f"{os.environ['HOME']}/Downloads/wtc-lms"):
        print(f"Hello {username}\n")


        if b'Login successful' in check_output_login():
            clear()
            print("SUCCESSFUL LOGIN\n")
            register()


def help_():
    for i in list_of_commands:
        print(i)


def commands():
    for i in list_of_commands:
        print(i)
    print()


def home():
    os.system('cd')
    
    
def pwd():
    return os.system('pwd')
    
    
def get_command_():
    return input(f' > {pwd()}: ')
def main():

    
    initializing()
    clear()
    print('Welcome to the interface...\n')
    time.sleep(2)
    
    
    
    while True:
        #print(f' > {pwd()}')
        command = get_command_()
        if command.lower() in list_of_commands:
            if 'help' in command:
                help_()
            elif command.lower() == 'off':
                break
            
            elif command.lower() == 'home':
                home()
            
            
        else:
            print(f"Command '{command}' does not exist")
            command = get_command_()

main()