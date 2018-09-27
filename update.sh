#!/usr/bin/bash
cd ..
rm -rf Oit
cd
pkg install git python2
git clone https://github.com/Budjank/Oit
cd Oit
cat README.txt
python2 Oit.py
