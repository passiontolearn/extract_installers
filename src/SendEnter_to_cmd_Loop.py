# pip install pypiwin32
import win32api
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
while True: 
	shell.AppActivate("cmd.exe")
	shell.SendKeys("{ENTER}")
	win32api.Sleep(750)