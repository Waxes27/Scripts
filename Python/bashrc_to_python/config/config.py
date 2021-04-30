import os
import sys

os.system("clear")
print("Welcome to LMS Troubleshooting...\n\n\n")


def config(username):
    with open(f"{os.environ['HOME']}/.config/wtc/config.yml", "w") as f:
        f.write(f"""---
editor: code
repo_path: ~/problems
navigator_url: "https://navigator.wethinkcode.co.za"
username: {username}@student.wethinkcode.co.za
review_manager_url: "https://review-manager.wethinkcode.co.za"
keycloak_url: "https://keycloak.wethinkcode.co.za"  
""")
    os.system("wtc-lms login;wtc-lms register")



def main():
    username = input("What is your username: ")
    config(username)

main()
