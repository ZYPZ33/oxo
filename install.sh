#!/bin/sh
executable_name="oxo"
install_directory="/usr/local/bin"
install oxo.py ${install_directory}/${executable_name}&&echo "${executable_name} installed at ${install_directory}"
