#!/bin/bash
name=`whoami`
version='ideaIC-2021.3.2.tar.gz'
name='ideaIC-2021.3.2'


echo "alias idea='/bin/bash ~/IDEA/$name/bin/idea.sh'" >> ~/.bashrc
echo "alias idea='/bin/bash ~/IDEA/$name/bin/idea.sh'" >> ~/.zshrc

# echo $prompt_intel
# echo $name

read -p "Install IntelliJ IDE (y/n): " prompt_intel

if [[ $prompt_intel == 'y' ]]; then
echo 'Installing IntelliJ...'; sleep 2

wget https://download.jetbrains.com/idea/$version
echo 'Unzipping file...'; sleep 2
mkdir ~/IDEA
tar -xvf $version -C ~/IDEA


fi
# sleep 7

sudo apt update
sudo apt install default-jdk -y
sudo apt install default-jre -y
sudo apt install maven -y

sudo mkdir /etc/profile.d/maven/

sudo echo 'export JAVA_HOME=/usr/lib/jvm/default-java' > /etc/profile.d/maven/maven.sh
sudo echo 'export M2_HOME=/usr/share/maven' >> /etc/profile.d/maven/maven.sh
sudo echo 'export MAVEN_HOME=/usr/share/maven' >> /etc/profile.d/maven/maven.sh
sudo echo 'export PATH=${M2_HOME}/bin:${PATH}' >> /etc/profile.d/maven/maven.sh

sudo chmod +x /etc/profile.d/maven/maven.sh
source /etc/profile.d/maven/maven.sh

# if [[ $prompt_intel == 'y' ]]; then
# echo "

# IntelliJ Stored in ~/IDEA

# "
# mv ideaIC-211.6432.7.tar.gz ~/IDEA
# fi
mvn -version
echo "To Use IntelliJ run command 'idea'"
exit
