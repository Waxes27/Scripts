import globals_

def help_():
    print("""Here is what is available under LMS:\n""")
    for i in globals_.lms_commands:
        print(f' > {i.upper()}')
    print()
    
    print("Here are interface commands:\n")
    commands()


def commands():
    for i in globals_.list_of_commands:
        print(f' > {i.upper()}')
    print()