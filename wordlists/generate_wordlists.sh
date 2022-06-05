#! /bin/bash

crunch 10 10 -t 079%%%%%%% -s 0791111111 -o zain
crunch 10 10 -t 078%%%%%%% -s 0781111111 -o umniah
crunch 10 10 -t 077%%%%%%% -s 0771111111 -o orange
cat zain umniah orange > jordanian_number
rm zain umniah orange
cp /usr/share/wordlists/rockyou.txt .

