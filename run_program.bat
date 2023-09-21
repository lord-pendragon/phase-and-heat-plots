@echo off
setlocal

:menu
echo.
echo 1. Run hello_world.py
echo 2. Run tests
echo 3. Simulations Menu
echo 4. Clear screen
echo 0. Exit
echo.

set /p choice="Enter your choice: "

if "%choice%"=="1" goto run_hello
if "%choice%"=="2" goto run_tests
if "%choice%"=="3" goto simulations
if "%choice%"=="4" goto clear_screen_menu
if "%choice%"=="0" goto end

goto menu

:clear_screen_menu
cls
goto menu

:clear_screen_sim
cls
goto simulations

:simulations
cls
echo.
echo 1. Run Support (Not Implemented)
echo 2. Run Planar
echo 3. Clear screen
echo 0. Back to Menu
echo.

set /p choice="Enter your choice: "

if "%choice%"=="2" goto planar
if "%choice%"=="3" goto clear_screen_sim
if "%choice%"=="0" goto menu

:planar
cd bin
echo Running Planar.py...
python run_Planar.py
cd ..
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
