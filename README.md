# FastAPI<br>
fastapi練習<br>
## そもそもFastAPIとは
Flaskのシンプルさと，Djangoにはないモダンな機能を兼ね備え，そこに圧倒的なパフォーマンスを加えたフレームワーク．<br>
強力なライブラリ２つ<br>
- Starlette:非同期処理を担う超高速な基盤
- Pydantic:Pythonの方ヒントを利用して，データの検証や設定管理を強力に行うライブラリ<br>

## 他のフレームワークとの比較
 特徴   | FastAPI | Django     | Flask |
|--------|------|----------|-----|
| タイプ   | マイクロフレームワーク   | フルスタックフレームワーク|マイクロフレームワーク|
| 非同期サポート   | ◎ (ネイティブ) | △ (部分的)|△ (部分的)|
| パフォーマンス   | ◎ (非常に高速)|	△ (比較的遅い)	|〇 (FastAPIよりは遅い)  |
| データ検証   | ◎ (Pydanticで強力)|	〇 (フォーム機能)	|× (別途ライブラリ要)   |
| APIドキュメント   | ◎ (自動生成)	|× (別途ライブラリ要)	|× (別途ライブラリ要)   |
| 主な用途   | Web API開発，機械学習モデルの提供	|Webサイト全般，管理画面を持つ業務システム	|小規模アプリ，プロトタイプ   |
## 参考にしたサイト
[FastAPIなんぞ](https://zenn.dev/hamaup/books/482d1320ad9400/viewer/ec4b96)<br>
[Markdownの記法](https://help.notepm.jp/hc/ja/articles/17267176922393-Markdown%E8%A8%98%E6%B3%95-%E6%9B%B8%E3%81%8D%E6%96%B9-%E8%A6%8B%E5%87%BA%E3%81%97-%E8%A1%A8-%E3%83%AA%E3%83%B3%E3%82%AF-%E7%94%BB%E5%83%8F-%E6%96%87%E5%AD%97%E8%89%B2%E3%81%AA%E3%81%A9)<br>
## 学んだこと<br>
- def(同期)とasync defエイシンク(非同期)<br>

## Responseの解説
**detail**: バリデーションエラーの詳細情報がリスト形式で格納されています。<br>
<br>
各エラーオブジェクトには、以下の情報が含まれています。<br>
<br>
**loc**: エラーが発生した場所(body.name, body.priceなど)<br>
**msg**: エラーメッセージ(Input should be a valid string, value is not a valid floatなど)<br>
**type**: エラータイプ(type_error.str, value_error.floatなど)<br>
