import os
import sys
import time
import subprocess
from topic_fundamentals import topics as topics
import globals_
import help_c

# if subprocess.getoutput(('echo $SHELL')) != "/bin/bash":
#     os.system('bash')
#     clear()

# if not os.path.exists(f"{os.environ['HOME']}/Scripts"):
#     a = subprocess.getoutput('git clone https://github.com/Waxes27/Scripts.git')
#     print(a)
# bashrc = open(f"{os.environ['HOME']}/.bashrc", 'r+')
# print()
# if not "python3 ~/Scripts/Python/bashrc_to_python/lms_login.py\n" in bashrc.read():
#     bashrc.write("python3 ~/Scripts/Python/bashrc_to_python/lms_login.py\n")




def open_file():
    try:
        return open('.history.txt', 'r+')
    except FileNotFoundError:
        os.system('echo >> .history.txt')
        return open('.history.txt', 'r+')

history_file = open_file()
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
    if os.path.exists(f"{os.environ['HOME']}/Downloads/wtc-lms") or os.path.exists(f"{os.environ['HOME']}/bin/wtc-lms") or os.path.exists(f"/bin/wtc-lms"):
        print(f"Hello {username}\n")


        if b'Login successful' in check_output_login(username):
            clear()
            print("SUCCESSFUL LOGIN\n")
            print("Do not interrupt this process...\n\n")
            try:
                register()
            except KeyboardInterrupt:
                print("Interrupt found... RESTARTING PROCESS\n")
                register()
    else:
        print("...Please install LMS...")
    history_file.write(username)
    
    clear()
    return username


def failed_authentication(username):
    # print("Authentication Failed! Please try again")

    try:
        verification = input(f'\n  >>>   {username}\n\n Is this you?\n\n >> If this ({username}) is you press ENTER\n\n >>> Otherwise enter a new username\n---> ')
    except KeyboardInterrupt:
        clear()
        value = failed_authentication(username)

    if len(verification) == 0: # User pressed ENTER
        value = check_output_login(username)
    else:
        # username = verification

        username = verify_user(verification)

        value = check_output_login(username)
    return value


def check_output_login(username):
    try:
        value = subprocess.check_output("wtc-lms login", shell=True)
    except subprocess.CalledProcessError as e:
        clear()
        value = failed_authentication(username)

    return value


def verify_user(username):
    # os.system('wtc-lms config')
    #subprocess.check_output('wtc-lms config', shell=True)
    clear()
    if username not in subprocess.getoutput('wtc-lms config')[190:]:
        print('changing config file...')
        time.sleep(1)
        # janet()
        if username not in subprocess.getoutput('wtc-lms config')[190:]:
            print(f"User not found\n\n --->  Added new user\n\n Welcome {username}\n")
            config(username)
            # username = get_username()


    return username


def get_username():
    # try:
    #     old_user = input(f"Is your username {history_file.read()} \n'y/n': ")
    #     if old_user.lower() != 'y':
    #         clear()
    #     else:
    #         history_file.write(f"{username}\n")
    #         return verify_user(i)
    # except KeyboardInterrupt:
    #     pass
    try:
        username = input("Username: ").lower()
        while len(username) == 0:
            clear()
            username = get_username()
    except KeyboardInterrupt as k:
        
        clear()
        username = get_username()

    # print(subprocess.getoutput('wtc-lms config')[190:].find(username))

    clear()
    username = verify_user(username)
    history_file.write(f"{username}\n")


    return username


def get_command_(username):
    return input(f' > {username} : ')


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
    for i in globals_.f_flags:
        if fun_topic.lower() in i:
        
            return lms_modules_topics(fun_topic)



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


def get_topics():
    fun_topic = input('\nWhich TOPIC are you working on...:')
    clear()
    topic = topics_uuid_modules(fun_topic)
    return fun_topic,topic


def get_problem():
    problem = input('\nWhat PROBLEM are you working on...: ')
    clear()
    return problem

def user_input():
    print('Here are a list of topics in LMS\n')
    for i in globals_.f_flags:
        print(f' >> {i}')
    fun_topic, topic = get_topics()


    print('\nHere are a list of problems available\n')
    if fun_topic.lower().startswith('fun'):
        list_of_problems()

    problem = get_problem()

    return topic, problem


def topics_uuid(uuid):
    for i in uuid.splitlines():
        if '(' in i:
            return i.split()[-1].strip('()')


def problem_handler(module_uuid, problem):
    list_of_problems_ = []
    print(module_uuid)
    value = subprocess.getoutput(f'wtc-lms topics {module_uuid}')
    try:
        # print(value)
        topics_index = value.find(topics[problem])
        # print(topics_index)
        uuid = value[topics_index:topics_index+250]
        # print(uuid)
        uuid = topics_uuid(uuid)
        print(".....Resolving your problem.....\n")

        value = subprocess.getoutput(f'wtc-lms problems {uuid}')[300:]
        # print(uuid)
        for i in value.splitlines():
            if len(i.split()) > 2:
                list_of_problems_.append(i)
                # print(i)
    except KeyError:
        try:
            print("Invalid Problems Selected\n\n    << Please select from the available below >>")
            list_of_problems()
            problem = get_problem()
            problem_handler(module_uuid, problem.lower())
        except KeyboardInterrupt:
            print("Invalid Problems Selected\n\n    << Please select from the available below >>")
            list_of_problems()
            problem = get_problem()
            problem_handler(module_uuid, problem.lower())



    # print(list_of_problems_)
    

    return filter_problem_uuid(list_of_problems_, problem.split())


def interface(username):

    try:
        command = get_command_(username)
        print('topic' in command)
    except KeyboardInterrupt:
        clear()
        return interface(username)

    if command.lower() in globals_.list_of_commands or command.lower() in globals_.p_flags:
        if 'help' in command.lower():
            help_c.help_()
            return True
        elif command.lower() == 'off':
            return False
        elif 'problems' in command.lower():
            clear()
            print("Here are the available topics")
            for k,v in topics.items():
                print(k)
            print()
            return True


    else:
        print(f"Command '{command}' does not exist")
        return True


def filter_problem_uuid(list_of_problem_, problem):
    clear()
    # print(problem)
    for i in list_of_problem_:
        if problem[0].capitalize() in i:
            # print(problem[0])
            if problem[0].capitalize() in i.split()[:-3] and problem[-1].capitalize() in i.split()[:-3]:
                # print(i.split()[:-3])
                return (i.split()[-1])

    print()


def main():
    
    
    engine = True
    try:
        username = initializing()
    except:
        KeyboardInterrupt
    clear()

    print('Welcome to the Interface...\n')
    time.sleep(1)
    topic, problem = user_input()
    print(topic)
    print(problem_handler(topic, problem.lower()))

    while engine:
        engine = interface(username)


    clear()
    print(f"Enjoy your day {username}\n\n")
    time.sleep(1.25)



# print(get_topics())
# (lms_modules_topics('fun'))
# print(topics_uuid_modules('fundamentals'))
# print(get_username())
main()
# clear()
# for k,v in topics.items():
#     print(problem_handler('505079ba-4393-47ff-a956-330555b09f00', k))
#     print(k)
#     time.sleep(1.8)
#     clear()
# filter_problem_uuid(['Problem - Recursion [In Progress] (decea39d-7a2a-45d9-bd08-1af152c94516)', 'Toy Robot - Iteration 2 [In Progress] (e5be25a3-5fd4-4f71-8dc0-67e3b8b211bf)'], 'toy robot 2'.split())
# print(len(history_file.read()))
# open_file()
# while 1:
#     if interface('ndumasi') == False:
#         break
