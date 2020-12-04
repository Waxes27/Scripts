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


def list_reviews(topic):
    if topic.split()[-1] == 'list':
        value = subprocess.getoutput(f"wtc-lms reviews | grep 'Invited'")
        print(value)
    else:
        value = subprocess.getoutput(f"wtc-lms reviews | grep '{topic.split()[-1].capitalize()}' | grep 'Invited'")
        print(value)


def history_reviews():
    value = subprocess.getoutput(f"wtc-lms reviews | grep 'Graded'")
    print(value)


def get_topic():
    return input("What topic do you want to review..? ").capitalize()


def get_iteration():
    return input("Iteration..? ")


def closing():
    time.sleep(1)
    clear()
    value = subprocess.getoutput('wtc-lms reviews | grep "Graded" | wc -l')
    print(f"{value} Reviews Done!!")
    value = subprocess.getoutput('wtc-lms reviews | grep "Assigned" | wc -l')
    print(f"{value} Reviews pending completion")


def slacked(username,exercise,grade,comment):
    slack_file = open(f"{os.environ['HOME']}/problems/.slacked.txt", 'a+')
    slackee = f'{username}---> {exercise}--->{grade}---->{comment}'
    slack_file.write(f'{slackee}\n')
    slack_file.close()

def get_help():
    clear()
    return """
 > HELP     : Brings up this help menu
 > HISTORY  : Brings up the previously graded reviews
 > lIST     : Brings up a list of available reviews

Examples:
    'r word'         - Begins the review of a Word Processing
    'r list word'    - Brings up a list of all Word Processing to be reviewed
    'r sync'         - Brings forth a pending review to grade and process

"""
def grading():
    grade = ''
    while not grade.isdigit():
        grade = input('Grade (0 -> 10): ')
    while int(grade) not in range(10):
        grade = input('Grade (0 - 10): ')

    return grade

def sync():
    value = subprocess.getoutput('wtc-lms reviews | grep "Assigned"')
    if len(value) == 0:
        v = input('Have you logged in (y/n)... : ').lower()
        if v == 'y':
            print('\nThen there are no available reviews to bring forth...')
            return
        else:
            os.system('wtc-lms login;clear')
            os.system('wtc-lms register')
            clear()
            sync()
            return

    sync_uuid = (value.splitlines()[0].split()[-2].strip('()'))
    print(sync_uuid)
    value = subprocess.getoutput(f'wtc-lms sync_review {sync_uuid}')
    if 'delete it' in value:
        os.system(f"rm -rf{value.split('at')[1].split('.')[0]}")
        value = subprocess.getoutput(f'wtc-lms sync_review {sync_uuid}')
    clear()
    username = value.split()[-1].split('/')[-1].split('_')[0].strip('0123456789')
    exercise = value.split('submission')[1]
    print(f'Review synced into problems directory\n\nUsername: {username}\nExercise : {exercise}')

    grade = grading()
    comment = input("Comment: ")
    slacked(username,exercise,grade,comment)
    finalizing(grade, comment, sync_uuid)
    closing()



def finalizing(grade, comment, review_uuid):
    os.system(f"wtc-lms add_comment {review_uuid} '{comment}'")
    os.system(f"wtc-lms grade_review {review_uuid} '{grade}'")

def main():
    clear()
    if 'sync' in sys.argv:
        sync()
        return
        
    if 'help' in sys.argv:
        print(get_help())
        return
    if 'history' in sys.argv:
        history_reviews()
        return
    if 'list' in sys.argv:
        list_reviews(sys.argv[-1])
        return
    
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
        return

    try:
        repo_path = subprocess.getoutput(f'wtc-lms accept {review_uuid}').split()[-1]
        print(f"Review Accepted and repo is here ---> {repo_path}")
        print((repo_path.split('/')[-1].split('_')))
        username = (repo_path.split('/')[-1].split('_')[0])
        exercise = (repo_path.split('/')[-1].split('_')[2])
        print(username)
        print(exercise)
    except UnboundLocalError:    
        print(topic.split()[-1])

    grade = grading()


    comment = input("Comment: ")
    slacked(username,exercise,grade,comment)
    
    finalizing(grade, comment, review_uuid)
    
    remove = 'y'

    
    if remove == 'y':
        os.system(f'rm -rf {repo_path}')
    closing()



if __name__ == "__main__":
    main()

    # list_reviews('r list')
    # slacked()

# grade = ''
# while not grade.isdigit():
#     grade = input('Grade: ')
# while int(grade) not in range(10):
#     grade = input('Grade: ')