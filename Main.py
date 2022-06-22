import random
import time

a=[74,65,55,45,40,35,30,25,20,19,18,17,16,15,14,13,12,11,10,9]

b=[random.randint(0,0) for i in range(100)]

def createRandom(num,oop=0):
    
    c=[0 for i in range(100-(a[num]+oop))]+[1 for i in range((a[num]+oop))]
    random.shuffle(c)
    #print('percent:',(a[num]+oop),'List:',c,'list.count=',c.count(1))
    return c

def GetResult(c):
    d=random.randrange(0,100)
    return c[d]
m=0
n=0
x=0
temp=0
while m<1000 and x<20:
    
    n=GetResult(createRandom(x))
    if n==1:
        x+=1
        print('times ',m," Success! CurrentLevel:",x)
        
    else:
        x=0
        
        if x<0:
            x=0
        print('times ',m," Failed! CurrentLevel:",x)
            
    temp=x if x>temp else temp
    m=m+1
    time.sleep(0)
    

print('top Level:',temp)
    
