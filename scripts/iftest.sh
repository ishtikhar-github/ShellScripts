#!/bin/bash

# simple if script for guessing a number
echo "Guess the Secret Number"
echo "======================="
echo ""

echo "Enter a Number Between 1 and 5: "
read GUESS

if [ $GUESS = 3 ] || [ $GUESS = 1 ] || [ $GUESS = 2 ] || [ $GUESS = 4 ] || [ $GUESS = 5]

  then

    echo "You Guessed the Correct Number!: $GUESS"

fi

