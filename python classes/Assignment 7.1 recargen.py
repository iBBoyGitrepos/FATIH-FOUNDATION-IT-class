#  recargen
def a(x):
    if x < 5: #<-1<-2,<-3,<-4,<-5
        res = a(x+1) 
        print(res)
        return res
    else: 
        return x
    
a(1)