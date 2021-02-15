#!/bin/bash

# echo $prompt_intel
name=`whoami`
# echo $name

if [[ $name != 'root' ]]; then
echo """


Getting ROOT permissions

"""
read -p "Install IntelliJ IDE (y/n): " prompt_intel

if [[ $prompt_intel == 'y' ]]; then
echo 'Installing IntelliJ...'; sleep 2

wget https://download.jetbrains.com/idea/ideaIC-2020.3.2.tar.gz
echo 'Unzipping file...'; sleep 2
mkdir ~/IDEA
tar -xvf ideaIC-2020.3.2.tar.gz -C ~/IDEA
fi

sudo ./java_setup.sh
exit
fi
# sleep 7

sudo apt update
sudo apt install default-jdk -y
sudo apt install default-jre -y
sudo apt install maven -y

sudo mkdir /etc/profile.d/maven/

sudo echo 'export JAVA_HOME=/usr/lib/jvm/default-java' > /etc/profile.d/maven/maven.sh
sudo echo 'export M2_HOME=/opt/maven' >> /etc/profile.d/maven/maven.sh
sudo echo 'export MAVEN_HOME=/opt/maven' >> /etc/profile.d/maven/maven.sh
sudo echo 'export PATH=${M2_HOME}/bin:${PATH}' >> /etc/profile.d/maven/maven.sh

sudo chmod +x /etc/profile.d/maven/maven.sh
source /etc/profile.d/maven/maven.sh

if [[ $prompt_intel == 'y' ]]; then
echo "

IntelliJ Stored in ~/IDEA

"
mv ideaIC-2020.3.2.tar.gz ~/IDEA
echo "To Use IntelliJ run command 'idea'"
fi
mvn -version
echo "alias idea='/bin/bash ~/IDEA/idea-IC-203.7148.57/bin/idea.sh'" >> ~/.bashrc 
exit