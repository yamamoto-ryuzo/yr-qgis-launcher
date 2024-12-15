# -*- coding: utf-8 -*-

# インストール
# python本体
# https://www.python.org/downloads/
# インストール時【Add python.exe to PATH】にチャックを入れる
# pip install pyinstaller
# pip install keyboard
# アップデートがあるとき
# python.exe -m pip install --upgrade pip

# EXE作成
#　ディレクトリは適宜変更
# cd C:\github\yr-qgis-launcher
# pyinstaller ProjectFile.py --onefile --noconsole --distpath ./ --clean
#　完成したらC:\GoogleDrive\github\yr-qgis-portable-launcher2\QGIS_portable\ProjectFile.exeとかメッセージが出て完成
  
#デバッグ時の注意事項
#実行ファイル名は必ず　python.exe　となるので、環境設定は　python.config が必ず必要
#プロジェクトファイルは、そのため python.qgs となりエラーで問題なし

import auth

import os
import sys
import keyboard
import shutil
import subprocess
import tkinter as tk
from tkinter import scrolledtext
from tkinter import simpledialog, messagebox
import configparser
import time
import stat

# 独自インポート
import set_drive,auth
import VersionManager

# グローバル変数の定義
# portable_profileを複写する場合は　profile = 1　にイベントで変更
profile = 0
username = ''
userrole = ''
selected_version = ''
selected_profile = ''
qgisconfig_folder = ''
customUI = ''
setting = ''
# 実施に実行するQGIS本体を指定する変数
exeQGIS = ''

def write_to_ini(ini_file, username, userrole):
    # ConfigParserオブジェクトの作成
    config = configparser.ConfigParser()
    
    # 変数をconfigに追加
    config['variables'] = {
        'username': username,
        'userrole': userrole
    }
    
    # iniファイルに書き込み
    with open(ini_file, 'w') as configfile:
        config.write(configfile)

def list_current_directory_contents():
    try:
        # カレントフォルダのファイルとフォルダのリストを取得
        contents = os.listdir()
        return "\n".join(contents)
    except PermissionError:
        return "カレントフォルダへのアクセス権限がありません。"
    except Exception as e:
        return "エラーが発生しました: {}".format(e)

def show_directory_contents():
    # 新しいウィンドウを作成
    window = tk.Tk()
    window.title("フォルダの内容")

    # スクロール可能なテキストボックスを作成
    text_area = scrolledtext.ScrolledText(window, width=40, height=10)
    text_area.pack(expand=True, fill="both")

    # カレントフォルダの内容をテキストボックスに表示
    directory_contents = list_current_directory_contents()
    text_area.insert(tk.END, directory_contents)

    # ウィンドウを表示
    window.mainloop()


# プロジェクトファイルの起動用コンフィグ読込設定
def read_qgis_project_file_from_config(file_name):
    try:
        with open(file_name+".config", "r", encoding="utf-8") as f:
            lines = f.readlines()
            # qgis_project_file 通常はEXEのファイル名.qgs
            # 実行可能ファイルのパスを取得
            executable_path = sys.executable
            # ファイル名から拡張子を除いた部分を取得
            file_name_without_ext = os.path.splitext(os.path.basename(executable_path))[0]
            # 新しい拡張子(.qgs)を追加
            qgis_project_file = '../ProjectFiles/' + file_name_without_ext + '.qgs'

            qgisconfig_folder = None
            # 仮想ドライブの標準設定は　Q:ドライブ　とする。
            VirtualDrive = "Q:"

            for line in lines:
                # コメント行を無視する
                if line.startswith("#"):
                    continue
                if line.startswith("ProjectFile"):
                    # プロジェクトファイルのパスを取得
                    qgis_project_file = line.split("=")[1].strip()
                    # messagebox.showerror("プロジェクトファイルのパス情報", qgis_project_file)
                elif line.startswith("qgisconfig_folder"):
                    # QGIS 設定フォルダーのパスを取得
                    qgisconfig_folder = line.split("=")[1].strip()
                    # messagebox.showerror("QGIS 設定フォルダーのパス情報", qgisconfig_folder)
                # カスタム仮想ドライブの読込
                elif line.startswith("VirtualDrive"):
                    # 稼働ドライブを取得
                    VirtualDrive = line.split("=")[1].strip()
                    print (f"仮想ドライブの設定情報：{VirtualDrive}")
            return qgis_project_file, qgisconfig_folder ,VirtualDrive
    except Exception as e:
        print("設定ファイルの読み込み中にエラーが発生しました:", e)
        return None

# フォルダが存在するかどうかの確認
def check_folder_exists(folder_path):
    if os.path.exists(folder_path):
        if os.path.isdir(folder_path):
            return True
        else:
            # messagebox.showerror("エラー", f"'{folder_path}' は存在しますが、フォルダではありません。")
            return False
    else:
        # messagebox.showerror("エラー", f"フォルダ '{folder_path}' は存在しません。")
        return False

