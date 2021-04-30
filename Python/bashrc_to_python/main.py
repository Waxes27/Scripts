import subprocess
import re
import os
import sys

problem_uuid = []
problems = []
dict_ = {}

with open(f"{os.environ['HOME']}/.bashrc","a+") as bash:
    if f'alias wtcs="python3 {os.environ["HOME"]}/Scripts/Python/bashrc_to_python/main.py"' not in bash:
        bash.write(f'alias wtcs="python3 {os.environ["HOME"]}/Scripts/Python/bashrc_to_python/main.py"')

with open(f"{os.environ['HOME']}/.zshrc","a+") as zshrc:
    if f'alias wtcs="python3 {os.environ["HOME"]}/Scripts/Python/bashrc_to_python/main.py"' not in zshrc:
        zshrc.write(f'alias wtcs="python3 {os.environ["HOME"]}/Scripts/Python/bashrc_to_python/main.py"')
        



def helpCommand():
    print("""
    HISTORY     - get History Assignments
    """)

def lms_output(command):
    return subprocess.getoutput(command)

topics = re.findall(r"\D{3}-\D{3}.\w{6}.\w{8}-\w{4}-\w{4}-\w{4}-\w{12}",lms_output("wtc-lms modules"))


def keyNameProblem(name,listOfProblems):
    dict_[name] = listOfProblems


def problemLinkDict():
    counter = 0
    for i in topics:
        problems.append(re.findall(r"\D{3}-\D{3}.\w{8}.\w{8}-\w{4}-\w{4}-\w{4}-\w{12}",lms_output(i)))
        keyNameProblem(counter,problems[counter])
        counter+=1


def lmsHistory():
    for _ in problem_uuid:
        for i in _:
            print(lms_output(f"wtc-lms history {i.strip('()')}"))
            print()


def main():
    problemLinkDict()
    for i in problems:
        for _ in i:
            problem_uuid.append(re.findall(r"\(\w.*\b\)",lms_output(_)))

    if 'history' in sys.argv:
        lmsHistory()
    else:
        helpCommand()    




main()