#code to input employee detail and print annual salary

name=input("enter the name of employee : ")
sal=float(input("enter the monthly salary : "))
empcd=input("enter the employee id : ")

print("Employee Name : ", name)
print("Employee Id : ", empcd)
print("Employee monthly Salary : ", sal)
print("Employee Annual Salary : ",(sal*12))
