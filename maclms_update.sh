#!/bin/bash

echo "Downloading LMS..."

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install wget
clear
wget www.georgepauer.com/maclms/wtc-lms
#clear

chmod +x wtc-lms
#sudo mv wtc-lms /bin/
#clear

echo "MAC WTC UPDATED..."
echo "Please restart Terminal."

sleep 2