set ARG_1="--model=mobilenet_thin"
set ARG_2="--resize=432x368"
set ARG_3="--image=C:\Users\Taha\Desktop\PROJECT\tf-pose-estimation\images\ansys.jpeg"

for %%f in (C:\Users\Taha\Desktop\tennis\*) do @echo %%f

@ECHO OFF
setlocal enabledelayedexpansion
for %%f in (C:\Users\Taha\Desktop\tennis\*) do (
  set /p val=<%%f
  echo "fullname: %%f"
  echo "name: %%~nf"
  echo "contents: !val!"
)

for %%f in (C:\Users\Taha\Desktop\tennis\*) do (
  py C:\Users\Taha\Desktop\PROJECT\tf-pose-estimation\run.py %ARG_1% %ARG_2% --image=%%f
)

pause