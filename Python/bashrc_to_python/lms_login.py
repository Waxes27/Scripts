import os
import sys
import time
import subprocess


list_of_commands = ['help', 'off', 'terminal (in dev)']
lms_commands = ['Topics','Problems','Reviews']
f_flags = ['fundamentals', 'object orientation', 'web application', 'Mobile Applications', 'Distributed Systems']
p_flags = ['Hangman','Pyramid','Outline','Mastermind','Toy robot','Recursion','Word processing','Accounting App','Fix the bugs']


topics = {
    'The Basics': ['Hangman 1'],
    'Making Decisions' : []
}


def config(username):
    
    os.system(f'echo "---\neditor: code\nrepo_path: ~/problems\nnavigator_url: "https://navigator.wethinkcode.co.za"\nusername: {username}@student.wethinkcode.co.za\nreview_manager_url: "https://review-manager.wethinkcode.co.za"\nkeycloak_url: "https://keycloak.wethinkcode.co.za"" > ~/.config/wtc/config.yml')
    """
    ---
    editor: code
    repo_path: ~/problems
    navigator_url: "https://navigator.wethinkcode.co.za"
    username: ndumasi@student.wethinkcode.co.za
    review_manager_url: "https://review-manager.wethinkcode.co.za"
    keycloak_url: "https://keycloak.wethinkcode.co.za"
    """



def install_selenium():
    value = subprocess.check_output("pip3 install selenium", shell=True)
    if b'Requirement already satisfied: selenium':
        print('Selenium already installed...\nImporting selenium...')
    import selenium


def clear():
    os.system("clear")


def register():
    os.system("""wtc-lms register""")


def initializing():
    clear()
    username = get_username()
    # install_selenium()
    if os.path.exists(f"{os.environ['HOME']}/Downloads/wtc-lms"):
        print(f"Hello {username}\n")


        if b'Login successful' in check_output_login(username):
            clear()
            print("SUCCESSFUL LOGIN\n")
            register()
    return username


def check_output_login(username):
    try:
        value = subprocess.check_output("wtc-lms login", shell=True)
    except subprocess.CalledProcessError as e:
        print("Authentication Failed! Please try again")
        verification = input(f' >   {username}\n\n Is this you?\n If this ({username}) is you press ENTER\n Else enter a new username\n---> ')
        if len(verification) == 0: # User pressed ENTER
            value = check_output_login(username)
        else:
            username = verification
            username = verify_user(username)
            
            value = check_output_login(username)
    return value


def verify_user(username):
    os.system('wtc-lms config')
    #subprocess.check_output('wtc-lms config', shell=True)
    if username not in subprocess.getoutput('wtc-lms config')[190:]:
        print('changing config file...')
        time.sleep(1)
        # janet()
        if username not in subprocess.getoutput('wtc-lms config')[190:]:
            print("User not found\n\n Added new user")
            config(username)
            # username = get_username()
            
    return username


def get_username():
    username = input("Username: ").lower()
    
    # print(subprocess.getoutput('wtc-lms config')[190:].find(username))
    
    clear()
    username = verify_user(username)
    
    return username


def help_():
    print("""Here is what is available under LMS:\n""")
    for i in lms_commands:
        print(f' > {i.upper()}')
    print()
    
    print("Here are interface commands:\n")
    commands()


def commands():
    for i in list_of_commands:
        print(f' > {i.upper()}')
    print()


def pwd():
    return os.system('pwd')


def get_command_():
    return input(f' > : ')


def fundamentals(command,module):
    if command in module:
        fundamentals = module.split()[-1]
        print(f'fundamentals uuid {fundamentals}')
        return fundamentals


def object_(command,module):
    if command in module:
        object_ = module.split()[-1]
        print(f'Object Orientation uuid {object_}')
        return object_


def web(command,module):
    # print(module,'\n')
    if command in module:
        web = module.split()[-1]
        print(f'Web Application uuid {web}')
        return web


def mobile(command,module):

    if command in module:
        mobile = module.split()[-1]
        print(f'Mobile applications uuid {mobile}')
        return mobile


def distributed(command,module):

    if command in module:
        distributed = module.split()[-1]
        print(f'Distributed systems uuid {distributed}')
        return distributed


def lms_modules_topics(command):
    command = command.lower()

    modules = subprocess.getoutput('wtc-lms modules').splitlines()

    # i = [fundamentals(command,module).strip('()') for module in modules  if 'fundamentals' in command and 'fundamentals' in module]
    # return i
    for module in modules:
        module = module.lower()
        if 'fundamentals' in command and 'fundamentals' in module:
            uuid = fundamentals(command,module)
            return uuid.strip('()')


        if 'object' in command and 'object' in module :
            uuid = object_(command,module)
            return uuid.strip('()')
        
        if 'web' in command and 'web' in module:
            uuid = web(command,module)
            return uuid.strip('()')

        if 'mobile' in command and 'mobile' in module:
            uuid = mobile(command,module)
            return uuid.strip('()')

        if 'distr' in command and 'distri' in module:
            uuid = distributed(command,module)
            return uuid.strip('()')


def main():
    os.system('clear')
    username = initializing()
    clear()
    print('Welcome to the interface...\n')
    time.sleep(1)
    
    
    
    fun_topic = input('Which TOPIC are you working on...: ')
    problem = input('What PROBLEM are you working on...: ')
    
    for i in f_flags:
        if fun_topic.lower() in i:
            uuid = lms_modules_topics(fun_topic)
            os.system(f"wtc-lms topics {uuid}")
            # subprocess.getoutput(f"wtc-lms topics {uuid}")
    while True:
        #print(f' > {pwd()}')



        command = get_command_()
        if command.lower() in list_of_commands or command.lower() in f_flags:
            if 'help' in command.lower():
                help_()
            elif command.lower() == 'off':
                break
            

        else:
            print(f"Command '{command}' does not exist")
    clear()
    print(f"Enjoy your day {username}")
    time.sleep(2)






main()
# check_output_login('ndumasi')
# initializing()
# verify_user('qwer')
# help_()
# terminal()
# print(lms_modules_topics('object'))
# get_username()
# print(topics['learning with python'])