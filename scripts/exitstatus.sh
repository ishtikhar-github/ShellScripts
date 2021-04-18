#!/bin/bash

# this is to show exit status types

set -e

expr 1 + 5
echo $?

rm doodles.sh
echo $?

expr 10 + 10
echo $?



# expression evaluation
expr 2 + 2
expr 2 + 2 \* 4
expr \( 2 + 2 \) \* 4
