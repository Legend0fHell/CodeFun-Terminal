@echo off
setlocal enabledelayedexpansion
goto init

:login
	(
		echo !usrname!
		echo !pssword!
		echo !subProblem!
		echo !filePath!
	) >"main\login.credential"
	goto :EOF
	
:init
	set /p usrname="Username: "
	set /p pssword="Password: "
	set /p filePath="File path: "
:submission
	set /p subProblem="Problem: "
	call :login
	pause
	main.py

	
	