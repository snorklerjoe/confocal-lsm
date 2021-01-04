#!/bin/sh

#This program changes the permissions of the specified file to be used by a user.
echo "Changing the permissions of $1";
USER=$(whoami);
#echo $USER;
sudo chmod 777 $1
echo "Done.";
