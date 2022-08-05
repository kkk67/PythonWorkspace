# 전공 수업과 비전공 수업 포함 6과목 수강가능
# 한 수업당 3학점

# 전공학점이 66학점 전체가 130점 이상이여야 졸업 가능

# 8학기 이내에 졸업이 가능한지

n,a,b = map(int,input().split())

list_x=[]
list_y=[]
cnt = 8-n
score =0

for i in range(10):
    x,y=map(int,input().split())
    list_x.append(x)
    list_y.append(y)

while True:
    if a>=66 and b>=130:
        print('Nice')
        break
    else:
        for i in range(cnt):
            a += list_x[i] * 3
            b += list_x[i] * 3
            score = 6- list_x[i]
            if score < list_y[i]:
                b += score * 3
            else:
                b += list_y[i] * 3
            score = 6
        if a >= 66 and b>=130:
            print('Nice')
            break
        else:
            print('Nae ga wae')
            break
      


    
    

            
            
    
    

    
    




