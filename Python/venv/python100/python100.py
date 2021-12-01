"""
1~5
print("Hello")
print("Hello World")
print("Hello")
print("World")
print("'Hello'")
print('"Hello World"')

5~10
print('\"!@#$%^&*()\'')
print('\"C:\\Download\\\'hello\'.py\"')
print('print(\"Hello\\nWorld\")')
c = input()
print(c)
n = input()
n = int(n)
print(n)

11~15
f = input()
f = float(f)
print(f)

a = input()
b = input()
print(b)
print(a)

c = input()
c = float(c)
print(c)
print(c)
print(c)

d,e = input().split()
print(d)
print(e)



#16~20
a, b = input().split();
print(b, a);

a = input();
print(a, a, a);

a,b = input().split(":");
print(a, b, sep=':');

a,b,c = input().split('.');
print(c,b,a,sep='-');

a,b = input().split('-');
print(a,b,sep='');



#21~25
a = input()
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

a = input()
print(a[0:2], a[2:4], a[4:6], sep=" ")

a = input().split(":")
print(a[1])

a, b = input().split()
s = a+b
print(s)

a, b = input().split()
s = int(a)+int(b)
print(s)


#26~31
a = input()
b = input()
c = float(a)
d = float(b)
print(c+d)

a = input()
n = int(a)
print('%x' %n)

a = input()
n = int(a)
print('%X' %n)


a = input()
n = int(a, 16)
print('%o' %n)

a = ord(input()) # ord : 입력받은 문자를 10진수 유니코드 값으로 변환
print(a)

a = int(input())
print(chr(a))
"""