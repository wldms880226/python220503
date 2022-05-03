# DemoTuple.python

a = {1,2,3,3}
print(a)
print(type(a))
b = {3,4,5,6}
print(b)

#Tuple 연습
tp=(1,2,3)
print(type(tp))
print(len(tp))

#함수 정의
def times(a, b):
    return a+b, a*b 

#함수 호출
result = times(3,4)
print(result)
print(result[0])
print(result[1])

