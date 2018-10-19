#!/bin/bash

echo "\x1b[32m\t- Game of Life Installer -\x1b[37m\n"

INSTALL_DIR=$PWD
OS="$(uname)"

if [ $OS != "Linux" ]
then
    echo "\x1b[31mNot running on Linux. Current OS: ($OS) \x1b[37m\n"
    exit 1
fi

# App files 
mkdir --parents /opt/drakmord/life/assets/images
cp $INSTALL_DIR/bin/RUN /opt/drakmord/life
cp $INSTALL_DIR/assets/images/icon.png /opt/drakmord/life/assets/images
echo "$INSTALL_DIR" > /opt/drakmord/life/config.cfg

# Create desktop shortcut
cp $INSTALL_DIR/Life.desktop /usr/share/applications

echo "\x1b[32m- Installation sucessful\x1b[37m\n"
