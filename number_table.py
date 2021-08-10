num=int(input("rnter the number for which you want to display the table"))

counter=int(1)

while(counter<=10):
    print("{num}*{counter}={result}".format(num=num,counter=counter,result=int(num*counter)))
    counter=counter+1

print("table as above")