@echo off
set sdk_path=
for /F "delims=" %%i in (android_sdk_path.config) do set sdk_path=%%i

set android=%sdk_path%\tools\android

%android% list targets %*