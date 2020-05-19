cake_list=['Butter Scotch','Vanilla','red valvet']

print("Hi, Thank you visiting our shop!!")

print("Below options are currently available")

for item in cake_list:
    print(item)

while True:

    choice=input("Kindly Choose your order: " )

    if choice == cake_list[0]:
        print("Your order no. is 1. Please collect it from the counter.")
        cake_list.remove(cake_list[0])
        exit 

    elif choice == cake_list[1]:
        print("Your order no. is 2. Please collect it from the counter.")
        cake_list.remove(cake_list[1])
        exit

    elif choice == cake_list[2]:
        print("Your order no. is 3. Please collect it from the counter.")
        cake_list.remove(cake_list[2])
        exit

    else: 
        print("Sorry! The requested item is out of stock.")
        0==0