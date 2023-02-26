s=int(input("size:"))
# st=s*s
# s=s**s
# print(st)
# print(s)
a=[None]*s
# function
def max(a):   
    for i in range(0,s):
        a[i]=int(input("data:"))
    max=a[0]
    for i in range(1,s):
        if a[i]>=max:
            max=a[i]
    print(max)
max(a) #you must call function

# switch case
def number(argument):
    match argument:
        case 0:
            print("zero")
        case 1:
            print( "fine")
        case 3:
            print( "terminal")

argument=0
number(argument)

#while
count=0
while(count<5):
    print("hello",count)
    count+=1


#class 
class stack():
    def __init__(self,size):
        self.top=-1
        self.size=size
        self.a=[None]*size
    def isempt(self):
        if self.top==-1:
            return True
        else:
            return False
    def isfull(self):
        if self.top== self.size:
            return True
        else:
            return False
    
    def pop(self):
        if self.isempt()==False:
            print( self.a[self.top])
            self.top-=1
    def push(self,x):
        if self.isfull()==False:
            self.top+=1
            self.a[self.top]=x
            print("succseeeflkf!")
            

s=stack(4)
s.push(3)
s.push(4)
s.push(5)
s.pop()
