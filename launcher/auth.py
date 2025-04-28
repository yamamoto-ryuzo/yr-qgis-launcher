import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import sys
import os
import configparser
import winreg
import webbrowser
import subprocess

# 独自インポート
import ProjectFile

# バージョン選択格納用のカスタムコンボボックスの定義
class CustomCombobox(ttk.Combobox):
    def __init__(self, master, **kw):
        self.display_values = kw.pop('display_values', [])
        self.actual_values = kw.pop('actual_values', [])
        ttk.Combobox.__init__(self, master, **kw)
        self['values'] = self.display_values

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def save_auth_data_to_ini(username, qgis_version, qgis_display_version, user_role, selected_profile, selected_project_file):
    config = configparser.ConfigParser()
    config['Auth'] = {
        'username': username,
        'qgis_version': qgis_version,
        'qgis_display_version': qgis_display_version,
        'user_role': user_role,
        'selected_profile': selected_profile,
        'selected_project_file': selected_project_file
    }
    with open('./launcher/ini/auth.ini', 'w') as configfile:
        config.write(configfile)

def get_associated_app(extension):
    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, f'.{extension}') as key:
            prog_id = winreg.QueryValue(key, '')
        
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, f'{prog_id}\\shell\\open\\command') as key:
            command = winreg.QueryValue(key, '')
        
        app_path = command.split('"')[1]
        
        return app_path if os.path.exists(app_path) else ''
    except WindowsError:
        return ''

def open_qgis_website():
    webbrowser.open("https://qgis.org/")

def get_qgis_project_files(directory):
    """指定されたディレクトリ内のQGISプロジェクトファイル（.qgs, .qgz）の一覧を取得する"""
    project_files = []
    for file in os.listdir(directory):
        if file.endswith('.qgs') or file.endswith('.qgz'):
            project_files.append(file)
    return project_files

def get_qgis_project_files_from_all_project_dirs():
    """Projectで始まる全フォルダ内のQGISプロジェクトファイル（.qgs, .qgz）の一覧を取得する"""
    project_files = []
    cwd = os.getcwd()
    for folder in os.listdir(cwd):
        if folder.startswith('Project') and os.path.isdir(os.path.join(cwd, folder)):
            folder_path = os.path.join(cwd, folder)
            for file in os.listdir(folder_path):
                if file.endswith('.qgs') or file.endswith('.qgz'):
                    # フォルダ名も含めて返す
                    project_files.append(os.path.join(folder, file))
    return project_files

def get_program_files_dir():
    try:
        app_path = get_associated_app('qgs')
        print("QGISインストール版のレジストリ登録フォルダは：", app_path)
        if (app_path):
            # QGIS*のある前までのフォルダを取得
            qgis_folder_index = app_path.lower().find('qgis')
            if (qgis_folder_index != -1):
                return app_path[:qgis_folder_index]
            else:
                return os.path.dirname(os.path.dirname(os.path.dirname(app_path)))
        else:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion") as key:
                program_files_dir = winreg.QueryValueEx(key, "ProgramFilesDir")[0]
            return program_files_dir
    except WindowsError:
        return "C:\\Program Files"

