QGIS+VSCodeでのデバック環境構築
Python
QGIS
VSCode
投稿日 2021年11月26日
はじめに
QGISのためのVSCodeでのデバック環境を構築します。

環境
Windows 10
QGIS 3.16
OSGeo4W
最初の環境構築(QGISとVSCodeのインストール)
QGISのインストール
ネットワークインストーラーで可変な環境をインストールしましょう
https://qgis.org/ja/site/forusers/download.html
VSCodeのインストール
https://azure.microsoft.com/ja-jp/products/visual-studio-code/
VSCodeでのデバック準備
ptvsdのインストール

OSGeo4Wのshellを起動する
C:/OSGeo4W64/OSGeo4W.batでcmdを起動する
python3をメインで使用するようにコマンドを実行する
py3_envでpython3をメインで使えるようになる
pipをインストールする
存在する場合はインスールしなくてよい
python -m ensurepip --default-pipでpipをインストールする
VSCodeでのデバック用にptvsdをインストールする
python -m pip install ptvsd
> py3_env
> python -m ensurepip --default-pip
> python -m pip install ptvsd
QGISにDebug用プラグインをインストールする

プラグインの管理とインストールを起動
メニューバー→プラグイン→プラグインの管理とインストール
debugvsを検索しインストール
VSCode側のデバック設定を作成

VSCodeを起動する
launch.jsonを作成する
.vscode/launch.json
launch.jsonにリモートデバック用の設定を記載する
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Remote Attach",
      "type": "python",
      "request": "attach",
      "connect": {
        "host": "localhost",
        "port": 5678
      },
      "pathMappings": [
        {
          "localRoot": "${workspaceFolder}",
          "remoteRoot": "${env:HOMEPATH}/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/sample_plugin"
        }
      ],
      "justMyCode": false
    }
  ]
}
localRoot
ローカルのコードが存在するパスを記述する
remoteRoot
シンボリックリンクを使用している場合はリンク先のパスを記述する
直接コードを編集している場合はlocalRootと同じで良い
justMyCode
他のコード内までデバックを行ないたい場合、falseにする
デバックを実行する
QGISを起動する
debugvsのEnable Debug for Visual Studioを実行する
VSCodeでPython: Remote Attachでデバックを実行する
VSCode上でブレイクポイントを設定し、QGISでプラグインを実行する
メモ
シンボリックリンクでpluginsにプラグインを入れていたため、デバックできずにハマった
launch.jsonのRemoteRootにリンク先を書こう！！まじで
pip3でインストールできないって困った
py3_envでpython3用にパスが通るぞ！！らく
参考
環境構築
