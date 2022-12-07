for  _ in range(int(input())):
    n,x1,y1,x2,y2=map(int,input().split())
    offgridcost=min(min((n+1-y1),y1),min((n+1-x1),x1))+min(min((n+1-x2),x2),min((n+1-y2),y2))
    ingridcost=abs(x1-x2)+abs(y1-y2)
    print(min(offgridcost,ingridcost))