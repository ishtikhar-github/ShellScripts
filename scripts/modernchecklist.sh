#!/bin/bash
# Linux Hardening Script for Ubuntu Server 20.04 LTS

##############################################################################################################

f_banner(){
echo " Welcome to fareye Ubuntu Server 20.04 LTS Hardening Process "
echo
}

##############################################################################################################
# Check if running with root User
clear
f_banner
check_root() {
if [ "$USER" != "root" ]; then
      echo "Permission Denied"
      echo "Can only be run by root"
      exit
else
     echo "you are running this script as $USER"
      #clear
      #f_banner
fi
}

##############################################################################################################
# Installing Dependencies # Needed Prerequesites will be set up here
install_dep(){
   clear
   f_banner
   echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
   echo -e "\e[93m[+]\e[00m Setting some Prerequisites"
   echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
   echo ""
   apt update -y
}
add_user(){
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
   echo -e "\e[93m[+]\e[00m Adding New User"
   echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
   echo ""
   adduser demo
}
###################################
# Main Script Logic Starts Here   #
###################################
function menu {
	clear
	echo
	echo -e "\t\t\tHardening  Menu\n"
	echo -e "\t1. Check Script is running using root user"
	echo -e "\t2. update packages"
	echo -e "\t3. Add NewUser Demo"
	echo -e "\t0. Exit Menu\n\n"
	echo -en "\t\tEnter an Option: "
	read -n 1 option
}
while [ 1 ]
do
	menu
	case $option in
	0)
	break ;;

	1)
	check_root ;;

	2)
	install_dep ;;

        3)
        add_user ;;

	*)
	clear
	echo "Sorry, wrong selection";;
	esac
	echo -en "\n\n\t\t\tHit any key to continue"
	read -n 1 line
done
clear

