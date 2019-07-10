javaは知っているが
pythonの文法が覚えられない
その逆もあると思う

ので、対応表を作ってまとめてみた
（・・いるのかは分からんけど）


自身も勉強中のため、随時追加予定

|説明|Java|Python||
|:-----|:-----|:-----|:-----|
|標準入力をスペースで区切り数値で取得|Scanner.nextInt()|int(input().split())||
|標準入力を１行文字列として取得|Scanner.nextLine()|input()||
|標準入力を引数(argv)から取得|メソッドの引数にString[] argsと書いて<br>そのメソッド内でargs（引数のインデックス）|import sys<br>sys.argv ||
|||||
|||||
|コンソールにxxを出力して改行する|System.out.println(xx)|print(xx)||
|コンソールにxxを出力して改行しない|System.out.print(xx)|print(xx,end="")||
|||||
|コンソールにxxを出力して改行しない||(文字列).upper()||
|||||
|||||
|タプル||||
|リスト||||
|リストの長さ|リスト.size()|len(リスト)||
|リストの全要素の合計||sum(リスト)||
|リストのソート（リスト自体は変化しない）||sorted(リスト)||
|リストのソート（リスト自体もソートされる）|Collections.sort(リスト)|リスト.sort()||
|リストa,bの共通要素のみを表示||c = [x for x in a if x in b]<br>もしくはa,bをsetにして & (and)でつなぐ<br>A = set(a)<br>B = set(b)<br>C = A & B||
|リストa,bの和集合を表示||a,bをsetにして ｜ (or)でつなぐ<br>A = set(a)<br>B = set(b)<br>C = A ｜ B||
|文字列Sを１文字ずつのリストにする||**list(文字列)**<br>（これでOKらしい・・）||
|||||
|||||
|||||
|辞書（Map)|Map<String,String> a = new HashMap<String,String>();<br>(String,Stringの例)|dict = {}<br>||
|辞書(Map)に要素を置く|(Map).put(キー,値)|辞書[キー] = 要素||
|辞書(Map)からキーを指定して要素取得|(Map).get(キー)|**辞書[キー]**<br>または<br>**辞書.get(key[,default])**<br>（defaultはキーがない場合のデフォルト値）||
|辞書(Map)から要素削除||辞書.pop(キー)<br>※全削除するなら↓<br>辞書.clear()||
|辞書(Map)から最大のキーを取得||max(辞書)||
|辞書(Map)から最小のキーを取得||min(辞書)||
|辞書(Map)から最大の値を取得||max(辞書.values())||
|辞書(Map)から最小の値を取得||min(辞書.values())||
|辞書(Map)から最大の値をとるキーを取得||max(辞書,key=辞書.get)||
|辞書(Map)から最小の値をとるキーを取得||min(辞書,key=辞書.get)||
|辞書(Map)からキーのリストを取得||**辞書.keys()**<br>（dict_keys型で取得。全てのキーを順に取るには<br>**for v in 辞書.keys()**）||
|辞書(Map)から値のリストを取得||**辞書.values()**<br>（dict_values型で取得。全ての値を順に取るには<br>**for i in 辞書.values()**）||
|||||
|リストを逆順にして表示||||
|||||
|||join()||
|||zip()||
|２つの配列、リストをどちらかを軸にして対応させるようにソートする|int[][] a<br>Arrays.sort(a,(x,y) -> Integer.comparator(x[0],y[0]))<br>（配列の形式と比較させたい方法によって適宜変更）|c = zip(a,b)<br>c = sorted(c)<br>a,b = zip(*c)<br>※ただしa,bはタプルで返ってくる||
|||||
|||||
|||||
|リストから共通の要素を取り出す||||
|||||
|||||
|数値を文字列に変更する|String.valueOf(数値)|str(数値)||
|文字列を数値に変更する|Integer.parseInt(文字列)|int(文字列)||
|数字の頭をゼロ詰して表示する|**String.format("03d",数字)**<br>（ゼロ詰して３桁で表示する時の例）|||
|||||
|関数（メソッド）|アクセス修飾子 (static) 返り値の型　メソッド名(引数){}|def 関数名(引数)||
|関数の説明(javadocみたいな)||def 関数名(引数):<br>"""<br>(説明)<br>"""||
|変数のデータ型を知りたいとき||type(変数)||
|クラスの宣言|class クラス名{}|class クラス名(object):||
|クラスのコンストラクタ|(public) クラス名と同じメソッド(引数)|def __init__(引数):<br>↑新しいクラスを作った時の宣言||
|オブジェクト（クラス）内のメソッドを列挙する||dir(オブジェクト)||
|||||
|ファイルのオープン||File = open(ファイルのパス,"r,wなど")<br>(Fileは変数)||
|ファイル変数の名前||||
|ファイル変数のモード||||
|ファイルから1行読み込む||ファイル変数.readline()||
|ファイルからx行読み込む||ファイル変数.readline(x)||
|ファイルから全文字読み込む||ファイル変数.read()<br>csvの場合はPandasを使って<br>import pandas<br>file = pandas.read_csv(csvファイル)でもできる||
|ファイルからx文字読み込む||ファイル変数.read(x)<br>（ただし、以前readやってたらその終点から数える）||
|読み込んだファイルの始め５行を出力する||file = pandas.read_csv<br>file.head()||
|Excelを読み込む||import pandas<br>xl = pandas.read_excel(エクセルファイルのパス)||
|||||
|||||
|||||
|階乗の計算||import math<br>math.factorial(数字)||
|絶対値|Math.abs(数字)|abs(数字)||
|２つの数字のうち大きい方|Math.max(数字、数字)|max(数字、数字・・)<br>幾つでも可||
|２つの数字のうち小さい方|Math.min(数字、数字)|min(数字、数字・・)<br>幾つでも可||
|リストのうち一番大きい数字|Collections.max(リスト)|max(リスト)||
|リストの各要素全てに一つの数字を演算する||import numpy<br>a = np.array(リスト)<br>b = a([k:l]) + 1<br>(リストの一部分に対して行いたいとき)<br>b = a[k:l] + 1||
|１次元行列を作る||import numpy as np<br>a = np.array([0,1,2,3,4])||
|行列の次元（ランク）を調べる||import numpy as np<br>a = np.array([0,1,2,3,4])<br>**a.ndim**||
|ベクトルの内積||import numpy as np<br>a = np.array([0,1,2,3,4])<br>b = np.array([0,1,2,3,4])<br>c = **a.dot(b)**||
|aからbまで、要素n個で各要素の間が均等になるようなリストを作る||import numpy as np<br>**np.linspace(a,b,n)**||
|２つの行列で対応する要素を掛け算した行列を出したい時||import numpy as np<br>a = np.array([0,1,2,3,4])<br>b = np.array([0,1,2,3,4])<br>c = **a * b**||
|2次元行列を作りたい時||a = [[x1,x2,,xn],[y1,y2,,yn],[z1,z2,,zn]]<br>A = np.array(a)||
|行列が何行何列か知りたい時||import numpy as np<br>a = np.array([0,1,2,3,4])<br>**a.shape()**<br>（タプルで行、列で返る）||
|２つの行列を掛け算したい時||**np.dot(A,B)**||
|行列の要素数を出したい時||import numpy<br>a = np.array(リスト)<br>**a.size**||
|行列を転置したい時||import numpy<br>a = np.array(リスト)<br>**a.T**||
|単位行列を作る||import numpy as np<br>a = **np.eye(N,M,k,dtype)**<br>(N=行数、M=列数(Noneの時はN)、k=上にkだけスライド、dtype=要素のデータタイプ)||
|||||
|||||
|||||
|||||
|||||
|||||
|円周率(π)||import numpy as np<br>**np.pi**||
|常用対数(底10)|Math.log10()|import math<br>math.log10(数字)||
|対数(底2)||import math<br>math.log2(数字)||
|||||
|||||
|小数点切り下げ|Math.floor(数値)|import math<br>math.floor(数値)||
|小数点切り上げ|Math.ceil(数値)|import math<br>math.ceil(数値)<br>また、割り算の時は<br>a = b **//** c<br>とすれば割り算と同時に切り下げも行う||
|二進数で表示||bin(数値)||
|二進数で表示した時の長さ||数値.bit_length()||
|||||
|３項演算子|int a = (条件式) ? (正のとき入れる値) : (負のとき入れる値)|a = (正のとき入れる値) if (条件式) else (負のとき入れる値)||
|||||
|||||
||||||

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


