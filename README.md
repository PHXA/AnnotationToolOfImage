
<img width="1209" alt="scs" src="https://user-images.githubusercontent.com/69100913/209538508-18c691f4-6b30-4ab6-a2ae-064eb67dc13a.png">

# 概要(Summary)

Flaskによるアノテーションツールです。

This repository is annotation tool based on Flask.

画像のバウンディングボックスの作成とラベリングを助けます。

To help making bounding box and labeling.

Python、Vue、Html、Js、Cssにより開発されています。
比較的軽量なシステムだと思います。

It is developed in Python, Vue, Html, Js, and Css.
It is a relatively lightweight system.

フロントエンドのブラウザとサーバとの間で画像とバウンディングボックスの2点(x,y)の情報とラベルの情報をやり取りします。

Information about the image and the two points (x,y) of the bounding box and the label are exchanged between the front-end browser and the server.


# 実行手順(Procedure)

1. .envファイルにホスト名を記述( ex. HOST = "localhost:8888")
2. datasets/配下に画像を保存
3. server.pyを実行( python server.py )
4. ホストにアクセス

# アノテーションデータ(Annotation data)

annotations/配下に保存されます。
jsonl形式です。
各行は{x1:"",x2:"",y1:"",y2:"",label:""}となります。

# 保存のタイミング(Event of saving)

保存ボタンの押下時、次のページ、前のページの遷移時です。

This is when the save button is pressed, or when transitioning to the next or previous page.

# 各ボタンの意味(Each button)

category_labelはバウンディングボックスに対するラベルを入力します。必須情報ではありません。未入力の場合は空の情報が保持されます。

lockは押下時にcategory_labelをReadonlyに切り替えます。

saveはバウンディングボックスとラベルの情報をサーバに送信します。

Resetは画面のバウンディングボックスをすべて削除します。

Ctr + Arrowleftを押下時に前のページに遷移します。Ctr + ArrowRightを押下時に次のページに遷移します。Ctr + zを押下時にひとつ前のバウンディングボックスを削除します。

⇦は前のページに遷移します。⇨は次のページに遷移します。

画像は10枚ずつやり取りが行われます。カーソルによりサーバとフロントエンドで制御されます。たとえば
http://localhost/getImg?c=0
のような形でcによりカーソルの位置を送信することで画像が切り替わります。次のページに遷移する場合はc=1となります。

# 注意(Note)

ページ遷移に伴いサーバにデータは送信され新しい画像がリクエストされます。

ページ遷移、Saveボタンの押下時、以外のリロードをした場合は保存されません。

フロントエンドとサーバサイドはファイル名をIDとして画像をやり取りします。

編集のような機能は現状はありません。

annotations配下に同じ画像名を持つjsonlファイルとしてアノテーション結果が追記されていきます。そのためアノテーションが終了後にannotationsのフォルダ名を変更することをおすすめします。

server.pyのホストとポート番号などの要件は任意に変更してください。


