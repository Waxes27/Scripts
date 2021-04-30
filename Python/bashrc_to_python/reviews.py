import subprocess
import re
import os
import sys
import concurrent.futures

problem_uuid = []
problems = []
dict_ = {}

with open(f"{os.environ['HOME']}/.bashrc","a+") as bash:
    if f'alias wtcr="python3 {os.environ["HOME"]}/Scripts/Python/bashrc_to_python/reviews.py"' not in bash:
        bash.write(f'alias wtcr="python3 {os.environ["HOME"]}/Scripts/Python/bashrc_to_python/reviews.py"')

with open(f"{os.environ['HOME']}/.zshrc","a+") as zshrc:
    if f'alias wtcr="python3 {os.environ["HOME"]}/Scripts/Python/bashrc_to_python/reviews.py"' not in zshrc:
        zshrc.write(f'alias wtcr="python3 {os.environ["HOME"]}/Scripts/Python/bashrc_to_python/reviews.py"')

def get_help():
    return """special keywords for projects:

    wtcr            -       starts a random review
    wtcr help       -       Shows this menu
    wtcr list       -       lists reviews
    wtcr sync list  -       lists already synced reviews
    wtcr stats      -       brings up statistics
    
    
    """

def lms_output(command):
    return subprocess.getoutput(command)


def assigned_counter():
    count = lms_output('wtc-lms reviews | grep "Assigned" | wc -l')
    print(f"{count}     projects pending...")



def not_done_counter():
    count = lms_output('wtc-lms reviews | grep "Invited" | wc -l')
    print(f"{count}     projects not started...")



def done():
    print(lms_output('wtc-lms reviews | grep "Graded" '))



def doneCounter():
    count = lms_output('wtc-lms reviews | grep "Graded" | wc -l')
    print(f"{count}     projects done...")


def review_finder(iteration,review):
    if len(iteration) == 0:
        pat = f"\(.+"
        reviews = re.findall(r">.*\b\)",lms_output("wtc-lms reviews"))
        for i in reviews:
            if review in i.lower():
                print(re.findall(pat,i.lower())[0].strip("()"))
    else:
        review_iter_pat = f"{review}.-.\w{{9}}.{iteration}.+"
        reviews = re.findall(review_iter_pat, lms_output("wtc-lms reviews").lower())

    return reviews



def rlist(topic,review,iteration):
    print(review, iteration)
    if topic == '':
        if iteration == "":
            reviews = lms_output(f"wtc-lms reviews | grep -i 'invited' | grep -i '{review}'").splitlines()
        else:
            reviews = lms_output(f"wtc-lms reviews | grep -i 'invited' |grep -i '{review} - iteration {iteration}'").splitlines()
    else:
        if iteration == "":
            reviews = lms_output(f"wtc-lms reviews | grep -i 'invited' | grep -i '{topic}' |grep -i '{review}'").splitlines()
        else:
            reviews = lms_output(f"wtc-lms reviews | grep -i 'invited' | grep -i '{topic}' |grep -i '{review} - iteration {iteration}'").splitlines()
    return reviews



def error_msg(param):
    if param == "login":
        logged_in= input("Are you logged in..? [Y/n]: ").lower()

        if logged_in == "y":
            print("You have no reviews available at this time...")
        else:
            if 'hyper::Error(Connect,' not in subprocess.getoutput("wtc-lms login".lower()):
                os.system("wtc-lms register")
                main()
                
            else:
                print("Error --->  Please Check your Internet Connection")
    exit()


def accept(list_of_available):
    if len(list_of_available) == 0:
        error_msg("login")
    

    for i in list_of_available:
        try:
            pattern = re.findall(r"(\(.+\b\))",i)[0].strip("()")
            print(subprocess.getoutput(f'wtc-lms accept {pattern}'))
            return subprocess.getoutput(f'wtc-lms accept {pattern}')
        except IndexError:
            print("Hmmmmm")
            exit()

def tester(path_to_repo):
    os.system(f"cd {path_to_repo};mvn compile exec:java")
    again = input("Test again [Y/n]: ").lower()

    if again == 'y':
        return tester(path_to_repo)



