@echo off
set command=%1
set name=%2

::get the rest of the arguments
shift
shift
set args=
:parse_args
if "%1" NEQ "" (
    set args=%args% %1
    shift
    goto :parse_args
)

::get android sdk path from config file
set sdk_path=
for /F "delims=" %%i in (android_sdk_path.config) do set sdk_path=%%i

set android=%sdk_path%\tools\android.bat
set adb=%sdk_path%\platform-tools\adb.exe

::NOW START THE INDIVIDUAL COMMANDS

if "%command%"=="list" %android% list targets %args%

if "%command%"=="create" (
    %android% create project --target "android-19" --name %name% --path .\%name% --activity MainActivity --package com.example.%name% %args%
)

if "%command%"=="build" (
    cd %name%
    call %android% update project -p .
    call ant clean
    call ant debug
    call cd ..
)

if "%command%"=="run" (
    %adb% install %name%/bin/%name%-debug.apk
)