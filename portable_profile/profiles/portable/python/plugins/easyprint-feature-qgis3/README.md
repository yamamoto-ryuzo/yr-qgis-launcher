# プラグイン名

EasyPrint

## プラグイン説明

デフォルトの印刷の操作が複雑なので、簡略化させた印刷プラグイン

## 設定

### 図郭選択

図郭の shp ファイルが存在する場合、プラグインに図郭番号を選択するためのコンボボックスが表示される。

**setting.py での設定方法**

- ZUKAKU_X_MARGIN
  - 図郭へのズーム時の横への空白
- ZUKAKU_Y_MARGIN = 100
  - 図郭へのズーム時の横への空白
- ZUKAKU_FILE_NAME
  - data フォルダ内の図郭ファイル名
- ZUKAKU_COLUMN_NAME = "ID"
  - 図郭番号の列名

## 依存しているプラグイン

なし

## 使い方

## フォルダ構成

```
./
├─data
├─i18n
├─images
├─layouts
├─pictures
├─preferences
├─styles
└─tools
```

### data

図郭ファイルなどプラグインが使用するデータが格納されている。

### i18n

国際化対応のファイルが格納されている。
初期のプラグインでは使用されていたが、現在は更新されていない。

### images

プラグインが使用するアイコンが格納されている。

### layouts

プリントコンポーザーで使用するテンプレートが格納されている。
現状は一種でメンテはされていない。

### pictures

プラグインで使用する画像が保存されている。
主な用途は、ユーザーが選択して追加する画像アイテムである。

### preferences

用紙のサイズや方向の設定情報が格納されている。

### styles

qml ファイルが格納されている。
何に使われているかは不明。

### tools

プラグインから起動するツール類が格納されている。
現状使用されているのは doCreateSimpleMap のみである。

## ファイルコンバート

### pyuic

```cmd
pyuic4 -x ui_test.ui -o ui_test.py
pyuic4.bat -x ui_test4.ui -o ui_test4.py
```

### pyrcc

```cmd
pyrcc4 -o resources.py resources.qrc
```
