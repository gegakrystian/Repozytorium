@echo off
tile Logowanie
color 2

:logowanie
echo.
echo Zaloguj sie
set /p login=Login:
if %login%==poprawnylogin goto haslo
goto blad

:haslo
cls
echo.
set /p haslo=Haslo:
if %haslo%==poprawnehaslo goto zalogowano

:zalogowano
cls
echo Zalogowany
echo.
echo Kliknij dowolny klawisz, aby sie wylogowac
pause
goto logowanie

:blad
echo Blad
pause 
goto logowanie