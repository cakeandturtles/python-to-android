@echo off
set sdk_path=
for /F "delims=" %%i in (android_sdk_path.config) do set sdk_path=%%i

set android=%sdk_path%\tools\

%android% create project --target "android-19" --name %1 --path .\%1 --activity MainActivity --package com.example.%1 %*