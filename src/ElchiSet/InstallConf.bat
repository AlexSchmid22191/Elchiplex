@echo off
:: --- Set target folder ---
set "targetDir=%APPDATA%\ElchWorks\ElchiMux"

:: --- Create folder if it doesn't exist ---
if not exist "%targetDir%" (
    mkdir "%targetDir%"
)

:: --- Define config file path ---
set "configFile=%targetDir%\config.yaml"

:: --- Create the config file with default contents ---
(
echo # Configuration for ElchiMux
echo device:
echo   type: Omniplex
echo   port: COMXY
echo 1:
echo   L1R1: 0
echo   L2R1: 0
echo   L3R1: 0
echo   L4R1: 0
echo   L1R2: 0
echo   L2R2: 0
echo   L3R2: 0
echo   L4R2: 0
echo   L1R3: 0
echo   L2R3: 0
echo   L3R3: 0
echo   L4R3: 0
echo   L1R4: 0
echo   L2R4: 0
echo   L3R4: 0
echo   L4R4: 0
echo 2:
echo   L1R1: 1
echo   L2R1: 1
echo   L3R1: 1
echo   L4R1: 1
echo   L1R2: 1
echo   L2R2: 1
echo   L3R2: 1
echo   L4R2: 1
echo   L1R3: 1
echo   L2R3: 1
echo   L3R3: 1
echo   L4R3: 1
echo   L1R4: 1
echo   L2R4: 1
echo   L3R4: 1
echo   L4R4: 1
) > "%configFile%"

echo Config file created at "%configFile%"
exit /b 0