### そのためも

- pythonでのand,orの演算
- pythonでインクリメントは使えない

- pythonで順列・組み合わせを求める方法は？

- pythonでの２次元リスト

作り方の例

```
list1 = [[0]*3]*2
list2 = [[0 for i in range(3)] for j in range(2)]
list3 = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

print(list1)
print(list2)
print(list3)
```
実行結果
```
[[0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 0, 0]]
[[1, 2, 3], [10, 20, 30], [100, 200, 300]]
```
要素を書き換えるとき
```
list1 = [[0]*3]*2
list2 = [[0 for i in range(3)] for j in range(2)]

print("2次元配列の初期化")
print("list1 = {0}".format(list1))
print("list2 = {0}".format(list2))

list1[0][1] = 1
list2[0][1] = 1

print("要素設定後")
print("list1 = {0}".format(list1))
print("list2 = {0}".format(list2))
```
実行結果
```
2次元配列の初期化
list1 = [[0, 0, 0], [0, 0, 0]]
list2 = [[0, 0, 0], [0, 0, 0]]
要素設定後
list1 = [[0, 1, 0], [0, 1, 0]]
list2 = [[0, 1, 0], [0, 0, 0]]
```

list1とlist2は同じ配列ですが、結果が異なることがわかりますね。

list1の場合は[0]*3で同じリストを3つ定義しているだけなので、要素の値を変更すると他の要素まで変わってしまいます。

list2の場合は内包表記を使って複数のリストを作っているので、2次元配列（リストのリスト）の要素[0][1]番目のみ、つまり意図したとおり値が変更されています。

そのため、要素番号を指定して正しく要素を指定したい場合は2次元配列をlist2のような内包表記で宣言すると良いでしょう。

- Pythonで連立一次方程式をときたい時

要は

Ax = B
