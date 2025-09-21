@echo off
echo このファイルは名前を変更しました。
echo 新しいファイル: local-launcher.bat を使用してください。
pause
for /f "usebackq tokens=1* delims==" %%A in ("%CONFIG_FILE%") do (
    set "key=%%A"
    set "value=%%B"
    call set "value=%%value%%"
    if /i "!key!"=="SYNC_SRC" call set "SYNC_SRC=!value!"
    if /i "!key!"=="SYNC_DST" call set "SYNC_DST=!value!"
    if /i "!key!"=="QFIELD_VERSION" set "QFIELD_VERSION=!value!"
    if /i "!key!"=="QGIS_VERSION" set "QGIS_VERSION=!value!"
    if /i "!key!"=="EXCLUDE_DIRS" set "EXCLUDE_DIRS=!value!"
)

REM パスの前後空白を削除
for %%V in (SYNC_SRC SYNC_DST QFIELD_VERSION QGIS_VERSION ASYNC_DIRS EXCLUDE_DIRS) do (
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

REM --- ここでSYNC_SRCの値を確認 ---
echo [DEBUG] SYNC_SRC = [%SYNC_SRC%]
if not exist "%SYNC_SRC%\" (
    echo [ERROR] SYNC_SRCのパス "%SYNC_SRC%" が存在しません。
    pause
    exit /b 1
)

REM --- portable.ver を比較して必要なら portable_profile を同期 ---
set "LOCAL_PORTABLE_VER=%SYNC_SRC%\launcher\portable_profile\profiles\portable.ver"
set "USER_PORTABLE_VER=%APPDATA%\QGIS\QGIS3\profiles\portable.ver"
set "LOCAL_VER="
set "USER_VER="
if exist "%LOCAL_PORTABLE_VER%" (
    for /f "usebackq delims=" %%A in ("%LOCAL_PORTABLE_VER%") do set "LOCAL_VER=%%A"
)
if exist "%USER_PORTABLE_VER%" (
    for /f "usebackq delims=" %%A in ("%USER_PORTABLE_VER%") do set "USER_VER=%%A"
)
echo [DEBUG] local portable.ver = [%LOCAL_VER%]
echo [DEBUG] user  portable.ver = [%USER_VER%]
if defined LOCAL_VER (
    if not "%LOCAL_VER%"=="%USER_VER%" (
        echo portable.ver が異なるためユーザープロファイルへ portable_profile を配布します。
        echo コピー元: "%SYNC_SRC%\launcher\portable_profile"
        echo コピー先: "%APPDATA%\QGIS\QGIS3\"
        REM /E : サブディレクトリを含めてコピー（空ディレクトリ含む）、/XO: 既存より古いファイルは上書きしない
        robocopy "%SYNC_SRC%\launcher\portable_profile" "%APPDATA%\QGIS\QGIS3\" /E /Z /NP /R:2 /W:2 /NJH /NJS /MT:1 /XO

        REM --- robocopy実行後に portable.ver を簡潔に上書き複写 ---
        copy /Y "%SYNC_SRC%\launcher\portable_profile\profiles\portable.ver" "%APPDATA%\QGIS\QGIS3\profiles\portable.ver" >nul 2>nul

        if errorlevel 8 (
            echo エラー: ユーザープロファイルへの同期に失敗しました。
        ) else (
            echo ユーザープロファイルへの同期が完了しました。
        )
    ) else (
        echo portable_profile は最新です。同期は不要です。
    )
) else (
    echo ローカルの portable.ver が見つかりません: "%LOCAL_PORTABLE_VER%"
)


REM ローカルのバージョン情報を qgislocalsync.config から取得
set LOCAL_QFIELD_VERSION=
set LOCAL_QGIS_VERSION=
set LOCAL_CONFIG_FILE=%SYNC_DST%\local-launcher\qgislocalsync.config

if exist "%LOCAL_CONFIG_FILE%" (
    for /f "usebackq tokens=1* delims==" %%A in ("%LOCAL_CONFIG_FILE%") do (
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
set "XD_ARGS=/XD QField* QGIS*"
if defined EXCLUDE_DIRS (
    rem EXCLUDE_DIRS はスペース区切りを想定し、各要素を追加
    for %%E in (!EXCLUDE_DIRS!) do set "XD_ARGS=!XD_ARGS! %%E"
)
if defined XD_ARGS (
    robocopy "%SYNC_SRC%" "%SYNC_DST%" /MIR /Z /NP /R:2 /W:2 /NJH /NJS /MT:1 /XO %XD_ARGS%
else
    robocopy "%SYNC_SRC%" "%SYNC_DST%" /MIR /Z /NP /R:2 /W:2 /NJH /NJS /MT:1 /XO
)

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
        robocopy "%%F" "%SYNC_DST%\%%~nxF" /MIR /Z /NP /R:2 /W:2 /NJH /NJS /MT:1 /XO
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
            robocopy "%%F" "%SYNC_DST%\%%~nxF" /MIR /Z /NP /R:2 /W:2 /XO
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
            robocopy "%%F" "%SYNC_DST%\%%~nxF" /MIR /Z /NP /R:2 /W:2 /XO
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
if "%SYNC_DST%"=="" (
    echo SYNC_DST が設定されていません。
    pause
    exit /b 1
)
if not exist "%SYNC_DST%\" (
    echo 同期先ディレクトリが存在しません。作成します: "%SYNC_DST%"
    mkdir "%SYNC_DST%"
)
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

REM 常に主要変数をエコー
echo.
echo 同期元: [%SYNC_SRC%]
echo 同期先: [%SYNC_DST%]
echo QFieldバージョン: [%QFIELD_VERSION%]
echo QGISバージョン: [%QGIS_VERSION%]
echo 除外フォルダ: [%EXCLUDE_DIRS%]
echo ローカルQFieldバージョン: [%LOCAL_QFIELD_VERSION%]
echo ローカルQGISバージョン: [%LOCAL_QGIS_VERSION%]
echo.

REM デバッグ時のみEnterで閉じる、通常は即終了
if "%DEBUG%"=="1" (
    echo バッチ処理が完了しました。Enterキーで閉じます
    pause
)
endlocal