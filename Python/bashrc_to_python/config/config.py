import os
import sys

os.system("clear")
print("Welcome to LMS Troubleshooting...\n")



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



def trouble(username):
    print()
    print("     Setting Git Global Config...")
    os.system(f"git config --global user.name '{username}'; git config --global user.email '{username}@student.wethinkcode.co.za'")
    print("     Git Global Config Set...\n")



def main():
    username = input("What is your username: ")
    config(username)
    trouble(username)

    print("Done, other LMS issues relay to Waxes27...")
    
