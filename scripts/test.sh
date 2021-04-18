#!/bin/bash

echo " testing env variables"
echo "testing exit status"



#!/bin/bash

if [[ "$(whoami)" != webwerks ]]; then
  echo "Only user root can run this script."
  exit 2
fi

echo "doing stuff..."

exit 0
