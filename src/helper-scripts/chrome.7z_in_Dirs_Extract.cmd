@echo off

set SevenZip="C:\Program Files\7-Zip\7z.exe"
set file="chrome.7z"
FOR /D %%D in (*.*) DO (
	cd %%D
	if exist %file% (
		echo Extracting %file% in folder %%D ...
		%SevenZip% x %file% -aoa
	)
	cd ..
)
PAUSE
