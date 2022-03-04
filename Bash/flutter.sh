sudo apt install curl git xz-utils
sudo apt install snapd
sudo snap install flutter --classic
sudo apt-get install clang cmake ninja-build pkg-config libgtk-3-dev
echo "export PATH=$PATH:/snap/bin"
flutter doctor --android-licenses

flutter config --enable-linux-desktop
