import os
import sys
import subprocess
import time
import lms_login


bashrc = open(f"{os.environ['HOME']}/.bashrc", 'a+')
bashrc1 = open(f"{os.environ['HOME']}/.bashrc", 'r')

if 'alias r="python3 ~/Scripts/Python/bashrc_to_python/reviews.py"' not in bashrc1.read():
    bashrc.write('alias r="python3 ~/Scripts/Python/bashrc_to_python/reviews.py"')
bashrc.close()
bashrc1.close()

def clear():
    os.system('clear')


def get_topic():
    return input("What topic do you want to review..? ").capitalize()


def get_iteration():
    return input("Iteration..? ")


def closing():
    time.sleep(1)
    clear()
    value = subprocess.getoutput('wtc-lms reviews | grep "Graded" | wc -l')
    print(f"{value} Reviews Done!!")


def main():
    clear()
    if 'reviews.py' not in sys.argv[-1]:
        topic = sys.argv[-1].capitalize()
    else:
        topic = get_topic()

    if len(topic.split()) == 2 and topic.split()[-1].isdigit():
        iteration = str(topic.split()[-1])
    else:
        print(topic.capitalize())
        iteration = get_iteration()

    clear()
    if len(iteration) == 0:
        value = subprocess.getoutput(f"wtc-lms reviews | grep 'Invited' | grep '{topic}'").splitlines()
    else:
        value = subprocess.getoutput(f"wtc-lms reviews | grep 'Invited' | grep '{topic}' | grep 'Iteration {iteration}'").splitlines()
    

    try:
        review_uuid = value[0].split()[-2].strip('()')
    except IndexError:
        print("Topic/Iteration Complete or is not found!!")

    try:
        repo_path = subprocess.getoutput(f'wtc-lms accept {review_uuid}').split()[-1]
        print(f"Review Accepted and repo is here ---> {repo_path}")
    except UnboundLocalError:
        closing()
        exit()
    
    grade = input('Grade: ')
    # while grade not in range(10) or not grade.isdigit():
    #     grade = input('Grade: ')
        
    comment = input("Comment: ")
    
    os.system(f"wtc-lms add_comment {review_uuid} '{comment}'")
    os.system(f"wtc-lms grade_review {review_uuid} '{grade}'")
    remove = input("remove repo...y/n?: ").lower()
    # while remove != 'n' or remove != 'y':
    #     clear()
    #     remove = input("remove repo...y/n?: ").lower()
    
    if remove == 'y':
        os.system(f'rm -rf {repo_path}')
    else:
        pass
    closing()




main()
