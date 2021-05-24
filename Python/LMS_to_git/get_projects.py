import os
import sys
import concurrent.futures
import subprocess
import re

def login():
    os.system("wtc-lms login")


def lms_scraper():
    print("Starting...")
    os.system(f"rm -rf {os.environ['HOME']}/problems")
    list_ = []
    temp = []
    start = []

    def starter(i):
        print("Starting......."+i)
        print(i)
        os.system(f"wtc-lms start {i}")

        


    def problems(i):
        print(f"Trying.......................wtc-lms problems {i}")
        work = subprocess.getoutput(f"wtc-lms problems {i}").splitlines()
        # if "problem" in work.lower():
        for i in work:
            
            if len(re.findall(r"\(\b.{36}\)",i)) > 0:
                pattern = re.findall(r"\(\b.{36}\)",i)[0].strip("()")
                start.append(pattern)


                print("Starting Problems.........\n\n")
                with concurrent.futures.ThreadPoolExecutor() as exe:
                    counter = 0
                    while len(start) > counter:
                        exe.submit(starter, start[counter].strip("()"))
                        counter += 1
                        start.remove(pattern)
        
            


    def topics(i):

        work = subprocess.getoutput(f"wtc-lms topics {i}").splitlines()
        for i in work:
            if len(re.findall(r"\(\b.{36}\)",i)) > 0:
                pattern = re.findall(r"\(\b.{36}\)",i)[0].strip("()")
                temp.append(pattern)

                # print("Filtering Problems")
                with concurrent.futures.ThreadPoolExecutor() as exe:
                    counter = 0
                    while len(temp) > counter:
                        exe.submit(problems, temp[counter].strip("()"))
                        counter += 1
                        temp.remove(pattern)

        
        


    work = subprocess.getoutput("wtc-lms modules").splitlines()

    
    for i in work:
        if len(re.findall(r"\(\b.{36}\)",i)) > 0:
            list_.append(re.findall(r"\(\b.{36}\)",i)[0])

    with concurrent.futures.ThreadPoolExecutor() as exe:
        counter = 0
        while len(list_) > counter:
            exe.submit(topics, list_[counter].strip("()"))
            counter += 1
            
    




def main():
    if "login" in sys.argv:
        login()
        exit()
    
    lms_scraper()

main()