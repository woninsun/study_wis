# 변수 a, b 생성
a=10
b=20
print(a+b)

# 변수 c, d 생성
c=30
d=40
print(d/c)
print(a+b+c+d)

for i in range(a):
  print(i*b)
  print(i*c)
  print(i*d)
  if i%2==0:
    print("짝수")