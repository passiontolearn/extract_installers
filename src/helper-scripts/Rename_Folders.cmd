FOR /D %%D in (*.*) DO (
	echo rename %%D to %%D.exe
	ren %%D %%D.exe
)
PAUSE
