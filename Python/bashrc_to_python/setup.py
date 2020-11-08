import subprocess
import sys
import os
bashrc = open(f"{os.environ['HOME']}/.bashrc", 'r+')


if subprocess.getoutput(('echo $SHELL')) != "/bin/bash":
    os.system('bash')
    clear()

if not os.path.exists(f"{os.environ['HOME']}/Scripts"):
    a = subprocess.getoutput('git clone https://github.com/Waxes27/Scripts.git')

if not "python3 ~/Scripts/Python/bashrc_to_python/lms_login.py\n" in bashrc.read() and os.path.exists(f"{os.environ['HOME']}/Scripts"):
    bashrc.write("python3 ~/Scripts/Python/bashrc_to_python/lms_login.py\n")