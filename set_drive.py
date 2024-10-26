import os
import subprocess

def remove_virtual_drive(drive_letter):
    """
    仮想ドライブを解除する関数
    :param drive_letter: 解除する仮想ドライブのドライブレター
    """
    try:
        # 仮想ドライブを解除する
        subprocess.run(["subst", drive_letter + ":", "/d"], check=True)
        print(f"仮想ドライブ '{drive_letter}:' が解除されました")
    except subprocess.CalledProcessError as e:
        print(f"仮想ドライブ '{drive_letter}:' の解除に失敗しました:", e)

# 仮想ドライブのマウント状態を取得する関数
def get_virtual_drive_mount_status(drive_letter):
    return os.path.exists(drive_letter + ':')

# 仮想ドライブに関連付けられたフォルダのファイル一覧を取得する関数
def get_virtual_drive_files(drive_letter):
    virtual_drive_folder_path = drive_letter + ':\\'
    if get_virtual_drive_mount_status(drive_letter):
        return os.listdir(virtual_drive_folder_path)
    else:
        return None 

def change_current_drive(drive_letter):
    """
    カレントドライブを指定したドライブに変更する関数
    :param drive_letter: 変更するカレントドライブのドライブレター
    """
    try:
        os.chdir(drive_letter + ":\\")
        print(f"カレントドライブが '{drive_letter}:' に変更されました")
    except FileNotFoundError:
        print(f"'{drive_letter}:' は存在しないドライブです")
    except Exception as e:
        print(f"カレントドライブの変更中にエラーが発生しました:", e)

def change_drive():
    # STEP.1: 現在のフォルダを取得
    current_folder = os.getcwd()
    print(f"現在のカレントフォルダは {current_folder} です")

    # カレントディレクトリ内の全てのファイルおよびディレクトリのリストを取得
    directory_contents = os.listdir()
    # リストを表示
    print(f"カレントフォルダ内のファイルおよびディレクトリ一覧:'{directory_contents}")

    # 仮想ドライブのドライブレターを指定
    drive_letter = 'Q'
    # 仮想ドライブに関連付けられたフォルダのファイル一覧を取得
    files_in_virtual_drive = get_virtual_drive_files(drive_letter)
    if files_in_virtual_drive:
        print(f"仮想ドライブに関連付けられたフォルダのファイル一覧:'{files_in_virtual_drive}'")
    else:
        print("仮想ドライブはマウントされていません")
        # "/persistent:yes" は、再起動後もドライブの割り当てを保持するためのオプション
        subprocess.run(["subst", "Q:", current_folder,"/persistent:yes"])
        print("Q ドライブに割り当てが完了しました")        

    if directory_contents == files_in_virtual_drive:
        print("Q ドライブはすでに割り当てられています")
        # カレントドライブをQドライブに変更
        change_current_drive('Q')

if __name__ == "__main__":
    # 事前に Q ドライブが存在する場合は解除しておく
    #print("Q ドライブの解除を試みます...")
    #remove_virtual_drive('Q')
    # メイン関数を実行
    change_drive()
