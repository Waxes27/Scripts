import os
import subprocess


def download():
    print(subprocess.getoutput(f"""
    sudo apt install curl wget gsettings -y
    wget https://assets.system76.com/wallpapers/unleash.png
    sudo mv unleash.png {os.environ["HOME"]}/.config
    """))


def setup():
    user = os.environ["USER"]
    
    print(subprocess.getoutput(f"""
    gsettings set org.gnome.desktop.background picture-uri file:////home/{user}/.config/unleash.png
    rm -rf unleash*
    """))

def clean():
    print(subprocess.getoutput(f"""
    mkdir {os.environ["HOME"]}/.wtc-backup
    mv {os.environ["HOME"]}/* {os.environ["HOME"]}/.wtc-backup
    cd {os.environ["HOME"]};rm -rf .mozilla .local .vscode .cache .config/google-chrome/Default .cache/google-chrome;mkdir -p Desktop Downloads Documents Music Pictures Public Templates Videos
    """))

    

def main():
    download()
    setup()
    clean()

main()

