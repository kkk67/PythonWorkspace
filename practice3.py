# 반복문 연습
for i in range(1,3):
    print('첫 번째 반복문의 {}번 째 반복입니다.'.format(i))
    for j in range(1,3):
        print('두 번째 반복문의 {}번 째 반복입니다.'.format(j))
        for k in range(1,3):
            print('세 번째 반복문의 {}번 째 반복입니다.'.format(k))

# 스택 연습 
stack = []

for i in range(5):
    stack.append(int(input('스택의 {}번쨰 요소를 입력하세요 : '.format(i))))

print('스택의 요소 값은 {} 입니다.'.format(stack))

for i in range(5):
    print('스택의 제외된 요소 값은 {} 입니다.'.format(stack.pop()))

print('스택의 요소 값은 {} 입니다.'.format(stack))

# 큐 연습
from collections import deque

queue = deque()

for i in range(5):
    queue.append(int(input('큐의 {}번쨰 요소를 입력하세요 : '.format(i))))

print('큐의 요소 값은 {} 입니다.'.format(queue))

for i in range(5):
    print('큐의 제외된 요소 값은 {} 입니다.'.format(queue.popleft()))

# print(queue)

# 재귀함수로 팩토리얼 구해보기

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)
# 반복적 방법으로 팩토리얼 구해보기

def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

n= int(input())

print('재귀적 방법의 팩토리얼 : {}'.format(factorial_recursive(n)))
print('반복적 방법의 팩토리얼 : {}'.format(factorial_iterative(n)))




