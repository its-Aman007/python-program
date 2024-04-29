## time complexity is calculated by  (time= a*n + b)

def work(num):
        a=[]
        for n in num:
                a.append(n*n)
        return a
num=[2,3,4,5]
x=work(num)
print(x)
##  its Time complexity is O(n)

def word(noun,pronoun,pos):
        k=noun[pos]/pronoun[pos]
        return k
 ## here k will always show constant function, its time comp.. is O(1)


num=[1,2,3,5,1,3,2,6,4,3]
for i in range(len(num)):
        for j in range(i+1,len(num)):
                if num [i]== num[j]:
                        print(num [i] , "is a duplicate")
                        
## here for loop runs for 2 times, means time comp.. is O(n^2) time = a * n^2 + b.






