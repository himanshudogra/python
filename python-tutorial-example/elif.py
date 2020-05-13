name=input('Hello Sir, Please enter your name: ')

calculator=input("Are you here to calculate something, Enter yes or no: ")

if calculator == 'yes':
    print('ok, please Enter the below values')
else:
    exit

val1=int(input("Value1: "))
val2=int(input("Value2: "))
operation=input("Provide the operation value ex: add, subs, multiply, divide: ")

if operation == "add":
    print("Result: ",val1 + val2)
elif operation == "subs":
    print("Result: ", val1-val2)
elif operation == "multiply":
    print("Result: ", val1 * val2)
elif operation == "divide":
    print("Result: ",val1 / val2)
else:
    print(name, "!!GANND Mara!!")