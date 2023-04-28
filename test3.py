#함수 정의
def add(x,y):
    return x+y

#람다 함수
add2 = lambda x,y : x+y

result = add(10,20)
result2 = add2(10,20)

print(result)
print(result2)

arr = [1, 2, 3]

f2 = lambda x : 2 * x
f3 = lambda x : 3 * x

def multiply2(arr, f) :
    result10 = []
    for ele in arr :
      result10.append(f(ele))
    return result10

print(multiply2(arr, f2))
print(multiply2(arr, f3))
print(multiply2(arr, lambda x : 4 * x))