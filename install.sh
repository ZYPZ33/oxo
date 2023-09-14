#!/bin/sh
executable_name="oxo"
install_directory="/usr/local/bin"
if [ -n "$1" ]
then executable_name="$1"
fi
install oxo.py ${install_directory}/${executable_name}&&\
echo "${executable_name} installed at ${install_directory}"
