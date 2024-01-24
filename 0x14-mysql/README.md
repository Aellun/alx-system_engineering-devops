## Project name: 0x14. MySQL

# Project Description
	Database administration
	Web stack debugging
	[How to] Install mysql 5.7
=========================================================================================================================================

Installation of mysql 5.7 steps include:

STEP 1
copy the key in this link paste it in a file named <signature.key> - https://intranet.alxswe.com/rltoken/Zzs_TLRYjWWFxjJRArmFcQ

STEP 2
sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

STEP 3
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B7B3B788A8D3785C

STEP 4
sudo apt-get update

STEP 5
sudo apt-cache policy mysql-server

STEP 6
sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
================================================================================================================================================