def search_installed_qgis():
    """
    インストールされているQGISおよびQFieldの実行ファイルを検索する関数。
    QGISおよびQFieldのインストールディレクトリを探し、バージョンごとの実行ファイルパスをリストに追加する。

    Returns:
        list: インストールされているQGISおよびQFieldの実行ファイルパスのリスト。
    """
    qgis_executables = []
    base_dir = get_program_files_dir()  # プログラムファイルディレクトリを取得
    qgis_folders = [item for item in os.listdir(base_dir) if item.startswith('QGIS') and os.path.isdir(os.path.join(base_dir, item))]
    qfield_folders = [item for item in os.listdir(base_dir) if item.startswith('QField') and os.path.isdir(os.path.join(base_dir, item))]
    
    # 各QGISフォルダを検索
    for folder in qgis_folders:
        print(f"検索したフォルダ: {folder}")
        folder_path_qt5 = os.path.join(base_dir, folder, 'bin', 'qgis.bat')  # QGIS 3.x (Qt5) の実行ファイルパス
        folder_path_qt6 = os.path.join(base_dir, folder, 'bin', 'qgis-qt6.bat')  # QGIS 3.x (Qt6) の実行ファイルパス
        
        # 実行ファイルが存在する場合、リストに追加
        if os.path.exists(folder_path_qt5):
            qgis_executables.append(folder_path_qt5)
        if os.path.exists(folder_path_qt6):
            qgis_executables.append(folder_path_qt6)
    
    # 各QFieldフォルダを検索
    for folder in qfield_folders:
        print(f"検索したQFieldフォルダ: {folder}")
        folder_path_qfield = os.path.join(base_dir, folder, 'usr', 'bin', 'qfield.exe')  # QFieldの実行ファイルパス
        
        # 実行ファイルが存在する場合、リストに追加
        if os.path.exists(folder_path_qfield):
            qgis_executables.append(folder_path_qfield)
    
    return qgis_executables

def get_qgis_versions():
    versions = [[], []]
    
    def add_column(value1, value2):
        versions[0].append(value1)
        versions[1].append(value2)
    
    # インストール版の確認
    qgis_executables = search_installed_qgis()
    for exe in qgis_executables:
        folder = os.path.basename(os.path.dirname(os.path.dirname(exe)))
        if 'qfield' in exe.lower():
            add_column(f'QFieldインストール版 ({folder})', exe)
        else:
            add_column(f'インストール版 ({folder})', exe)
        print(f"{folder}が見つかりました：", versions[0][-1])
        print("フォルダのパス：", versions[1][-1])
    
    # ポータブル版の確認
    qgis_folders = [item for item in os.listdir() if item.startswith('QGIS') and os.path.isdir(item)]
    for folder in qgis_folders:
        DRV_LTR = os.getcwd()
        OSGEO4W_ROOT = os.path.join(DRV_LTR, folder, 'qgis')
        folder_path = os.path.join(OSGEO4W_ROOT, 'apps', 'qgis-ltr')
        QGIS_Type = 'qgis-ltr' if os.path.exists(folder_path) else 'qgis'
        program_path = os.path.join(OSGEO4W_ROOT, 'bin', f"{QGIS_Type}.bat")
        add_column(f'ポータブル版 ({folder})', program_path)
        print("QGISポータブル版が見つかりました：", versions[0][-1])
        print("QGISフォルダのパス：", versions[1][-1])
        # システムパスにQGIS関連のフォルダを追加
        os.environ['PATH'] += os.pathsep + os.path.join(OSGEO4W_ROOT, 'apps', QGIS_Type, 'bin')
        os.environ['PATH'] += os.pathsep + os.path.join(OSGEO4W_ROOT, 'apps')
        os.environ['PATH'] += os.pathsep + os.path.join(OSGEO4W_ROOT, 'bin')
        os.environ['PATH'] += os.pathsep + os.path.join(OSGEO4W_ROOT, 'apps', 'grass')
    
    # QFieldのポータブル版の確認
    qfield_folders = [item for item in os.listdir() if item.startswith('QField') and os.path.isdir(item)]
    for folder in qfield_folders:
        DRV_LTR = os.getcwd()
        QFIELD_ROOT = os.path.join(DRV_LTR, folder)
        program_path = os.path.join(QFIELD_ROOT, 'usr', 'bin', 'qfield.exe')
        add_column(f'QFieldポータブル版 ({folder})', program_path)
        print("QFieldポータブル版が見つかりました：", versions[0][-1])
        print("QFieldフォルダのパス：", versions[1][-1])
        # システムパスにQField関連のフォルダを追加
        os.environ['PATH'] += os.pathsep + os.path.join(QFIELD_ROOT, 'usr', 'bin')
    
    # バージョンを数値の大きいほうから並べる
    if versions[0] and versions[1]:
        versions[0], versions[1] = zip(*sorted(zip(versions[0], versions[1]), key=lambda x: x[0], reverse=True))
        versions = [list(versions[0]), list(versions[1])]
    else:
        versions = [[], []]
    
    return versions

