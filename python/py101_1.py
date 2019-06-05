#-*- coding:utf-8 -*-
import sys

print(sys.version)

print("Hello!");

#型を表示
print(type(11));
print(type(11.11));
type(12)

a = 2.2
b = int(a)
print(a) #2.2
print(b) #2

c = 5
d = float(c)
print(c) #5
print(d) #5.0

#javaのInteger.parseIntがpythonではこれだけで可能！
e = "1"
f = int(e)
print(e) #1
print(f) #1

#Booleanもintにキャスト可能！逆も可能！
g = True
h = int(g)
print(g) #True
print(h) #1
i = bool(h)
print(i) #True

#演算子で割り算、/は小数まで出すが //は整数にする？
j=25/6.0
k=25//6.0
print(j) #4.16666666667
print(k) #4.0

#Stringは配列として扱える？インデックスで1文字だせる、C言語のようなもの？
l="Michael Jackson"
print(l[0]) #M
print(l[3]) #h
print(l[10])#c

print(l[-3])#s
print(l[0:3]) #Mic (０以上３未満)

print(l[::2]) #スライス、２起き
print(l[0:5:2]) #０以上５未満２おき

print(3*l) #lを３つ
