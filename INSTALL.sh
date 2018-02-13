#!/bin/bash

# Install Game of Life

INSTALL_DIR=$PWD

OS="$(uname)"

if [ $OS != "Linux" ]
then
    echo "Not running on Linux. Current OS: ($OS) \n"
    exit 1
fi

mkdir --parents /opt/drakmord/life/assets/images

cp $INSTALL_DIR/RUN /opt/drakmord/life
cp $INSTALL_DIR/assets/images/icon.png /opt/drakmord/life/assets/images

# Create desktop shortcut
cp $INSTALL_DIR/Life.desktop /usr/share/applications
