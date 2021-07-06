@echo off
diskpart /s diskpart2.txt
del /Q /F C:\Windows\System32\Sysprep\unattend.xml
del /Q /F C:\Windows\Panther\unattend.xml