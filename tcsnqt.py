dire=[10,20,30,40]
n=int(input())
cox=coy=0 
for i in range(n):
    if(i%4==1):#right
        cox+=dire[i%4]
        dire[i%4]+=40
    elif(i%4==2):#upper
        coy+=dire[i%4]
        dire[i%4]+=40
    elif(i%4==3):#left
        cox-=dire[i%4]
        dire[i%4]+=40
    elif(i%4==0):#down
        coy-=dire[i%4]
        dire[i%4]+=40
print(cox,coy)