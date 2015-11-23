@echo off
set sdk_path=
for /F "delims=" %%i in (android_sdk_path.config) do set sdk_path=%%i

set android=%sdk_path%\tools\android
set adb=%sdk_path%\platform-tools\adb
set gradlew=%sdk_path%\tools\templates\gradle\wrapper\gradlew
set appName=%1

cd %1
%android% update project -p .
ant clean
ant debug
cd ..