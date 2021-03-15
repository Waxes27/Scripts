import os
import sys
import subprocess
import time
import requests
import re
import threading
import concurrent.futures
# import lms_login

module_dict = {}
module_list = ['Fundamentals',"Object Orientation","Web Applications","Mobile Applications","Distributed Systems"]


bashrc = open(f"{os.environ['HOME']}/.bashrc", 'a+')
bashrc1 = open(f"{os.environ['HOME']}/.bashrc", 'r')

if 'alias r="python3 ~/Scripts/Python/bashrc_to_python/reviews.py"' not in bashrc1.read():
    bashrc.write('alias r="python3 ~/Scripts/Python/bashrc_to_python/reviews.py"')
bashrc.close()
bashrc1.close()

def clear():
    os.system('clear')


def wtc_topics():
    modules = subprocess.getoutput("wtc-lms modules")
    matches = re.findall(r'wtc-lms topics .{36}',modules)
    return matches


def wtc_modules(matches):
    topic_list = []
    for i in matches:
        topic_list.append(subprocess.getoutput(i))
    
    # print(topics)
    counter =0
    for i in topic_list:
        
        module_dict[module_list[counter]] = re.findall(r"wtc-lms problems .{36}",i)
        counter += 1


def userIn():
    reviewTopic = input("What are you reviewing: ").lower()
    for i in reviewTopic.split():
        if i.isdigit():
            iteration = i
            break
    if not i.isdigit():
        iteration = input("Iteration: ")
    return reviewTopic, iteration


def problemSolver(v, delay=0):
    print(subprocess.getoutput(f"{v}&"))
    # print(v)
    # time.sleep(delay)



def main():
    # reviewTopic, iteration = userIn()

    matches = wtc_topics()
    wtc_modules(matches)
    x = 0
    with concurrent.futures.ThreadPoolExecutor() as e:

        while x <= len(module_dict['Fundamentals'])-1:
            # t1 = e.submit(problemSolver(module_dict['Fundamentals'][x]))
            # t2 = e.submit(problemSolver(module_dict['Fundamentals'][(len(module_dict['Fundamentals'])//2)+x]))
            for i in range(len(module_dict['Fundamentals'])):
                t1 = e.submit(problemSolver(module_dict['Fundamentals'][i]))
                print("T1")
                t2 = e.submit(problemSolver(module_dict['Fundamentals'][len(module_dict['Fundamentals'])//2+i]))
                print("t2")
            """
            Threads = [x for x in range(n)]
            for x in range(0, len(dict), len(Threads)):
                for i in range(0, len(Threads)):
                    if i < len(dict):
                        e.submit(problemSolver(module_dict['Fundamentals'][i]))
            """
            
            x +=1
        
        
        # print(k,v)




if __name__ == "__main__":
    main()
    # topic = subprocess.getoutput("wtc-lms modules")
    # print(topic)