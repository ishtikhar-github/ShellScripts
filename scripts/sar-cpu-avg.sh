# vi /opt/scripts/sar-cpu-avg.sh

#!/bin/bash
echo "+----------------------------------------------------------------------------------+"
echo "|Average:         CPU     %user     %nice   %system   %iowait    %steal     %idle  |"
echo "+----------------------------------------------------------------------------------+"
for file in `ls -tr /var/log/sysstat/sa* | grep -v sar`
do
dat=`sar -f $file | head -n 1 | awk '{print $4}'`
echo -n $dat
sar -f $file  | grep -i Average | sed "s/Average://"
done
echo "+----------------------------------------------------------------------------------+"



