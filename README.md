# 初めての人でも扱いやすいポータブルQGIS環境の構築
## 起動画面
![image](https://github.com/user-attachments/assets/ea4196c0-be51-47d9-888a-45811f3e2024)
#### 【auth.config】ファイルが存在しない場合は、認証が不要になります。  
　　　［標準設定］  
　　"username": "view","password": "","userrole": "Viewer"  
　　"username": "edit","password": "","userrole": "Editor"  
　　"username": "qgis", "password": "","userrole": "Editor"  
　　"username": "admin","password": "","userrole": "Administrator"  
　　　［バージョン選択］  
　　インストール版：拡張子qgsと関連付けされているQGIS  
　　ポータブル版：congiで指定されているQGIS  
#### 【ProjectFile.config】
　　VirtualDrive=Q:  
　　により仮想ドライブを指定してください。  
　　その他の項目は任意です。  
   
## ランチャー導入により、QGISのDVD納品・統一環境の構築等に可能となります。 
[システム一式 ver3.38.1](https://1drv.ms/u/c/cbbfeab49e70546f/EYyJqLhVbXNFufPDmemiWhABSOS7PdZqyGN_K_YfKuRKIg?e=N0973F)  

## QGISランチャーコンセプト
- 起動.EXEファイルによる、指定プロジェクトファイルの起動  
- UIカスタマイズによる、権限別のUI設定   
　AdministratorUI_customization.ini  
　EditorUI_customization.ini  
　ViewerUI_customization.ini  
　qgis_global_settings.ini  
- startup.pyによる、権限別のレイヤ設定  
  "userrole": "Viewer"　に対して、「レイヤーを読み取り」に設定
![image](https://github.com/user-attachments/assets/20c4a48d-7de1-49c4-9e45-f1da5e1fd8af)
## QGISランチャー
 ProjectFile.exe を起動してください。  
 /ProjectFiles/ProjectFile.qgs が起動します。  
 'shift'キーを押しながら起動すると、プロファイルをリセットできます。

EXEはファイル名を変えることで、同じ名称のqgsファイルを起動します。  
 例）test.exe　に　変更すると　test.qgs が起動します  

 ※拡張子はLIZMAP連携のためQGSを利用しています。
 
（フォルダー構成）  
　QGISポータブル版を私の趣味により統一環境として組込済のプラグインを含んでいます。  
　WindowsのProjectFile.exeです。    
　/ルードフォルダ
　　ProjectFile.exe ----------------　ランチャー本体   
　　/QGIS各バージョン/qgis --------------- QGIS本体  
　　/QGIS各バージョン/qgisconfig----------　各種共通設定ファイルを含んだコンフィグファイル    
　　/ProjectFiles-------------------　初期設定がされたプロジェクトファイルを保存するフォルダ    
　　/ProjectFiles/data----------　プロジェクトファイルで利用しているオープンデータを保存するフォルダ(Lizmap)
 
　英数字のみからなるフォルダに解凍してください。   
　日本語を含むフォルダはエラーになります。  
![image](https://github.com/yamamoto-ryuzo/yr-qgis-portable-launcher2/assets/86514652/177ffbe3-654d-4d22-9f70-add09bcf0323)
  
## 統一環境として組込済のプラグイン  
### MMQGIS
[https://plugins.qgis.org/plugins/mmqgis/#plugin-about ](https://michaelminn.com/linux/mmqgis/)   
### 検索  
### Search Layers  
https://github.com/NationalSecurityAgency/qgis-searchlayers-plugin  
### GEO_search  
https://github.com/yamamoto-ryuzo/GEO-search-plugin  
## 印刷  
### Instant Print  
https://github.com/sourcepole/qgis-instantprint-plugin  
### 簡易印刷  
公開予定  
### (保留中)  
公式プラグインでは日本語対応していません、下記リポジトリからダウンロードください。  
https://github.com/sourcepole/qgis-instantprint-plugin  
### (保留中)  
https://github.com/Orbitalnet-incs/meshprint  
## レイヤー管理   
### Layers menu from project  
https://github.com/xcaeag/MenuFromProject-Qgis-Plugin  
## 画面  
### ZoomView  
https://bitbucket.org/janzandr/zoomview/src/master/
## WEB連携  
### Street View  
リポジトリなし  
### Lizmap  
https://github.com/3liz/lizmap-plugin  
### qgis2web  
https://github.com/qgis2web/qgis2web  
### Qgis2threejs  
https://github.com/minorua/Qgis2threejs  
## データ連携  
### PLATEAU QGIS Plugin  
https://github.com/Project-PLATEAU/plateau-qgis-plugin  
### ExcelSync  
https://github.com/opengisch/qgis_excel_sync  
### Spreadsheet Layers  
https://github.com/camptocamp/QGIS-SpreadSheetLayers  
### MOJXML Loader  
https://github.com/MIERUNE/qgis-mojxml-plugin  
## その他  
### Select Themes  
https://github.com/Amphibitus/selectThemes  
### QGIS-legendView  
https://github.com/yamamoto-ryuzo/QGIS-legendView
### EasyAttributeFilter  
https://github.com/Orbitalnet-incs/EasyAttributeFilter  
### (保留中)  
https://github.com/Orbitalnet-incs/SearchZmap  
　　
#### ・補足事項  
    .BATの改行コードをWindows用にするため　.gitattributes　を設置 

