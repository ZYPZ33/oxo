#!/bin/sh
executable_name="oxo"
install_directory="/usr/local/bin"
if [ -n "$1" ]
then executable_name="$1"
fi
test -e ${install_directory}/${executable_name}&& \
read -p "Do you want to replace the already installed version? [Y/n]" input

#if [ "${input}" = "y" ||  "${input}" = "Y" ]
if [ "${input}" = "y" ] || [ "${input}" = "Y" ]
  then install oxo.py ${install_directory}/${executable_name}&&\
echo "${executable_name} installed at ${install_directory}"
fi
