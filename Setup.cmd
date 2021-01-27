@echo off
cd Install
Test.bat
cd ..
python3 -m pip install –upgrade pip
cls
cd Install
python3 -m pip3 install -r requirements.txt
cls
python3 telegram.py
echo "Script is running do not close the application"
