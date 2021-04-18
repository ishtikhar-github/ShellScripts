#!/bin/bash
echo "+-------------------------------------------------------------------------------------------------------------------+"
echo "|Average:       kbmemfree kbmemused  %memused kbbuffers kbcached  kbcommit   %commit  kbactive   kbinact   kbdirty  |"
echo "+-------------------------------------------------------------------------------------------------------------------+"
for file in `ls -tr /var/log/sysstat/sa* | grep -v sar`
do
dat=`sar -f $file | head -n 1 | awk '{print $4}'`
echo -n $dat
sar -r -f $file  | grep -i Average | sed "s/Average://"
done
echo "+-------------------------------------------------------------------------------------------------------------------+"
