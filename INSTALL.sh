#!/bin/bash

INSTALL_DIR=$PWD
DESKTOP_DIR="$(xdg-user-dir DESKTOP)"
OS="$(uname)"
SUDO=''

echo -e "\x1b[32m\n\t- Game of Life Installer -\x1b[37m\n"

echo -e "-Checking permissions"
if (( $EUID != 0 )); then
    SUDO='sudo'
fi

echo -e "-Checking operating system"
if [ $OS != "Linux" ]
then
    echo -e "\x1b[31mNot running on Linux. Current OS: ($OS) \x1b[37m"
    exit 1
fi

echo -e "-Installing files"
# App files
$SUDO mkdir --parents /opt/drakmord/life/assets/images
$SUDO cp $INSTALL_DIR/bin/RUN /opt/drakmord/life
$SUDO cp $INSTALL_DIR/assets/images/icon.png /opt/drakmord/life/assets/images
$SUDO chmod -R 777 /opt/drakmord
touch /opt/drakmord/life/config.cfg
echo "$INSTALL_DIR" > /opt/drakmord/life/config.cfg

echo -e "-Creating desktop shortcut"
# Create desktop shortcut
$SUDO cp $INSTALL_DIR/bin/Life.desktop /usr/share/applications
$SUDO chmod 777 /usr/share/applications/Life.desktop
$SUDO ln -s /usr/share/applications/Life.desktop "$DESKTOP_DIR"

echo -e "\x1b[32m\n-Installation sucessful\x1b[37m\n"
