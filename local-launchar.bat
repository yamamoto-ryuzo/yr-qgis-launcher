@echo off
setlocal enabledelayedexpansion

REM BOXなどの環境変数を利用してパスを動的に設定
REM 例: set BOX_ROOT=%USERPROFILE%\Box
REM 必要に応じて環境変数を事前に設定しておくこと

REM 設定ファイルのパス
set CONFIG_FILE=%~dp0local-launcher\qgislocalsync.config

REM 初期化
set SYNC_SRC=
set SYNC_DST=
set QFIELD_VERSION=
set QGIS_VERSION=
set ASYNC_DIRS=
set EXCLUDE_DIRS=

REM 設定ファイルからパスとバージョン・除外フォルダを取得（環境変数展開対応）
for /f "usebackq tokens=1,2 delims==" %%A in ("%CONFIG_FILE%") do (
    set "key=%%A"
    set "value=%%B"
    call set "value=%%value%%"
    if /i "!key!"=="SYNC_SRC" set "SYNC_SRC=!value!"
    if /i "!key!"=="SYNC_DST" set "SYNC_DST=!value!"
    if /i "!key!"=="QFIELD_VERSION" set "QFIELD_VERSION=!value!"
    if /i "!key!"=="QGIS_VERSION" set "QGIS_VERSION=!value!"
    if /i "!key!"=="EXCLUDE_DIRS" set "EXCLUDE_DIRS=!value!"
)

REM パスの前後空白を削除
for %%V in (SYNC_SRC SYNC_DST QFIELD_VERSION QGIS_VERSION ASYNC_DIRS) do (
    set "val=!%%V!"
    for /f "tokens=* delims= " %%X in ("!val!") do set "%%V=%%X"
)

REM パスが取得できているか確認
if "%SYNC_SRC%"=="" (
    echo SYNC_SRCが設定ファイルにありません。
    pause
    exit /b 1
)
if "%SYNC_DST%"=="" (
    echo SYNC_DSTが設定ファイルにありません。
    pause
    exit /b 1
)

REM ローカルのバージョン情報を qgislocalsync.config から取得
set LOCAL_QFIELD_VERSION=
set LOCAL_QGIS_VERSION=
set LOCAL_CONFIG_FILE=%SYNC_DST%\local-launcher\qgislocalsync.config

if exist "%LOCAL_CONFIG_FILE%" (
    for /f "usebackq tokens=1,2 delims==" %%A in ("%LOCAL_CONFIG_FILE%") do (
        set "key=%%A"
        set "value=%%B"
        if /i "!key!"=="QFIELD_VERSION" set "LOCAL_QFIELD_VERSION=!value!"
        if /i "!key!"=="QGIS_VERSION" set "LOCAL_QGIS_VERSION=!value!"
    )
)

REM QField*/QGIS*以外のフォルダを同期（除外指定があれば除外）
for /d %%F in ("%SYNC_SRC%\*") do (
    set "FOLDER=%%~nxF"
    set "SYNC=1"
    if /i "!FOLDER:~0,6!"=="QField" set "SYNC=0"
    if /i "!FOLDER:~0,4!"=="QGIS" set "SYNC=0"
    REM EXCLUDE_DIRSで指定されたフォルダ名は同期しない
    for %%E in (!EXCLUDE_DIRS!) do (
        if /i "!FOLDER!"=="%%E" set "SYNC=0"
    )
    if !SYNC! equ 1 (
        robocopy "%%F" "%SYNC_DST%\%%~nxF" /MIR /Z /NP /R:2 /W:2
    )
)

REM ASYNC_DIRSで指定されたフォルダを常に同期
for %%D in (!ASYNC_DIRS!) do (
    if exist "%SYNC_SRC%\%%D" (
        robocopy "%SYNC_SRC%\%%D" "%SYNC_DST%\%%D" /MIR /Z /NP /R:2 /W:2
    )
)

REM QFieldバージョンが違う場合のみ同期
if not "%QFIELD_VERSION%"=="%LOCAL_QFIELD_VERSION%" (
    echo QFieldバージョンが異なるため同期します。
    for /d %%F in ("%SYNC_SRC%\QField*") do (
        robocopy "%%F" "%SYNC_DST%\%%~nxF" /MIR /Z /NP /R:2 /W:2
    )
) else (
    echo QFieldバージョンが同じのため同期しません。
)

REM QGISバージョンが違う場合のみ同期
if not "%QGIS_VERSION%"=="%LOCAL_QGIS_VERSION%" (
    echo QGISバージョンが異なるため同期します。
    for /d %%F in ("%SYNC_SRC%\QGIS*") do (
        robocopy "%%F" "%SYNC_DST%\%%~nxF" /MIR /Z /NP /R:2 /W:2
    )
) else (
    echo QGISバージョンが同じのため同期しません。
)

REM ProjectFile.exeの起動
pushd "%SYNC_DST%"
if exist ProjectFile.exe (
    start "" ProjectFile.exe
) else (
    echo ProjectFile.exeが見つかりません。
    pause
)
popd

endlocal
