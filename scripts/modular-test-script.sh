#!/bin/bash
# Linux Hardening Script for Ubuntu Server 20.04 LTS

# https://github.com/Jsitech/JShielder/blob/master/UbuntuServer_18.04LTS/jshielder.sh
# menu driven shell script to call a function: https://www.foxinfotech.in/2019/04/linux-unix-simple-menu-driven-program-using-shell-script.html

##############################################################################################################

banner(){
echo " Welcome to fareye Ubuntu Server 20.04 LTS Hardening Process "
echo
}

########################################################################################
# Check if running with root User
clear
banner
check_root() {
if [ "$USER" != "root" ]; then
      echo "Permission Denied"
      echo "Can only be run by root"
      exit
else
     echo "you are running this script as $USER"
fi
}

########################################################################################
# Disable Unused Filesystems
disable_unused_fs(){
   clear
   echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
   echo -e "\e[93m[+]\e[00m Disabling Unused File Systems"
   echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
   echo ""
for i in cramfs freevxfs jffs2 hfs hfsplus udf vfat usb-storage dccp sctp rds tipc ;
do 
touch /etc/modprobe.d/$i.conf  &&  echo "install $i /bin/true" > /etc/modprobe.d/$i.conf
done
if [ $? -eq 0 ] ; then
echo "you command has been executed successfully"
else
echo "your command is not executed successfully"
fi
}

 # Ensure Mounting and FS Options Are configured Properly
set_mounting_options(){
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo -e "\e[93m[+]\e[00m Setting Mounting Options on /tmp and /dev/shm filesystems"
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo ""
for i in nodev nosuid noexec ;
do
mount | grep -E '\s/tmp\s' | grep  $i >> /dev/null
if [ $? -eq 0 ]
then
echo "$i is already set on /tmp filesystem"	
else
mount -o remount,$i /tmp 
fi
done

for i in nodev nosuid noexec ;
do
mount | grep -E '\s/dev/shm\s' | grep  $i >> /dev/null
if [ $? -eq 0 ]
then
echo "$i is already set on /dev/shm filesystem"	
else
mount -o remount,$i /dev/shm 
fi
done
if [ $? -eq 0 ] ; then
echo "your command has been executed successfully"
else
echo "your command is not executed successfully"
fi
}

# Set the sticky bit on all world writable directories:
set_stickybit(){
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo -e "\e[93m[+]\e[00m Setting Sticky Bit on all world writable directories"
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo ""
df --local -P | awk '{if (NR!=1) print $6}' | xargs -I '{}' find '{}' -xdev -type d \( -perm -0002 -a ! -perm -1000 \) 2>/dev/null | xargs -I '{}' chmod a+t '{}'
if [ $? -eq 0 ] ; then
echo "your command has been executed successfully"
else
echo "your command is not executed successfully"
fi
}

# Disable Automounting 
disable_automounting(){
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo -e "\e[93m[+]\e[00m Disable Automounting "
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo ""
systemctl --now mask autofs 
if [ $? -eq 0 ] ; then
echo "your command has been executed successfully"
else
echo "your command is not executed successfully"
fi
}
# FileSystems Integrity Check. Ensure AIDE is installed and filesystems integrity is regularly checked
fs_integrity_check(){
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo -e "\e[93m[+]\e[00m Installing AIDE and Setting Cron for FS Integrity Check regularly "
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo ""
apt install aide aide-common  &&  aideinit  &&  mv /var/lib/aide/aide.db.new /var/lib/aide/aide.db
echo "0 5 * * * /usr/bin/aide.wrapper --config /etc/aide/aide.conf --check" >> /var/spool/cron/crontabs/root
if [ $? -eq 0 ] ; then
echo "your command has been executed successfully"
else
echo "your command is not executed successfully"
fi
}

# Ensure AppArmor is installed and its profiles are in enforce or complain mode
apparmor(){
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo -e "\e[93m[+]\e[00m Installing AppArmor and Setting Its Profile in enforce mode "
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo ""
apt install apparmor &&  aa-enforce /etc/apparmor.d/*         
if [ $? -eq 0 ] ; then
echo "your command has been executed successfully"
else
echo "your command is not executed successfully"
fi
}

# Warning Banners
login_local_remote_banner(){
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo -e "\e[93m[+]\e[00m Setting up Local and Remote Login Warning Msgs "
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo ""

# check motd file is present or not
file="/etc/motd"
if [ -f "$file" ] ; then
echo "file $file is present"
echo "removing file $file permanently" && rm -fr $file
else
echo "file $file is not present"
fi
echo "moving ahead with setting up local and remote banner"
echo " setting local login msg"
echo "Authorized uses only. All activity may be monitored and reported." > /etc/issue  && chown root:root /etc/issue &&  chmod u-x,go-wx /etc/issue
echo "setting remote login msg"
echo "Authorized uses only. All activity may be monitored and reported." > /etc/issue.net && chown root:root /etc/issue.net && chmod u-x,go-wx /etc/issue.net
if [ $? -eq 0 ] ; then
echo "your command has been executed successfully"
else
echo "your command is not executed successfully"
fi
}

# Ensure prelink & GDM are removed
prelink_gdm(){
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo -e "\e[93m[+]\e[00m Purging Prelink and Gdm Packages "
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo ""
echo  "purging prelink and gdm "
apt purge prelink  && apt purge gdm3
if [ $? -eq 0 ] ; then
echo "your command has been executed successfully"
else
echo "your command is not executed successfully"
fi
}

# Ensure Network Services like xinetd,openbsd-inetd,X Window System,Avahi Server,CUPS,dhcp,ldap,nfs,dns,ftp,imap & pop3,samba,snmp,rsync,nis & http squid server are not installed
network_services(){
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo -e "\e[93m[+]\e[00m Purging Unused Network Services and its Client Services "
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo ""

for i in xinetd openbsd-inetd xserver-xorg* avahi-daemon cups isc-dhcp-server slapd rpcbind bind9 vsftpd dovecot-imapd  dovecot-pop3d samba squid snmpd rsync nis rsh-client talk telnet ldap-utils
do 
echo "$i service, we are purging it now"
echo  "Purging $i service"
apt purge $i
done
if [ $? -eq 0 ] ; then
echo "your command has been executed successfully"
else
echo "your command is not executed successfully"
fi
}



menu=""
until [ "$menu" = "10" ]; do
clear
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo -e "\e[93m[+]\e[00m SELECT THE DESIRED OPTION"
echo -e "\e[34m---------------------------------------------------------------------------------------------------------\e[00m"
echo ""
echo "1. Check Script is running using root user"
echo "2. Disable Unused FileSystems"
echo "3. Set Mounting Options on /tmp and /dev/shm filesystems"
echo "4. Setting Sticky Bit on all world writable directories"
echo "5. Disable Automounting"
echo "6. Install AIDE and Set Cron for FS Integrity Check regularly"
echo "7. Install AppArmor and Set its profile in enforce mode"
echo "8. Setup Local and Remote Login Msgs"
echo "9. Purge Prelink and Gdm3 Package"
echo "10.Purge Unused Network Services and Its Client Services"

read menu
case $menu in
        1)
        check_root ;;
        2)
        disable_unused_fs ;;
        3)
        set_mounting_options ;;
        4)
        set_stickybit ;;
        5)
        disable_automounting ;;
        6)
        fs_integrity_check ;;
        7)
        Apparmor ;;
        8)
        login_local_remote_banner ;;
        9)
        prelink_gdm ;;
        10)
        network_services ;;
        *)
        clear
        echo "Sorry, wrong selection";;
esac
done
	echo -en "\n\n\t\t\tHit any key to continue"





