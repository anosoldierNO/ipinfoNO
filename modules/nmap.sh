#!/bin/bash
nmap --version > /dev/null 2>&1
if [ "$?" = "0" ]; then
    exit 1

else
    echo Det nødvendig å installere Nmap, installerer...
    sudo apt install nmap -y > /dev/null 2>&1

fi
