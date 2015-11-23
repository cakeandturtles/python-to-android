@echo off
set sdk_path=
for /F "delims=" %%i in (android_sdk_path.config) do set sdk_path=%%i

set android=%sdk_path%\tools\android
set adb=%sdk_path%\platform-tools\adb

%adb% install %1/bin/%1-debug.apk