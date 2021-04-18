#!/bin/bash
# Disable Unused FileSystems
for i in cramfs freevxfs jffs2 hfs hfsplus udf vfat usb-storage dccp sctp rds tipc ;
do 
touch /etc/modprobe.d/$i.conf ; echo "install $i /bin/true" > /etc/modprobe.d/$i.conf
done

# Ensure Mounting and FS Options Are configured Properly
for i in nodev nosuid noexec ;
do
mount | grep -E '\s/tmp\s' | grep  $i >> /dev/null
if [ $? -eq 0 ]
then
echo "$i is already set on /tmp partition"	
else
mount -o remount,$i /tmp 
fi
done

for i in nodev nosuid noexec ;
do
mount | grep -E '\s/dev/shm\s' | grep  $i >> /dev/null
if [ $? -eq 0 ]
then
echo "$i is already set on /dev/shm partition"	
else
mount -o remount,$i /dev/shm 
fi
done

# Set the sticky bit on all world writable directories:
df --local -P | awk '{if (NR!=1) print $6}' | xargs -I '{}' find '{}' -xdev -type d \( -perm -0002 -a ! -perm -1000 \) 2>/dev/null | xargs -I '{}' chmod a+t '{}'

# Run the following command to stop and mask autofs : 
systemctl --now mask autofs 

# Ensure AIDE is installed
apt install aide aide-common  &&  aideinit  &&  mv /var/lib/aide/aide.db.new /var/lib/aide/aide.db

# Ensure filesystem integrity is regularly checked (Automated)
echo "0 5 * * * /usr/bin/aide.wrapper --config /etc/aide/aide.conf --check" >> /var/spool/cron/crontabs/root

# Ensure address space layout randomization (ASLR) is enabled. Set the following parameter in /etc/sysctl.conf or a /etc/sysctl.d/* file: 
echo "kernel.randomize_va_space = 2" >> /etc/sysctl.conf && sysctl -w kernel.randomize_va_space = 2

# Ensure prelink is disabled (Automated)
apt purge prelink

# Ensure core dumps are restricted (Automated).Set the following parameter in /etc/sysctl.conf or a /etc/sysctl.d/* file:
echo "fs.suid_dumpable = 0" >> /etc/sysctl.conf && sysctl -w fs.suid_dumpable=0    

# Ensure AppArmor is installed (Automated). Install AppArmor : 
apt install apparmor

# Ensure all AppArmor Profiles are in enforce or complain mode. Run the following command to set all profiles to enforce mode:
aa-enforce /etc/apparmor.d/*         

# Ensure local login warning banner is configured properly and permission
echo "Authorized uses only. All activity may be monitored and reported." > /etc/issue  && chown root:root /etc/issue &&  chmod u-x,go-wx /etc/issue

# Ensure remote login warning banner is configured properly and permission
echo "Authorized uses only. All activity may be monitored and reported." > /etc/issue.net && chown root:root /etc/issue.net && chmod u-x,go-wx /etc/issue.net

# Ensure GDM is removed 
apt purge gdm3

# Ensure xinetd,  openbsd-inetd, X Window System, Avahi Server, CUPS, dhcp, ldap,nfs,dns,ftp, imap & pop3,samba,snmp,rsync,nis & http squid server are not installed
for packages in `cat /tmp/packages.txt`; do apt purge $packages;done

# Disable IPv6 (Manual). Edit /etc/default/grub and add ipv6.disable=1 to the GRUB_CMDLINE_LINUX parameters: 
echo "GRUB_CMDLINE_LINUX="ipv6.disable=1"" >> /etc/default/grub  &&  update-grub

# Ensure packet redirect sending disabled, ip forwarding disabled, source routed packets disabled,icmp redirects disabled, secure icmp redirect disabled,suspicious packets are logged, broadcast icmp request disabled, bogus icmp responses ignored,reverse path filtering enabled, tcp sync cookies enabled, ipv6 router disabled (Automated)
for netconf in `cat /tmp/netconf.txt`; do echo "$netconf" >> /etc/sysctl.conf && sysctl -w $netconf;done

# Firewall Configuration : Installation & Configuration of UFW
 apt install ufw 
# Ensure loopback traffic is configured (Automated)
 ufw allow in on lo
 ufw allow out from lo
 ufw deny in from 127.0.0.0/8
 ufw deny in from ::1
# Ensure outbound connections are configured (Manual)
  ufw allow out on all

# Ensure firewall rules exist for all open ports (Manual). For each port identified in the audit which does not have a firewall rule establish a proper. rule for accepting  inbound connections: for e.g ufw allow in <port>/<tcp or udp protocol>

# Run the following commands to implement a default deny policy:
# ufw default deny incoming
# ufw default deny outgoing
# ufw default deny routed

# Logging & Auditing. 
# Ensure auditd is installed &  service is enabled 
apt install auditd audispd-plugins &&  systemctl --now enable auditd

# Ensure rsyslog is installed and service is enabled & Ensure rsyslog default file permissions configured (Automated)
apt install rsyslog && systemctl --now enable rsyslog && echo "$FileCreateMode 0640" >> /etc/rsyslog.conf

#Ensure journald is configured to send logs to rsyslog, compress large log files & write logfiles to persistent disk Edit the /etc/systemd/journald.conf file and add the following lines:
echo "ForwardToSyslog=yes" >> /etc/systemd/journald.conf && echo "Compress=yes" >> /etc/systemd/journald.conf && echo "Storage=persistent" >> /etc/systemd/journald.conf

# Ensure permissions on all logfiles are configured (Automated) : Run the following commands to set permissions on all existing log files:
find /var/log -type f -exec chmod g-wx,o-rwx "{}" + -o -type d -exec chmod g-w,o-rwx "{}" +


# Access, Authentication and Authorization
# Ensure cron daemon is enabled and running. set permission on crontab files 
systemctl --now enable cron &&  chown root:root /etc/crontab &&  chmod og-rwx /etc/crontab

# sshd configuration
chown root:root /etc/ssh/sshd_config &&  chmod og-rwx /etc/ssh/sshd_config
sed -i '/X11Forwarding/s/^/#/g' /etc/ssh/sshd_config
cat << EOF >> /etc/ssh/sshd_config
LogLevel INFO
X11Forwarding no
MaxAuthTries 4
IgnoreRhosts yes
HostbasedAuthentication no
PermitRootLogin no
PermitEmptyPasswords no
PermitUserEnvironment no
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512,hmac-sha2-256
KexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org,diffie-hellman-group14-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,ecdh-sha2-nistp521,ecdh-sha2-nistp384,ecdh-sha2-nistp256,diffie-hellman-group-exchange-sha256
ClientAliveInterval 300
ClientAliveCountMax 3
Banner /etc/issue.net
AllowTcpForwarding no
maxstartups 10:30:100
MaxSessions 10
EOF

