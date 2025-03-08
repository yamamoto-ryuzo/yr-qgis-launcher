import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import sys
import os
import configparser
import winreg
import webbrowser

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

def get_username_from_auth_ini():
    config = configparser.ConfigParser()
    auth_ini_path = os.path.join(os.getcwd(), 'ini', 'auth.ini')
    config.read(auth_ini_path)
    return config.get('Auth', 'username', fallback='')

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

def create_login_window():
    root = tk.Tk()
    root.title("ログインフォーム")
    center_window(root, 300, 300)

    login_attempts = 0
    max_attempts = 10
    logged_in_user = None
    user_role = None
    selected_version = None
    selected_profile = None
    selected_project_file = None

    def focus_password(event):
        password_entry.focus()

    def focus_version_combo(event):
        version_combo.focus()

    def focus_profile_combo(event):
        profile_combo.focus()

    def focus_login_button(event):
        login_button.focus()

    def validate_login(event=None):
        nonlocal login_attempts, logged_in_user, user_role, selected_version, selected_profile, selected_project_file

        entered_username = username_entry.get()
        entered_password = password_entry.get()
        selected_version_index = version_combo.current()
        selected_version = version_combo.actual_values[selected_version_index]
        selected_profile = profile_combo.get()
        
        try:
            with open('auth.config', 'r') as config_file:
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
        
    def get_qgis_versions():
        versions = [[], []]
        
        def add_column(value1, value2):
            versions[0].append(value1)
            versions[1].append(value2)
        
        # インストール版の確認
        install_path = get_associated_app('qgs')
        if install_path:
            print(f"インストール版が見つかりました：{install_path}")
            add_column('インストール版', install_path)
        
        # ポータブル版の確認
        qgis_folders = [item for item in os.listdir() if item.startswith('QGIS') and os.path.isdir(item)]
        for folder in qgis_folders:
            DRV_LTR = os.getcwd()
            OSGEO4W_ROOT = os.path.join(DRV_LTR, folder, 'qgis')
            folder_path = os.path.join(OSGEO4W_ROOT, 'apps', 'qgis-ltr')
            QGIS_Type = 'qgis-ltr' if os.path.exists(folder_path) else 'qgis'
            program_path = os.path.join(OSGEO4W_ROOT, 'bin', f"{QGIS_Type}.bat")
            add_column(f'ポータブル版 ({folder})', program_path)
            print("QGISポータブル版が見つかりました：",versions[0][-1] )
            print("QGISフォルダのパス：",versions[1][-1] )
            # システムパスにQGIS関連のフォルダを追加
            os.environ['PATH'] += os.pathsep + os.path.join(OSGEO4W_ROOT, 'apps', QGIS_Type, 'bin')
            os.environ['PATH'] += os.pathsep + os.path.join(OSGEO4W_ROOT, 'apps')
            os.environ['PATH'] += os.pathsep + os.path.join(OSGEO4W_ROOT, 'bin')
            os.environ['PATH'] += os.pathsep + os.path.join(OSGEO4W_ROOT, 'apps', 'grass')
        return versions

    # ================ プロジェクトファイルの選択 ===================
    tk.Label(root, text="プロジェクトファイル選択:").pack()
    project_var = tk.StringVar()
    project_files = get_qgis_project_files('ProjectFiles')
    project_combo = ttk.Combobox(root, textvariable=project_var)
    project_combo['values'] = project_files
    if project_files:
        project_combo.current(0)
    project_combo.pack()
    project_combo.bind('<Return>', focus_login_button)

    tk.Label(root, text="ユーザー名:").pack()
    username_entry = tk.Entry(root)
    username_entry.insert(0, get_username_from_auth_ini())
    username_entry.pack()
    username_entry.bind('<Return>', focus_password)

    tk.Label(root, text="パスワード:").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    password_entry.bind('<Return>', focus_version_combo)
    
    #============= バージョン選択 =============
    tk.Label(root, text="バージョン選択:").pack()
    version_var = tk.StringVar()
    versions = get_qgis_versions()
    version_combo = CustomCombobox(root, textvariable=version_var, 
                                   display_values=versions[0], 
                                   actual_values=versions[1])
    print(f"バージョン選択初期設定：{version_combo['values'][0]}")
    version_combo.current(0)
    version_combo.pack()
    version_combo.bind('<Return>', focus_profile_combo)
    
    # ================　プロファイルの選択 ===================
    tk.Label(root, text="プロファイル選択:").pack()
    profile_var = tk.StringVar()
    profile_combo = ttk.Combobox(root, textvariable=profile_var)
    profile_combo['values'] = ('portable', 'profile強制更新')
    profile_combo.set('portable')
    profile_combo.pack()
    profile_combo.bind('<Return>', focus_login_button)

    login_button = tk.Button(root, text="ログイン", command=validate_login, width=20, height=2)
    login_button.pack(pady=10)
    login_button.bind('<Return>', validate_login)

    # QGISリンクボタンの追加
    qgis_link_button = tk.Button(root, text="QGISインストール版の取得", command=open_qgis_website)
    qgis_link_button.pack(pady=5)

    username_entry.focus()
    root.mainloop()
    return logged_in_user, user_role, selected_version, selected_profile, selected_project_file

def save_username_to_ini(username):
    config = configparser.ConfigParser()
    config['Auth'] = {'username': username}
    with open('./ini/auth.ini', 'w') as configfile:
        config.write(configfile)

def run_login():
    return create_login_window()

if __name__ == "__main__":
    logged_in_user, user_role, selected_version, selected_profile, selected_project_file = run_login()
    if logged_in_user:
        print(f"ログインに成功しました。ユーザー名: {logged_in_user}, 権限: {user_role}, 選択されたバージョン: {selected_version}, プロファイル：{selected_profile}, プロジェクトファイル: {selected_project_file}")
        save_username_to_ini(logged_in_user)
    else:
        print("ログインに失敗しました。")