def get_auth_data_from_ini():
    config = configparser.ConfigParser()
    auth_ini_path = os.path.join(os.getcwd(),'launcher','ini', 'auth.ini')
    print("get_auth_data_from_iniにおけるカレントディレクトリ：", os.getcwd())
    encodings = ['utf-8', 'cp932', 'shift_jis']
    for encoding in encodings:
        try:
            with open(auth_ini_path, 'r', encoding=encoding) as file:
                config.read_file(file)
            break
        except UnicodeDecodeError:
            continue
    auth_data = {
        'username': config.get('Auth', 'username', fallback=''),
        'qgis_version': config.get('Auth', 'qgis_version', fallback=''),
        'qgis_display_version': config.get('Auth', 'qgis_display_version', fallback=''),
        'user_role': config.get('Auth', 'user_role', fallback=''),
        'selected_profile': config.get('Auth', 'selected_profile', fallback=''),
        'selected_project_file': config.get('Auth', 'selected_project_file', fallback='')
    }
    print(f"読み込んだ認証データ: {auth_data}")
    return auth_data

# グローバル変数の定義
version_combo = None

def create_login_window():
    global version_combo
    root = tk.Tk()
    root.title("ログインフォーム")
    center_window(root, 390, 390)  # ウィンドウサイズを1.3倍に変更

    login_attempts = 0
    max_attempts = 10
    logged_in_user = None
    user_role = None
    selected_version = None
    selected_display_version = None
    selected_profile = None
    selected_project_file = None

    auth_data = get_auth_data_from_ini()

    def focus_password(event):
        password_entry.focus()

    def focus_version_combo(event):
        version_combo.focus()

    def focus_profile_combo(event):
        profile_combo.focus()

    def focus_login_button(event):
        login_button.focus()

    def validate_login(event=None):
        nonlocal login_attempts, logged_in_user, user_role, selected_version, selected_display_version, selected_profile, selected_project_file

        entered_username = username_entry.get()
        entered_password = password_entry.get()
        selected_version_index = version_combo.current()
        selected_version = version_combo.actual_values[selected_version_index]
        selected_display_version = version_combo.display_values[selected_version_index]
        print(f"【選択された表示バージョン: {selected_display_version}】")
        selected_profile = profile_combo.get()
        
        try:
            with open('launcher/auth.config', 'r') as config_file:
                config = json.load(config_file)
        except FileNotFoundError:
            messagebox.showerror("エラー", "設定ファイルが見つかりません。")
            root.quit()
            return
        except json.JSONDecodeError:
            messagebox.showerror("エラー", "設定ファイルの形式が正しくありません。")
            root.quit()
            return

        users = config.get('users', [])
        valid_user = next((user for user in users if user['username'] == entered_username and user['password'] == entered_password), None)

        if valid_user:
            messagebox.showinfo("ログイン成功", f"ようこそ、{entered_username}さん!\n あなたの権限は {valid_user['userrole']}です。\n 選択されたバージョン: {version_combo.get()}\n 選択されたプロファイル: {selected_profile}")
            logged_in_user = entered_username
            user_role = valid_user['userrole']
            selected_project_file = project_combo.get()
            root.quit()
        else:
            login_attempts += 1
            remaining_attempts = max_attempts - login_attempts
            if remaining_attempts > 0:
                messagebox.showerror("ログイン失敗", f"ユーザー名またはパスワードが無効です。\n残り試行回数: {remaining_attempts}")
                clear_entries()
            else:
                messagebox.showerror("ログイン失敗", "試行回数の上限に達しました。プログラムを終了します。")
                root.quit()
                sys.exit()

    def clear_entries():
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        username_entry.focus()
        
    # ================ プロジェクトファイルの選択 ===================
    tk.Label(root, text="プロジェクトファイル選択:", font=("TkDefaultFont", 13)).pack()
    project_var = tk.StringVar()
    project_files = get_qgis_project_files_from_all_project_dirs()
    project_combo = ttk.Combobox(root, textvariable=project_var, font=("TkDefaultFont", 13), width=39)
    project_combo['values'] = project_files
    if project_files:
        project_combo.current(0)
    project_combo.pack()
    project_combo.bind('<Return>', focus_login_button)

    tk.Label(root, text="ユーザー名:", font=("TkDefaultFont", 13)).pack()
    username_entry = tk.Entry(root, font=("TkDefaultFont", 13), width=39)
    username_entry.insert(0, auth_data['username'])
    username_entry.pack()
    username_entry.bind('<Return>', focus_password)

    tk.Label(root, text="パスワード:", font=("TkDefaultFont", 13)).pack()
    password_entry = tk.Entry(root, show="*", font=("TkDefaultFont", 13), width=39)
    password_entry.pack()
    password_entry.bind('<Return>', focus_version_combo)
    
    #============= バージョン選択 =============
    tk.Label(root, text="バージョン選択:", font=("TkDefaultFont", 13)).pack()
    version_var = tk.StringVar()
    versions = get_qgis_versions()
    version_combo = CustomCombobox(root, textvariable=version_var, 
                                   display_values=versions[0], 
                                   actual_values=versions[1], 
                                   font=("TkDefaultFont", 13), width=39)
    print(f"バージョン選択初期設定：{version_combo['values'][0]}")
    version_combo.set(auth_data['qgis_display_version'])  # 初期値を設定
    
    # selected_versionがコンボに無い場合は、コンボにある先頭の値にする
    if auth_data['qgis_version'] not in version_combo.actual_values:
        version_combo.set(version_combo.display_values[0])
        print(f"選択されたバージョンが無効なため、先頭のバージョンに設定しました: {version_combo.display_values[0]}")
    
    version_combo.pack()
    version_combo.bind('<Return>', focus_profile_combo)
    
    # ================　プロファイルの選択 ===================
    tk.Label(root, text="プロファイル選択:", font=("TkDefaultFont", 13)).pack()
    profile_var = tk.StringVar()
    profile_combo = ttk.Combobox(root, textvariable=profile_var, font=("TkDefaultFont", 13), width=39)
    profile_combo['values'] = ('portable', 'profile強制更新')
    profile_combo.set(auth_data['selected_profile'])
    profile_combo.pack()
    profile_combo.bind('<Return>', focus_login_button)

    login_button = tk.Button(root, text="ログイン", command=validate_login, width=26, height=2, font=("TkDefaultFont", 13))
    login_button.pack(pady=13)
    login_button.bind('<Return>', validate_login)

    # QGISリンクボタンの追加
    qgis_link_button = tk.Button(root, text="QGISインストール版の取得", command=open_qgis_website, font=("TkDefaultFont", 13))
    qgis_link_button.pack(pady=6)

    username_entry.focus()
    root.mainloop()
    return logged_in_user, user_role, selected_version, selected_display_version, selected_profile, selected_project_file

def run_login():
    global version_combo
    logged_in_user, user_role, selected_version, selected_display_version, selected_profile, selected_project_file = create_login_window()
    if logged_in_user:
        save_auth_data_to_ini(logged_in_user, selected_version, selected_display_version, user_role, selected_profile, selected_project_file)
        # 関数を呼び出して値を書き込む
        ProjectFile.write_to_ini('./launcher/ini/qgis_global_settings.ini', logged_in_user, user_role)
        return logged_in_user, user_role, selected_version, selected_display_version, selected_profile, selected_project_file
    return None, None, None, None, None, None

if __name__ == "__main__":
    logged_in_user, user_role, selected_version, selected_display_version, selected_profile, selected_project_file = run_login()
    if logged_in_user:
        print(f"auth.py上でのログインに成功しました。ユーザー名: {logged_in_user}, 権限: {user_role}, 選択された実行バージョン: {selected_version}, 選択された表示バージョン: {selected_display_version}, プロファイル：{selected_profile}, プロジェクトファイル: {selected_project_file}")
    else:
        print("ログインに失敗しました。")
