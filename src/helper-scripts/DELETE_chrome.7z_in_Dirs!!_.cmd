@echo off

set file="chrome.7z"
FOR /D %%D in (*.*) DO (
	cd %%D
	if exist %file% (
		echo Deleting %file% in folder %%D ... !
		del %file%
	)
	cd ..
)
PAUSE
