# FastAPI<br>
fastapi練習<br>
## 参考にしたサイト
[FastAPIなんぞ](https://zenn.dev/hamaup/books/482d1320ad9400/viewer/ec4b96)<br>
[Markdownの記法](https://help.notepm.jp/hc/ja/articles/17267176922393-Markdown%E8%A8%98%E6%B3%95-%E6%9B%B8%E3%81%8D%E6%96%B9-%E8%A6%8B%E5%87%BA%E3%81%97-%E8%A1%A8-%E3%83%AA%E3%83%B3%E3%82%AF-%E7%94%BB%E5%83%8F-%E6%96%87%E5%AD%97%E8%89%B2%E3%81%AA%E3%81%A9)<br>
## 学んだこと<br>
- def(同期)とasync def(非同期)なんぞ


## Responseの解説
**detail**: バリデーションエラーの詳細情報がリスト形式で格納されています。<br>
<br>
各エラーオブジェクトには、以下の情報が含まれています。<br>
<br>
**loc**: エラーが発生した場所(body.name, body.priceなど)<br>
**msg**: エラーメッセージ(Input should be a valid string, value is not a valid floatなど)<br>
**type**: エラータイプ(type_error.str, value_error.floatなど)<br>
