@echo off
cd Script
Test.bat
python3 -m pip install –upgrade pip
cls
python3 -m pip3 install -r requirements.txt
cls
python3 telegram.py
echo "Script is running do not close the application"
