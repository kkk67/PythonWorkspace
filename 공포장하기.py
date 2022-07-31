r,g,b= map(int,input().split())
box=0

Min= min(r,g,b)
box = Min
r -= Min
g -= Min
b -= Min

box += r//3 + g//3 + b//3
r %= 3
g %= 3
b %= 3
if r == 2:
  box += 1
  r = 0
if g == 2:
  box += 1
  g = 0
if b == 2:
  box += 1
  b = 0

if r+g+b >0:
    box+=1

print(box)



        


