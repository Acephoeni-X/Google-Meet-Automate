@echo off #This will turn off output screen
echo "Script will wait 3 second to check additional functionalities"
timeout 3 >nul
cd Script
pip3 install -r requirements.txt
cls
python3 telegram.py
echo "Script is running do not close the application"
timeout 5 >nul