####################
#  MAINプログラム  #
###################
def main():
    ############################
    #   設定ファイルの読み込み   #
    ############################
    # 実行ファイルのパスを取得
    exe_path = sys.executable
    print (f"実行ファイル：{exe_path}")
    # ファイル名を取得し、拡張子を除去
    file_name = os.path.splitext(os.path.basename(exe_path))[0]
    print(f"実行ファイル名：{file_name}")
    
    # 通常は　　　　Projyect.config
    # デバック時は　python.config となるので注意！
    # QGISのプロジェクトファイルを設定ファイルから読み込む
    qgis_project_file, qgisconfig_folder , VirtualDrive = read_qgis_project_file_from_config(file_name)
    print (f"qgis_project_fileを設定しました：{qgis_project_file}")


    ############################
    #   仮想ドライブ環境の設定   #
    ############################
    # 一度仮想ドライブを削除
    subprocess.run(["subst", "/d" , VirtualDrive])
    # 現在の作業ディレクトリを VirtualDrive ドライブに指定
    # set_drive.change_drive() 
    # 現在のフォルダを取得する
    current_folder = os.getcwd()
    print (f"現在のフォルダを取得する", current_folder)
    # "/persistent:yes" オプションは、再起動後もドライブの割り当てを保持するためのものです
    subprocess.run(["subst",VirtualDrive, current_folder])
    # ドライブの設定をユーザーに通知する
    print (f"仮想ドライブの設定：{VirtualDrive}ドライブを設定しました。")
    # カレントディレクトリを VirtualDriveドライブに変更します。
    os.chdir( VirtualDrive + "\\" )
    DRV_LTR = os.getcwd()  
    print (f"現在の作業フォルダのパス：{DRV_LTR}")  

    ##############################
    # portableプロファイルを初期化 #
    ##############################
    # 予定のユーザープロファイルにportableフォルダーが存在しない場合は標準のqgisconfigを複写する
    # 実行で使いたいportableフォルダのパス
    # 環境変数を含むことを前提とする
    # 環境変数 %APPDATA%を含むフォルダのパス
    # 環境変数を展開して実際のパスに変換する
    print (f"コンフィグで指定されたポータブルqgisconfig_folderフォルダ:{qgisconfig_folder}")  
    if qgisconfig_folder == None:
        appdata = os.getenv('APPDATA')
        print (f"環境変数appdataフォルダ:{appdata}")  
        qgisconfig_folder = os.path.join(appdata, 'QGIS', 'QGIS3')
        print (f"実行・ポータブルprofilesフォルダqgisconfig_folder:{qgisconfig_folder}")  
    portable_profile_path = qgisconfig_folder
    print (f"実行・ポータブルprofilesフォルダ:{portable_profile_path}")  

    source_path = os.path.abspath('./portable_profile')
    print (f"配布用・ポータブルprofilesフォルダ:{source_path}")        
    # ポータブルプロファイルが存在しない場合にコピーする
    # 起動時に　'profile強制更新'　を選択
    if not os.path.exists(os.path.join(portable_profile_path,'profiles','portable')) or (selected_profile == 'profile強制更新'):
        print(f"profilesフォルダを初期化します：{portable_profile_path}")
        
         # 上書き許可でコピー
        shutil.copytree(source_path, portable_profile_path, dirs_exist_ok=True)
        print(f"profilesフォルダを初期化完了しました：{portable_profile_path}")
    
    ##############
    # QGISの起動 #
    #############
    print (f"実行するQGIS：{exeQGIS}")
    print (f"プロジェクトファイルのパス：{qgis_project_file}")  
    print (f"profilesフォルダ：{portable_profile_path}")  
    # qgis_project_file が存在するか確認
    # messagebox.showerror("qgis_project_file", qgis_project_file)
    if not os.path.exists(qgis_project_file):
        messagebox.showerror("警告", "指定されたQGISプロジェクトファイルは存在しません。\n無視してQGISを実行します。")

    # 9.6.1. コマンドラインと環境変数
    # https://docs.qgis.org/3.34/ja/docs/user_manual/introduction/qgis_configuration.html#command-line-and-environment-variables  
    # 標準のプロファイルは「portable」 
    if qgis_project_file is None:
        # 引数がない場合は新しい空のプロジェクトでQGISを起動
        subprocess.Popen([exeQGIS,'--globalsettingsfile' , setting ,'--customizationfile' , customUI , '--profiles-path' , portable_profile_path , '--profile', 'portable','--code', '../processing/scripts/startup.py'], shell=True)
    else:
        # 引数がある場合は指定されたプロジェクトファイルを開く
        subprocess.Popen([exeQGIS,'--globalsettingsfile' , setting ,'--customizationfile' , customUI , '--profiles-path' , portable_profile_path , '--profile', 'portable','--code', '../processing/scripts/startup.py' , '--project' , qgis_project_file], shell=True)


if __name__ == "__main__":
    #################
    #  システム更新  #
    #################
    VersionManager.main()
    
    ################
    #  認証を実施   #
    ################
    logged_in_user,user_role,exeQGIS,selected_profile= auth.run_login()
    print(f"ログインに成功しました。ユーザー名: {logged_in_user}, 権限: {user_role}, 実行するQGIS： {exeQGIS},プロファイル：{selected_profile}")
    # 環境変数などの設定
    setting = '../ini/qgis_global_settings.ini'
    # 関数を呼び出して値を書き込む
    write_to_ini('./ini/qgis_global_settings.ini', logged_in_user, user_role)

    # ユーザーインファーフェイスのカスタマイズ
    customUI = '../ini/' + user_role + 'UI_customization.ini'
    if logged_in_user:
        print(f"ログインに成功しました。ユーザー名: {logged_in_user}")
        auth.save_username_to_ini(logged_in_user)
        main()
    else:
        print("ログインに失敗しました。")

   
