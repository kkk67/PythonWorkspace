data = input()

row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) +1


steps=[(-2,-1),(-1,-2),(1,2),(2,1),(-1,2),(1,-2),(-2,1),(2,-1)]
print('row = {} column = {} '.format(row,column))

result=0
for step in steps:
    next_row=row + step[0]
    next_column=column+step[1]
    print('next_low= {} next_column = {}'.format(next_row,next_column))
    if next_row >= 1 and next_column >= 1 and next_column <= 8 and next_row <= 8:
        result+=1

print(result)