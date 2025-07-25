@echo off
REM === BOXからZIPをダウンロードして解凍する初期インストールバッチ ===

REM ▼設定（必要に応じて編集）
set "BOX_ZIP_URL=https://example.box.com/s/xxxxxxxxxxxxxxxxxxxx/download"  REM ←BOXのダウンロードURLに書き換えてください
set "ZIP_FILE=%TEMP%\box_download.zip"
REM ▼qgislocalsync.configからSYNC_DSTを取得
set "CONFIG_FILE=%~dp0local-launcher\qgislocalsync.config"
for /f "usebackq tokens=1,2 delims==" %%A in ("%CONFIG_FILE%") do (
    if /i "%%A"=="SYNC_DST" set "EXTRACT_TO=%%B"
)
if "%EXTRACT_TO%"=="" (
    echo SYNC_DSTがqgislocalsync.configから取得できませんでした。
    pause
    exit /b 1
)

REM ▼ダウンロード
echo BOXからZIPをダウンロード中...
powershell -Command "Invoke-WebRequest -Uri '%BOX_ZIP_URL%' -OutFile '%ZIP_FILE%'"
if errorlevel 1 (
    echo ダウンロードに失敗しました。
    pause
    exit /b 1
)

REM ▼解凍
echo ZIPを解凍中...
powershell -Command "Expand-Archive -Path '%ZIP_FILE%' -DestinationPath '%EXTRACT_TO%' -Force"
if errorlevel 1 (
    echo 解凍に失敗しました。
    pause
    exit /b 1
)

REM ▼後処理
del "%ZIP_FILE%"
echo 完了しました。解凍先: %EXTRACT_TO%
pause
