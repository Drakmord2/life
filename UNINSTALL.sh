#!/bin/bash

echo -e "\x1b[32m\n\t- Game of Life Uninstaller -\x1b[37m\n"

SUDO=''
if (( $EUID != 0 )); then
    SUDO='sudo'
fi

$SUDO rm -R /opt/drakmord
$SUDO rm /usr/share/applications/Life.desktop

echo -e "-Done\n"
