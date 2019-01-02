##fibonacci = 1,1,2,3,5,8,13,21,33,54........

##empty dictionary
fibonacci_stored={}

def fibonacci(x):
    ##if value is already stored, return it
    if x in fibonacci_stored:
        return fibonacci_stored[x]
    
    ##if number is position 1 or 2
    if x==1 or x==2:
        value=1
##    elif x==2:
##        value = 1
    ##else
    elif x>2:
        value = fibonacci(x-1)+fibonacci(x-2)
##store and call the value
    fibonacci_stored[x]=value
    return value

for x in range(1,51):
    print(x,'-',fibonacci(x))
