@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

REM --- BOXなどの環境変数をここで定義してください ---
REM 例: set BOX_ROOT=%USERPROFILE%\Box
if "%BOX_ROOT%"=="" (
    set "BOX_ROOT=%USERPROFILE%\Box"
)
REM ---------------------------------------------------

REM ※このバッチファイルはUTF-8(BOMなし)で保存してください
REM デバッグ用: 1にすると各コマンドを表示
set DEBUG=0

REM デバッグモードONの場合、echo onにする
if "%DEBUG%"=="1" (
    echo デバッグモード: ON
    echo.
    @echo on
)

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
    REM 環境変数を明示的に展開
    call set "value=%%value%%"
    if /i "!key!"=="SYNC_SRC" call set "SYNC_SRC=!value!"
    if /i "!key!"=="SYNC_DST" call set "SYNC_DST=!value!"
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

REM robocopyの /NJH /NJS /MT:1 オプション追加で詳細表示とマルチスレッド無効化
REM コピー元・先のパスやフォルダ名に日本語やスペースが含まれる場合は、robocopyのバージョンや環境依存で失敗することがあります。
REM 対策例:
REM 1. コマンドプロンプトのコードページを chcp 932 に設定（既に対応済み）
REM 2. robocopyのパスを "" で囲む（既に対応済み）
REM 3. パスの途中に「.」や「\」の重複、末尾スペースがないか確認
REM 4. ネットワークドライブやOneDrive/Box等の特殊な同期フォルダは権限やロックに注意

REM トップレベルのファイルをrobocopyで同期（除外指定があれば除外）
robocopy "%SYNC_SRC%" "%SYNC_DST%" /MIR /Z /NP /R:2 /W:2 /NJH /NJS /MT:1 /XD QField* QGIS* !EXCLUDE_DIRS!

REM QField*/QGIS*以外のフォルダを個別に同期（除外指定があれば除外）
for /d %%F in ("%SYNC_SRC%\*") do (
    set "FOLDER=%%~nxF"
    set "SYNC=1"
    if /i "!FOLDER:~0,6!"=="QField" set "SYNC=0"
    if /i "!FOLDER:~0,4!"=="QGIS" set "SYNC=0"
    for %%E in (!EXCLUDE_DIRS!) do (
        if /i "!FOLDER!"=="%%E" set "SYNC=0"
    )
    if !SYNC! equ 1 (
        echo フォルダコピー中: "%%F" → "%SYNC_DST%\%%~nxF"
        robocopy "%%F" "%SYNC_DST%\%%~nxF" /MIR /Z /NP /R:2 /W:2 /NJH /NJS /MT:1
        if errorlevel 8 (
            echo エラー: "%%F" のコピーに失敗しました。パスや権限、ファイル名を確認してください。
        )
    )
)

REM QFieldバージョンが違う場合のみ同期
if not "%QFIELD_VERSION%"=="%LOCAL_QFIELD_VERSION%" (
    echo QFieldバージョンが異なるため同期します。
    set "QFIELD_SYNCED=0"
    for /d %%F in ("%SYNC_SRC%\QField*") do (
        if exist "%%F" (
            robocopy "%%F" "%SYNC_DST%\%%~nxF" /MIR /Z /NP /R:2 /W:2
            set "QFIELD_SYNCED=1"
        )
    )
    if "!QFIELD_SYNCED!"=="0" (
        echo QFieldフォルダが同期元に見つかりません。
    )
) else (
    echo QFieldバージョンが同じのため同期しません。
)

REM QGISバージョンが違う場合のみ同期
if not "%QGIS_VERSION%"=="%LOCAL_QGIS_VERSION%" (
    echo QGISバージョンが異なるため同期します。
    set "QGIS_SYNCED=0"
    for /d %%F in ("%SYNC_SRC%\QGIS*") do (
        if exist "%%F" (
            robocopy "%%F" "%SYNC_DST%\%%~nxF" /MIR /Z /NP /R:2 /W:2
            set "QGIS_SYNCED=1"
        )
    )
    if "!QGIS_SYNCED!"=="0" (
        echo QGISフォルダが同期元に見つかりません。
    )
) else (
    echo QGISバージョンが同じのため同期しません。
)

REM ProjectFile.exeの起動前に存在確認とデバッグ出力
pushd "%SYNC_DST%"
echo --- %SYNC_DST% の内容を表示 ---
dir
if exist ProjectFile.exe (
    echo ProjectFile.exeを起動します...
    start "" "ProjectFile.exe"
) else (
    echo ProjectFile.exeが見つかりません。
    pause
)
popd

REM デバッグ用: 主要変数の内容を表示
if "%DEBUG%"=="1" (
    echo 同期元: [%SYNC_SRC%]
    echo 同期先: [%SYNC_DST%]
    echo QFieldバージョン: [%QFIELD_VERSION%]
    echo QGISバージョン: [%QGIS_VERSION%]
    echo 除外フォルダ: [%EXCLUDE_DIRS%]
    echo ローカルQFieldバージョン: [%LOCAL_QFIELD_VERSION%]
    echo ローカルQGISバージョン: [%LOCAL_QGIS_VERSION%]
    echo.
)

REM 各robocopy実行前にコマンド内容を表示（デバッグ時のみ）
REM 例:
REM if "%DEBUG%"=="1" echo robocopy "%%F" "%SYNC_DST%\%%~nxF" /MIR /Z /NP /R:2 /W:2 /NJH /NJS /MT:1

REM 終了時に一時停止（デバッグ時のみ）
if "%DEBUG%"=="1" (
    echo.
    echo デバッグ終了: Enterキーで閉じます
    pause
)
endlocal
