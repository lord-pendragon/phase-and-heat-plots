@echo off
setlocal

:menu
echo.
echo 1. Run hello_world.py
echo 2. Run tests
echo 3. Clear screen
echo 0. Exit
echo.

set /p choice="Enter your choice: "

if "%choice%"=="1" goto run_hello
if "%choice%"=="2" goto run_tests
if "%choice%"=="3" goto clear_screen
if "%choice%"=="0" goto end

goto menu

:clear_screen
cls
goto menu

:run_hello
echo Running Program...
python src\hello_world.py
goto menu

:run_tests
cd tests
echo Running Tests...
python -m unittest discover
cd ..
goto menu

:end
exit /b
