import math
inp = input().split(" ")
x1,y1,r1 = float(inp[0]),float(inp[1]),abs(float(inp[2]))
x2,y2,r2 = float(inp[3]),float(inp[4]),abs(float(inp[5]))
if r1>0 and r2>0:
    x = abs(x1-x2)
    y = abs(y1-y2)
    c = math.sqrt((x**2)+(y**2))
    if x1==x2 and y1==y2 and c==0:
        if r1!=r2:
            print(0)
        else:
            print(-1)
    else:                                       
        if(c>(r1+r2)):
            print(0)
        elif(c==(r1+r2)):
            print(1)
        elif(abs(r1-r2)==c):
            print(1)
        elif(abs(r1-r2)>c):
            print(0)
        else:
            print(2)
else:
    print(0)