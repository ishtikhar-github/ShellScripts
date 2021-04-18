#!/bin/bash

# This script is intended to show how to do simple substitution
shopt -s expand_aliases

alias TODAY="date"
alias UFILES="find /home -user $USER"

TODAYSDATE=`date`
USERFILES=`find /home -user $USER`

echo "Today's Date: $TODAYSDATE"
echo "All Files Owned by USER: $USERFILES"

A=`TODAY`
B=`UFILES`

echo "With Alias, TODAY is: $A"
echo "With Alias, UFILES is: $B"



