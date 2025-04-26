import os
import filecmp
import subprocess
import shutil
import sys

import tkinter as tk
from tkinter import messagebox

# pythonコンソールの文字化け対策
# chcp 65001を実行
subprocess.run('chcp 65001', shell=True, check=True)
# 標準出力のエンコーディングを設定
# sys.stdout.reconfigure(encoding='utf-8')

def read_version_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()
    data = {}
    folders = []
    # 【重要】invalid_charsによる文字列処理は必ず必要、削除しないように！
    # 　　　　削除により、ルートフォルダ全体がロボコピーされるなどOS全体に及ぶ重大なエラーとなる
    invalid_chars = '\\/*?:"<>|'
    for line in content:
        line = line.strip()
        # コメントまたは空行をスキップ
        if line.startswith('#') or not line:
            continue
        if '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            if key == 'folder':
                # 先頭に無効な文字がある場合のみ削除
                if any(value.startswith(char) for char in invalid_chars):
                    value = value.lstrip(invalid_chars)
                folders.append(value)
            else:
                data[key] = value
    data['folders'] = folders
    return data

def compare_version_files(main_path, local_path):
    main_version_file = os.path.join(main_path, "version.txt")
    local_version_file = os.path.join(local_path, "version.txt")

    if not os.path.exists(main_version_file) or not os.path.exists(local_version_file):
        print("エラー: version.txtファイルが見つかりません。")
        return False

    return not filecmp.cmp(main_version_file, local_version_file, shallow=False)

def display_absolute_paths(main_data_path, local_path, folders):
    print("\nロボコピーの対象フォルダー（絶対パス）:")
    for folder in folders:
        source_folder = os.path.join(main_data_path, folder)
        local_folder = os.path.join(local_path, folder)
        print(f"ソース: {source_folder}")
        print(f"コピー先: {local_folder}")
        print("---")

def robocopy_folders(source_path, local_path, folder):
    source_folder = os.path.normpath(os.path.join(source_path, folder))
    local_folder = os.path.normpath(os.path.join(local_path, folder))
    print(f"\nロボコピー実行中:")
    print(f"ソース: {source_folder}")
    print(f"コピー先: {local_folder}")
    command = [
        "robocopy",
        source_folder,
        local_folder,
        "/E",
        "/R:3",
        "/W:10",
        "/MT:8",
        "/UNILOG:NUL",
        "/TEE"
    ]
    
    process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True, encoding='utf-8', errors='replace')
    print("システム更新中。")
    for output in process.stdout:
        print(output.strip())

    return process.returncode


def main():
   # tkinterのルートウィンドウを作成（必要に応じて）
    root = tk.Tk()
    root.withdraw()  # メインウィンドウを非表示にする
    
    # version.txtファイルのパスを指定
    version_file = "./launcher/version.txt"

    # version.txtファイルから情報を読み込む
    data = read_version_file(version_file)

    version = data.get('version')
    main_data_path = data.get('main_data_path','')
    local_path = data.get('local_path', main_data_path)
    # 複数フォルダに対応
    folders = data.get('folders', [])

    print(f"バージョン: {version}")
    print(f"ソース: {main_data_path}")
    print(f"コピー先: {local_path}")
    print(f"変更対象フォルダ: {', '.join(folders)}")

    # ロボコピーの対象フォルダーを絶対パスで表示
    display_absolute_paths(main_data_path, local_path, folders)

    # local_pathのフォルダが存在するか確認
    if os.path.exists(local_path) and os.path.isdir(local_path):
        # local_pathのフォルダが存在する場合
        # ファイルの内容を比較
        if compare_version_files(main_data_path, local_path):
            print("\nversion.txtファイルの内容が異なります。")
            print("ロボコピーを実行します。")
            for folder in folders:
                robocopy_folders(main_data_path, local_path, folder)
            print("main_data_pathをlocal_pathにコピーします。")
            shutil.copy2(os.path.join(main_data_path, version_file), local_path)
        else:
            print("\nversion.txtファイルの内容が同じです。ロボコピーは不要です。")
    else:
        # local_pathのフォルダが存在しない場合
        print("初期インストールを開始します。")
        robocopy_folders(main_data_path, local_path, '')

if __name__ == "__main__":
     main()