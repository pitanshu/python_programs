
while True:
    
    var=str(input("enter the message to be printed : \n"))

    if (len(var)==0):
        break

    if (var[0]=='#'):
        continue

    print("message = ",var)

    

print("Done")