def filter_data(uuid,person,details):
    print(details)
    query = input("\nDo you want to continue this review [Y/n]: ").lower()
    # print(query == "y")
    if query == "y":
        pat = "\b:.\/h.*"
        # print(re.findall(pat,details)[0].strip(": "))
        file_path = (f'{subprocess.getoutput(f"wtc-lms sync_review {uuid}").split()[-1].strip("`")}')
        # print("")
        os.system(f'cd {file_path};mvn clean package')
        print("Synced...")

        testing = input("Do you wanna run the program [Y/n]: ").lower()
        if testing == 'y':
            tester(file_path)



        grade = input("\n\nGrade [1-10]: ")
        os.system(f"rm -rf {file_path}")
        comment = input("Comment: ")
        os.system(f"wtc-lms add_comment {uuid} '{comment}'")
        os.system(f"wtc-lms grade_review {uuid} {grade}")

        left = subprocess.getoutput('wtc-lms reviews | grep -i "assigned" -wc')

        print(f"Reviews Left: {left}")




def find_uuid(assigned,person):
    uuid = re.findall(r"\(.+\b\)",assigned)[0].strip("()")
    details = subprocess.getoutput(f"wtc-lms review_details {uuid}").lower()
    

    if person in details:
        filter_data(uuid,person,details)
        return True
    return False

def print_review_details(assigned):
    uuid = re.findall(r"\(.+\b\)",assigned)[0].strip("()")
    details = subprocess.getoutput(f"wtc-lms review_details {uuid}").lower()

    print(details)


def sync(problem,person):
    assigned = subprocess.getoutput("wtc-lms reviews | grep 'Assigned' ").lower().splitlines()
    if len(assigned) == 0:
        logged = input("Are you logged in [Y/n]: ").lower()
        if logged == 'n':
            os.system("wtc-lms login")
            assigned = subprocess.getoutput("wtc-lms reviews | grep 'Assigned' ").lower().splitlines()
            if len(assigned) == 0:
                print("\nInternet Connection or LMS is down")
                exit()

        else:
            print("No reviews at this time...")
            exit()

    with concurrent.futures.ThreadPoolExecutor() as exe:
        if "list" in sys.argv:
            print("Listing...\n\n\n\n\n\n")
            for i in assigned:
                print_review_details(i)
            return

        if len(person) == 0:
            assigned = assigned[0]
            print(assigned)
            exe.submit(find_uuid,assigned,person)
            

        for i in assigned:
            exe.submit(find_uuid,i,person)

    exit(123)



def review_arg_sorter(topic, iteration):

    if "sync" in sys.argv:
        if "list" in sys.argv:
            sync("","")
            exit()
        problem = input("What do you want to sync: ")
        person = input("Any username in specific [ENTER for blank]: ")
        sync(problem,person)


    if "help" in sys.argv:
        print(get_help())
        exit()


    elif "stats" in sys.argv:
        with concurrent.futures.ThreadPoolExecutor() as exe:
            exe.submit(not_done_counter)
            exe.submit(doneCounter)
            exe.submit(assigned_counter)
        exit()


    elif "list" in sys.argv[1:]:
        review = input("What do you want to see [ENTER for all]: ").lower()
        [print(i) for i in rlist(topic,review,iteration)]
        exit()


    elif len(sys.argv) == 1:
        review = input("What submission or topic do you want to review: ").lower()
        topic = input("Topic [ENTER for any]: ").lower()
        iteration = input("Iteration: ")
        return accept(rlist(topic,review,iteration))


    elif len(sys.argv) == 2:
        iteration = input("Iteration: ")
        review = sys.argv[-1]
        return accept(rlist(topic,review,iteration))


    elif sys.argv[-1].isdigit():
            iteration = [i for i in sys.argv if i.isdigit()][0]
            review = [i for i in sys.argv[1:] if i.isalpha()][0]
            return accept(rlist(topic,review,iteration))



def main():
    print(subprocess.getstatusoutput("ping -c1 google.com")[0])
    print("Testing connection...")
    if subprocess.getstatusoutput("ping -c1 google.com")[0] == 2:
        print("Check internet connection... or Google.com is down [Unlikely]")
        exit()
    print("done...\n")
    

    topic=review=iteration=''

    path_to_repo = re.findall(r"\/.+",review_arg_sorter(topic,iteration))



main()
# uuid = "c3db5615-f6e1-45cb-a0ed-fb67314a8566"
