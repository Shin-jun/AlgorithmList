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

#32~40
a = int(input())
print(-a)

a = ord(input()) # ord : 문자열을 고유의 숫자로 바꿀수 있다.
print(chr(a+1))

a, b = input().split()
c = int(a)-int(b)
print(c)

a, b = input().split()
c = float(a)*float(b)
print(c)

w, n = input().split()
print(w*int(n))

w = input()
s = input()
print(int(w)*s)

a, b = input().split()
c = int(a)**int(b)
print(c)

a,b = input().split()
c = float(a)**float(b)
print(c)

a, b = input().split()
c = int(a)//int(b)
print(c)


#41~45

a, b = input().split()
print(int(a)%int(b))

a = float(input())
print(format(a, ".2f"))

a, b = input().split()
c = float(a)/float(b)
print(format(c, ".3f"))

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(round(a/b, 2)) # 소수점 반올림 round()함수

a, b, c = map(int, input().split())
print(a+b+c,format((a+b+c)/3, ".2f"))


# 46~50

a = int(input())
print(a<<1)

a, b = map(int, input().split())
print(a<<b)

a, b = map(int, input().split())
print(a<b)

a, b = map(int, input().split())
print(a==b)

a, b = map(int, input().split())
print(a<=b)


#50~55
a, b = input().split()
print(a != b)

a = int(input())
print(bool(a))

a = bool(int(input()))
print(not a)

a, b = input().split()
print(bool(int(a)) and bool(int(b)))

a, b = input().split()
print(bool(int(a)) or bool(int(b)))


# 56~60
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and(not b) or ((not a) and b)))

a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(((not a) and (not b)) or (a and b))

a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(((not a) and (not b)) or (not(a or b)))

a = input()
print(~int(a))

a, b = input().split()
print(int(a)&int(b))

#61~66
a, b = input().split()
print(int(a)|int(b))

a, b = input().split()
print(int(a)^int(b))

a, b = input().split()
a = int(a)
b = int(b)
c = (a if (a>=b) else b)
print(int(c))

a, b, c= input().split()
a = int(a)
b = int(b)
c = int(c)
d = (a if a<=b else b) if ((a if a<=b else b)<=c) else c
print(int(d))

a, b, c= input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2 ==0:
    print(a)
if b%2 ==0:
    print(b)
if c%2 ==0:
    print(c)

a, b, c= input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2 == 0:
    print("even")
else:
    print("odd")
if b%2 == 0:
    print("even")
else:
    print("odd")
if c%2 == 0:
    print("even")
else:
    print("odd")

#67~71
a = int(input())
if a<0:
    if a%2 == 0:
        print("A")
    else:
        print("B")
else:
    if a%2 == 0:
        print("C")
    else:
        print("D")

n = int(input())
if n>=90 :
  print('A')
else :
  if n>=70 :
    print('B')
  else :
    if n>=40 :
      print('C')
    else :
      print('D')

a = input()
if a == 'A':
    print('best!!!')
elif a == 'B':
    print('good!!')
elif a == 'C':
    print('run!')
elif a == 'D':
    print('slowly~')
else:
    print('what?')

n = int(input())
if n==12 or n<=2:
  print("winter")
elif n<=5:
  print("spring")
elif n<=8:
  print("summer")
elif n<=11:
  print("fall")
"""
n=1
while n!=0:
    n=int(input())
    if n!=0:
        print(n)
