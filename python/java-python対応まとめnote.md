javaは知っているが
pythonの文法が覚えられない
その逆も然り（・・いるのかは分からんけど）

ので、対応表を作ってまとめた


||Java|Python|説明|
|:----|:----|:----|:---|
||Scanner.nextInt()|int(input().split())|標準入力をスペースで区切り数値で取得|
||Scanner.nextLine()|input()|標準入力を１行文字列として取得|
|||import sys sys.argv |標準入力を引数(argv)から取得|
|||||
|||||
||System.out.println(xx)|print(xx)|コンソールにxxを出力して改行する|
||System.out.print(xx)|print(xx,end="")|コンソールにxxを出力して改行しない|
|||||
||||タプル|
||||リスト|
||リスト.size()|len(リスト)|リストの長さ|
|||sum(リスト)|リストの全要素の合計|
|||sorted(リスト)|リストのソート（リスト自体は変化しない）|
||Collections.sort(リスト)|リスト.sort()|リストのソート（リスト自体もソートされる）|
|||||
|||||
||||辞書（Map)|
|||||
||||リストを逆順にして表示|
|||||
|||join()||
|||zip()||
|||||
||||リストから共通の要素を取り出す|
|||||
|||||
||String.valueOf(数値)|str(数値)|数値を文字列に変更する|
||Integer.parseInt(文字列)|int(文字列)|文字列を数値に変更する|
|||||
|||||
||アクセス修飾子 (static) 返り値の型　メソッド名(引数){}|def 関数名(引数)|関数（メソッド）|
|||def 関数名(引数):<br>"""<br>(説明)<br>"""|関数の説明(javadocみたいな)|
|||type(変数)|変数のデータ型を知りたいとき|
|class クラス名{}|class クラス名(object):||クラスの宣言|
|(public) クラス名と同じメソッド(引数)|def __init__(引数):<br>↑新しいクラスを作った時の宣言||クラスのコンストラクタ|
|||dir(オブジェクト)|オブジェクト（クラス）内のメソッドを列挙する|
|||||
|||File = open(ファイルのパス,"r,wなど")<br>(Fileは変数)|ファイルのオープン|
||||ファイル変数の名前|
||||ファイル変数のモード|
|||ファイル変数.readline()|ファイルから1行読み込む|
|||ファイル変数.readline(x)|ファイルからx行読み込む|
|||ファイル変数.read()<br>csvの場合はPandasを使って<br>import pandas<br>file = pandas.read_csv(csvファイル)でもできる|ファイルから全文字読み込む|
|||ファイル変数.read(x)<br>（ただし、以前readやってたらその終点から数える）|ファイルからx文字読み込む|
|||file = pandas.read_csv<br>file.head()|読み込んだファイルの始め５行を出力する|
|||import pandas<br>xl = pandas.read_excel(エクセルファイルのパス)|Excelを読み込む|
|||||
|||import math<br>math.factorial(数字)|階乗の計算|
||Math.abs(数字)|abs(数字)|絶対値の|
||Math.max(数字、数字)|max(数字、数字・・)<br>幾つでも可|２つの数字のうち大きい方|
||Math.min(数字、数字)|min(数字、数字・・)<br>幾つでも可|２つの数字のうち小さい方|
||Collections.max(リスト)|max(リスト)|リストのうち一番大きい数字|
|||||
||Math.log10()|import math<br>math.log10(数字)|常用対数(底10)|
|||import math<br>math.log2(数字)|対数(底2)|
|||||
|||||
||Math.floor(数値)|import math<br>math.floor(数値)|小数点切り下げ|
||Math.ceil(数値)|import math<br>math.ceil(数値)<br>また、割り算の時は<br>a = b **//** c<br>とすれば割り算と同時に切り下げも行う|小数点切り上げ|
|||bin(数値)|二進数で表示|
|||数値.bit_length()|二進数で表示した時の長さ|
|||||
|||||
|||||
|||||
||||||

# 他、Pythonの小技

## 拡張for文

```
squares=["red","green","yellow"]
for i,square in enumerate(squares):
  square  //squaresの要素
  i       //squaresのインデックス
```

が入るって知ってた？javaではどうなる？


# Python分かりにくかったところ

- with構文

ファイルオープンの時に使うと楽になるやつ？
この下でインデント分けて、終わったら自動でクローズしてくれる
今swiftでやってるRealmみたいなやつかな？

# Pandasライブラリ

データ分析の有名なライブラリ？
