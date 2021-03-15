# source lms_update.sh
clear
# exit
echo "Downloading LMS..."

wget www.georgepauer.com/lms/wtc-lms
clear

chmod +x wtc-lms
sudo mv wtc-lms /bin

clear
echo "LMS UPDATED...\nPlease restart Terminal"
sleep 2
# exit
