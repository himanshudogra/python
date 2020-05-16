from collections import namedtuple

employee_record = namedtuple ("employee","Name,Dept,Desig,exp")

print("-"*15,"Please enter below details","-"*15)

Name=input("Name: ");Department=input("Department: ");Designation=input("Designation: ");experience=input("Experience in yr: ")

detail=employee_record(Name,Department,Designation,experience)

print("\n")
print("-"*15,"Employee Details:","-"*15)


print("Name =",detail[0])
print("Department =",detail[1])
print("Designation =",detail[2])
print("experience =",detail[3])


#print("Here is the employee detail:")

#print("Name: ",detail.Name)
#print("Department: ",detail.Dept)
#print("Designation: ",detail.Designation)
#print("Overall Experience: ",detail.exp)