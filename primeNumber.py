def prime_num(var):
    index=2
    isPrime='True'
    while(index<var):
        if(var%index==0):
            isPrime='False'
        index+=1
    
    return(isPrime)


num=int(input("enter the number to check if it is prime or not : "))

result=prime_num(num)

print(result)