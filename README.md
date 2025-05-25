# ポータブルQGIS・QField環境ランチャー

  ランチャー導入により、QGIS・QFiledのDVD納品・統一環境の構築等が可能となります。  
  [システム最新版　一式](https://github.com/yamamoto-ryuzo/yr-qgis-launcher/archive/refs/heads/main.zip)  
  [システム　　　　一式 ポータブル版QGISver3.42.0+QFiled3.4.2含む](https://1drv.ms/u/c/cbbfeab49e70546f/EeP0kFMfp3hDp6NourqA9TABu9P4Ez0D6bDBP-kPdfCi2g)  
  [システム　　　　一式 ポータブル版QGISver3.40.0含む](https://1drv.ms/u/c/cbbfeab49e70546f/Ebzf1zbg_YtPmk5HhNcgucwB6GtusI6YXNKs_MMXKNo2PA)  
  [システム　　　　一式 ポータブル版QFiled3.4.2含む](https://1drv.ms/u/c/cbbfeab49e70546f/EUv4Xt-05ihEiJgXjchBc9UB7Fyjwk6Y7eJKwbiPRkcYEw?e=AMnNSe)    
## 起動画面

![image](https://github.com/user-attachments/assets/a3b96028-f40d-4d57-999d-f3b12d625344)

---

## セットアップ・使い方

1. **ダウンロードしたファイルを英数字のみのパスに展開してください。**  
   ※日本語を含むパスでは動作しません。

2. `ProjectFile.exe` を実行します。

3. `/ProjectFiles/` フォルダ内の `.qgs` または `.qgz` プロジェクトファイルを選択して起動します。

---

## 認証について

- `auth.config` ファイルが存在しない場合は認証不要です。
- 標準ユーザー設定例:

| username | password | userrole      |
| -------- | -------- | ------------- |
| view     |          | Viewer        |
| edit     |          | Editor        |
| qgis     |          | Editor        |
| admin    |          | Administrator |

---

## バージョン選択

- **インストール版**: 拡張子 `.qgs` に関連付けされたQGIS
- **ポータブル版**: `config` で指定されたQGIS

---

## 設定ファイル例

- `ProjectFile.config`
  ```
  VirtualDrive=Q:
  ```
  ※仮想ドライブの指定。他の項目は任意。

---

## フォルダ構成例

```
/(ルートフォルダ)
  ProjectFile.exe                ... ランチャー本体
  /QGIS各バージョン/qgis        ... QGISポータブル本体
  /ini                          ... 初期設定ファイル
  /portable_profile             ... 共通設定ファイル
  /ProjectFiles                 ... プロジェクトファイル保存先
  /ProjectFiles/data            ... オープンデータ保存先（Lizmap仕様）
```

---

## ランチャーの特徴

- EXEファイルから指定プロジェクトを直接起動
- 権限別UIカスタマイズ（例: `AdministratorUI_customization.ini` など）
- `startup.py` による権限別レイヤ設定（例: Viewerは「レイヤーを読み取り」）

---

## 組込済みプラグイン例

- **検索**: [Search Layers](https://github.com/NationalSecurityAgency/qgis-searchlayers-plugin), [GEO_search](https://github.com/yamamoto-ryuzo/GEO-search-plugin)
- **印刷**: [Instant Print](https://github.com/sourcepole/qgis-instantprint-plugin), [easyinstantprint](https://github.com/yamamoto-ryuzo/yr-qgis-easyinstantprint), [簡易印刷](https://github.com/yamamoto-ryuzo/easyprint-feature-qgis3)
- **レイヤー管理**: [Layers menu from project](https://github.com/xcaeag/MenuFromProject-Qgis-Plugin)
- **画面**: [mapswipetool](https://github.com/lmotta/mapswipetool_plugin)
- **WEB連携**: [Lizmap](https://github.com/3liz/lizmap-plugin), [qgis2web](https://github.com/qgis2web/qgis2web)
- **3D関連**: [Qgis2threejs](https://github.com/minorua/Qgis2threejs), [QuickDEM4JP](https://github.com/MIERUNE/QuickDEM4JP), [PLATEAU QGIS Plugin](https://github.com/Project-PLATEAU/plateau-qgis-plugin)
- **データ連携**: [ExcelSync](https://github.com/opengisch/qgis_excel_sync), [Spreadsheet Layers](https://github.com/camptocamp/QGIS-SpreadSheetLayers), [MOJXML Loader](https://github.com/MIERUNE/qgis-mojxml-plugin)
- **開発**: [Plugin Reloader](https://github.com/borysiasty/plugin_reloader)
- **その他**: [Select Themes](https://github.com/Amphibitus/selectThemes), [QGIS-legendView](https://github.com/yamamoto-ryuzo/QGIS-legendView), [EasyAttributeFilter](https://github.com/Orbitalnet-incs/EasyAttributeFilter), [ImportPhotos](https://github.com/KIOS-Research/ImportPhotos/), [MMQGIS](https://michaelminn.com/linux/mmqgis/)

---

## ローカル同期＆ランチャー起動バッチ（local-launchar.bat）

`local-launchar.bat`は、QGIS/QField環境をローカルPCに同期し、必要な場合のみQField*/QGIS*フォルダをバージョン判定して同期、さらに`ProjectFile.exe`を自動起動するバッチです。
これにより、BOXなどのクラウドストレージと高速に同期した閲覧専用の動作環境を構築できます。

### 主な動作

1. `local-launcher\qgislocalsync.config` から同期元・同期先パス、QField/QGISバージョン情報を取得
2. 同期先の `local-launcher\qgislocalsync.config` からローカルのバージョン情報を取得
3. QField*/QGIS*以外のフォルダは常に同期
4. QField*/QGIS*フォルダはバージョンが異なる場合のみ同期
5. 同期後、同期先で `ProjectFile.exe` を自動起動

### 設定ファイル例（local-launcher\qgislocalsync.config）

```
SYNC_SRC=C:\github\yr-qgis-launcher
SYNC_DST=C:\qgis-local-launcher
QFIELD_VERSION=3.4.2
QGIS_VERSION=3.42.0
```

### 使い方

1. `local-launcher\qgislocalsync.config` を編集し、同期元・同期先・バージョンを指定
2. `local-launchar.bat` を実行

3. ---

## 注意事項

- `.BAT` の改行コードはWindows用です（`.gitattributes`設置済み）。
- **日本語を含むパスでは動作しません。必ず英数字のみのパスに展開してください。**

---

## 免責事項

本システムは個人のPCで作成・テストされたものです。  
ご利用によるいかなる損害も責任を負いません。

<p align="center">
  <a href="https://giphy.com/explore/free-gif" target="_blank">
    <img src="https://github.com/yamamoto-ryuzo/QGIS_portable_3x/raw/master/imgs/giphy.gif" width="500" title="avvio QGIS">
  </a>
</p>

