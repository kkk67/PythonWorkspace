n,m,k = map(int,input().split()) # n은 배열의 크기, m은 더하는 횟수,k는 같은 인덱스의 값을 더할 수 있는 최대 횟수

array= list(map(int,input().split())) # 입력이 n=5 m=8 k=3 배열은 2 4 5 4 6이 들어왔을시
array.sort()

first=array[-1]
second=array[-2]

count = int((m/(k+1))*k) # 가장 큰 수가 더해지는 횟수
count += m % (k+1) # 나머지 나눠지지 않는 값 더하기

result=0
result += (count) * first # 가장 큰 수
result += (m-count) * second # 두번 째로 큰 수

print(result) # 46 출력