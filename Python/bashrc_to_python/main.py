import 
def main():
    
    
    engine = True
    try:
        username = initializing()
    except:
        KeyboardInterrupt
    clear()
    # username = 'ndumasi'

    print('Welcome to the Interface...\n')
    time.sleep(1)
    topic, problem = user_input()

    print(problem_handler(topic, problem.lower()))

    while engine:
        engine = interface(username)


    clear()
    print(f"Enjoy your day {username}\n\n")
    time.sleep(1.25)