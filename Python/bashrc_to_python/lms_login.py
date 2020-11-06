import os
import sys
import time
import subprocess


list_of_commands = ['help', 'off', 'terminal (in dev)']
lms_commands = ['Topics','Problems','Reviews']
f_flags = ['fundamentals', 'object orientation', 'web application', 'Mobile Applications', 'Distributed Systems']
p_flags = ['Hangman','Pyramid','Outline','Mastermind','Toy robot','Recursion','Word processing','Accounting App','Fix the bugs']

topics = {
    ('hangman 1') : 'The Basics',
    ('hangman 2') : 'Making Decisions',
    ('pyramid') : 'Repeating Instructions',
    ('hangman 3') : 'Repeating Instructions',
    ('outline') : 'Structuring Data',
    ('mastermind 1') : 'Structuring Data',
    ('toy robot 1') : 'Procedures',
    ('mastermind 2') : 'Procedures',
    ('mastermind 3') : 'Simple Compute',#
    ('recursion') : 'Calling Functions',
    ('toy robot 2') : 'Calling Functions',
    ('word processing') : 'Processing Collections',
    ('toy robot 3') : 'Processing Collections',
    ('accounting app') : 'Modules & Packages',
    ('toy robot 4') : 'Modules & Packages',
    ('toy robot 5') : 'Modules & Packages',
    ('fix the bugs') : "Don't Panic",
    ('code clinic booking system') : 'Group Project',
}

def config(username):
    
    os.system(f'echo "---\neditor: code\nrepo_path: ~/problems\nnavigator_url: "https://navigator.wethinkcode.co.za"\nusername: {username}@student.wethinkcode.co.za\nreview_manager_url: "https://review-manager.wethinkcode.co.za"\nkeycloak_url: "https://keycloak.wethinkcode.co.za"" > ~/.config/wtc/config.yml')


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
    clear()
    return username


def check_output_login(username):
    try:
        value = subprocess.check_output("wtc-lms login", shell=True)
    except subprocess.CalledProcessError as e:
        print("Authentication Failed! Please try again")
        verification = input(f' >   {username}\n\n Is this you?\n If this ({username}) is you press ENTER\n Else enter a new username\n---> ')
        clear()
        if len(verification) == 0: # User pressed ENTER
            value = check_output_login(username)
        else:
            username = verification
            username = verify_user(username)
            
            value = check_output_login(username)
    return value


def verify_user(username):
    # os.system('wtc-lms config')
    #subprocess.check_output('wtc-lms config', shell=True)
    if username not in subprocess.getoutput('wtc-lms config')[190:]:
        print('changing config file...')
        time.sleep(1)
        # janet()
        if username not in subprocess.getoutput('wtc-lms config')[190:]:
            print("User not found\n\n --->  Added new user")
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
        if 'fun' in command and 'fun' in module:
            uuid = fundamentals(command,module)
            return uuid.strip('()')


        if 'obj' in command and 'obj' in module :
            uuid = object_(command,module)
            return uuid.strip('()')
        
        if 'web' in command and 'web' in module:
            uuid = web(command,module)
            return uuid.strip('()')

        if 'mob' in command and 'mob' in module:
            uuid = mobile(command,module)
            return uuid.strip('()')

        if 'dist' in command and 'dist' in module:
            uuid = distributed(command,module)
            return uuid.strip('()')


def topics_uuid_modules(fun_topic):
    for i in f_flags:
        if fun_topic.lower() in i:
            uuid = lms_modules_topics(fun_topic)
    return uuid


def list_of_problems():
    list_ = []
    for k,v in topics.items():
        try:
            k.split()
            print(f'>> {k}')
            list_.append(k)
        except AttributeError:
            list_.append(k[0])
            list_.append(k[1])
            print(f'>> {k[0]}')
            print(f'>> {k[1]}')
    return list_


def user_input():
    print('Here are a list of topics in LMS\n')
    for i in f_flags:
        print(f' >> {i}')


    fun_topic = input('\nWhich TOPIC are you working on...: ("back if undesired Module")')
    topic = topics_uuid_modules(fun_topic)


    print('\nHere are a list of problems available\n')
    if fun_topic.lower().startswith('fun'):
        list_of_problems()


    problem = input('\nWhat PROBLEM are you working on...: ')
    return topic, problem


def topics_uuid(uuid):
    for i in uuid.splitlines():
        if '(' in i:
            return i.split()[-1].strip('()')


def problem_handler(module_uuid, problem):

    value = subprocess.getoutput(f'wtc-lms topics {module_uuid}')
    
    topics_index = value.find(topics[problem])
    uuid = value[topics_index:topics_index+250]

    uuid = topics_uuid(uuid)

    print(".....Resolving your problem.....\n")
    
    value = subprocess.getoutput(f'wtc-lms problems {uuid}')[300:]
    for i in value.splitlines():
        if len(i.split()) > 2:
            print(i)


    
    return 'still need to get problem uuid'.upper()


def main():

    username = initializing()

    print('Welcome to the Interface...\n')
    time.sleep(1)
    
    topic, problem = user_input()
    print(problem_handler(topic, problem.lower()))
    
    while True:



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

# for k,v in topics.items():
#     print(k.upper())

#     (problem_handler("505079ba-4393-47ff-a956-330555b09f00", k.lower()))
#     clear()
    
# (problem_handler("505079ba-4393-47ff-a956-330555b09f00", 'mastermind 3'.lower()))