:: Requires UniExtract2
:: see: https://github.com/Bioruebe/UniExtract2/releases

set CurrentPath=%~dp0
set UniExtract="D:\__Tools\win\UniExtract2\UniExtract.exe"

FOR %%f in (*.exe *.msi) DO ( 
	REM Using a temp Folder ("Extracted") to workaround a UniExtract problem with foldernames that end with ".exe" 
	REM among other odd behaviors of trying to Automate UniExtract.exe in a bat script (!)
	%UniExtract% "%%f" %CurrentPath%\Extracted\"%%f" /silent
)
PAUSE
