import os
import filecmp
import subprocess

def read_version_file(file_path):
    with open(file_path, 'r') as f:
        content = f.readlines()
    data = {}
    folders = []
    for line in content:
        if '=' in line:
            key, value = line.strip().split('=')
            key = key.strip()
            value = value.strip()
            if key == 'folder':
                # 【重要】この処理は必ず必要、削除しないように！
                # 　　　　削除により、ルートフォルダ全体がロボコピーされるなど重大なエラ
                value = value.lstrip('\\/*?:"<>|')
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
        source_folder = os.path.join(os.path.join(main_data_path, folder))
        local_folder = os.path.join(os.path.join(local_path, folder))
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
        "/MT:8"
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    print(f"\n{folder}のコピー結果:")
    print(result.stdout)
    if result.stderr:
        print("エラー:", result.stderr)
    print("---")

def main():
    # version.txtファイルのパスを指定
    version_file = "version.txt"

    # version.txtファイルから情報を読み込む
    data = read_version_file(version_file)

    version = data.get('version')
    main_data_path = data.get('main_data_path')
    local_path = data.get('local_path')
    folders = data.get('folders', [])

    print(f"バージョン: {version}")
    print(f"ソース: {main_data_path}")
    print(f"コピー先: {local_path}")
    print(f"変更対象フォルダ: {', '.join(folders)}")

    # ロボコピーの対象フォルダーを絶対パスで表示
    display_absolute_paths(main_data_path, local_path, folders)

    # ファイルの内容を比較
    if compare_version_files(main_data_path, local_path):
        print("\nversion.txtファイルの内容が異なります。")
        print("ロボコピーを実行します。")
        for folder in folders:
            print(f"変更対象フォルダ: {', '.join(folders)}")
            # robocopy_folders(main_data_path, local_path, folder)
    else:
        print("\nversion.txtファイルの内容が同じです。ロボコピーは不要です。")

if __name__ == "__main__":
    main()