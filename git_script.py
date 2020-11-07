import sys
import os



def git_ask(command):
    git_files = {}
    os.system('clear;ls')
    number_of_files = input("\nHow many files do you wish to git add: ")
    for i in range(int(number_of_files)):
        name_of_file = input("\nName of file? ")
        commit_message = input(f"\n\nEnter commit message for --> {name_of_file}\n --> Here: ")
        git_files[name_of_file] = commit_message
    
    return git_files

def git_confirm(dict_):
    i = 1
    for k,v in dict_.items():
        print(f"\nFile{i}: {k}\n    Commit Message: {v}")
        i += 1
    confirmation = input("Are you sure you want to 'GIT PUSH' y/n: ")
    if 'y' in confirmation.lower():
        for k,v in dict_.items():
            os.system(f"""git add {k};git commit -m '{v}'""")
        os.system('git push')


git_confirm(git_ask(""))