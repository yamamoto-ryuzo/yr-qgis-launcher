import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import sys
import os
import configparser

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("ログインフォーム")
        self.center_window(300, 220)

        self.login_attempts = 0
        self.max_attempts = 10
        self.logged_in_user = None
        self.user_role = None
        self.selected_version = None

        self.create_widgets()

    def center_window(self, width, height):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.master.geometry(f'{width}x{height}+{x}+{y}')

    @staticmethod
    def get_username_from_auth_ini():
        config = configparser.ConfigParser()
        auth_ini_path = os.path.join(os.getcwd(),'ini', 'auth.ini')
        config.read(auth_ini_path)
        return config.get('Auth', 'username', fallback='')

    def create_widgets(self):
        tk.Label(self.master, text="ユーザー名:").pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.insert(0, self.get_username_from_auth_ini())
        self.username_entry.pack()
        self.username_entry.bind('<Return>', self.focus_password)

        tk.Label(self.master, text="パスワード:").pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()
        self.password_entry.bind('<Return>', self.focus_version_combo)

        tk.Label(self.master, text="バージョン選択:").pack()
        self.version_var = tk.StringVar()
        self.version_combo = ttk.Combobox(self.master, textvariable=self.version_var)
        version_combo_values = list(self.version_combo['values'])
        print (f"インストール版の確認：{get_associated_app('qgs')}")
        # カレントディレクトリ内のファイル・フォルダ一覧を取得
        contents = os.listdir()
        # QGISで始まるフォルダを探す
        qgis_folders = [item for item in contents if item.startswith('QGIS') and os.path.isdir(item)]
        if qgis_folders:
            print("QGISで始まるフォルダが見つかりました:")
            version_combo_values.append('ポータブル版')
            self.version_combo.set('ポータブル版')  # デフォルト値
        if get_associated_app('qgs') != '':
            version_combo_values.append('インストール版')
            self.version_combo.set('インストール版')  # デフォルト値
        self.version_combo['values'] = version_combo_values
        self.version_combo.pack()
        self.version_combo.bind('<Return>', self.focus_profile_combo)

        tk.Label(self.master, text="プロファイル選択:").pack()
        self.profile_var = tk.StringVar()
        self.profile_combo = ttk.Combobox(self.master, textvariable=self.profile_var)
        self.profile_combo['values'] = ('portable', 'profile強制更新')
        self.profile_combo.set('portable')  # デフォルト値
        self.profile_combo.pack()
        self.profile_combo.bind('<Return>', self.focus_login_button)

        self.login_button = tk.Button(self.master, text="ログイン", command=self.validate_login)
        self.login_button.pack(pady=10)
        self.login_button.bind('<Return>', self.validate_login)

        self.username_entry.focus()

    def focus_password(self, event):
        self.password_entry.focus()

    def focus_version_combo(self, event):
        self.version_combo.focus()

    def focus_profile_combo(self, event):
        self.profile_combo.focus()

    def focus_login_button(self, event):
        self.login_button.focus()

    def validate_login(self, event=None):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
        self.selected_version = self.version_var.get()
        self.selected_profile = self.profile_combo.get()
        
        try:
            with open('auth.config', 'r') as config_file:
                config = json.load(config_file)
        except FileNotFoundError:
            messagebox.showerror("エラー", "設定ファイルが見つかりません。")
            self.master.quit()
            return
        except json.JSONDecodeError:
            messagebox.showerror("エラー", "設定ファイルの形式が正しくありません。")
            self.master.quit()
            return

        users = config.get('users', [])
        valid_user = next((user for user in users if user['username'] == entered_username and user['password'] == entered_password), None)

        if valid_user:
            messagebox.showinfo("ログイン成功", f"ようこそ、{entered_username}さん!\n あなたの権限は {valid_user['userrole']}です。\n 選択されたバージョン: {self.selected_version}\n 選択されたプロファイル: {self.selected_profile }")
            self.logged_in_user = entered_username
            self.user_role = valid_user['userrole']
            self.master.quit()
        else:
            self.login_attempts += 1
            remaining_attempts = self.max_attempts - self.login_attempts
            if remaining_attempts > 0:
                messagebox.showerror("ログイン失敗", f"ユーザー名またはパスワードが無効です。\n残り試行回数: {remaining_attempts}")
                self.clear_entries()
            else:
                messagebox.showerror("ログイン失敗", "試行回数の上限に達しました。プログラムを終了します。")
                self.master.quit()
                sys.exit()

    def clear_entries(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.username_entry.focus()

    def get_login_info(self):
        return self.logged_in_user, self.user_role, self.selected_version,self.selected_profile

import winreg

def get_associated_app(extension):
    try:
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, f'.{extension}') as key:
            prog_id = winreg.QueryValue(key, '')
        
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, f'{prog_id}\\shell\\open\\command') as key:
            command = winreg.QueryValue(key, '')
        
        # コマンドから実行ファイルのパスを抽出
        app_path = command.split('"')[1]
        
        # パスが実在するか確認
        if os.path.exists(app_path):
            return app_path
        else:
            return ''
    except WindowsError:
        return ''

def run_login():
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
    return app.get_login_info()

def save_username_to_ini(username):
    config = configparser.ConfigParser()
    config['Auth'] = {'username': username}
    with open('./ini/auth.ini', 'w') as configfile:
        config.write(configfile)
        
"""
# メイン処理
if __name__ == "__main__":
    logged_in_user, user_role, selected_version ,selected_profile= run_login()
    if logged_in_user:
        print(f"ログインに成功しました。ユーザー名: {logged_in_user}, 権限: {user_role}, 選択されたバージョン: {selected_version},プロファイル：{selected_profile}")
        save_username_to_ini(logged_in_user)
    else:
        print("ログインに失敗しました。")
"""