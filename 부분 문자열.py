while True:
    try:

        str = input().split()

        s= str[0]
        t= str[1]

        correct=0
        value=0

        for i in range(len(t)):
            if t[i] == s[value]:
                value +=1
                if value == len(s):
                    correct=1
                    break

        if correct == 1:
            print('Yes')
        else:
            print('No')
    except:
        break