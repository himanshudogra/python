cake_list=['Butter Scotch','Vanilla','red valvet']

print("Hi, Thank you visiting our HAPPY shop!!\n")

menu_option=input('How can we help you? Do you want the menu, Yes=y No=n ')

if menu_option=='y':
    print('We have below items in cake currently available.\n')
    for item in cake_list:
         print(item.center(5,' '))
         
print('\n')

while True:

    choice=input("Kindly Choose your order: " )

    if choice in cake_list:
        print("Your order no. is 1. Please collect it from the counter.\n")
        cake_list.remove(cake_list[0])
        0==0 

    elif choice in cake_list:
        print("Your order no. is 2. Please collect it from the counter.\n")
        cake_list.remove(cake_list[1])
        0==0

    elif choice in cake_list:
        print("Your order no. is 3. Please collect it from the counter.\n")
        cake_list.remove(cake_list[2])
        0==0

    else: 
        print("Sorry! The requested item is out of stock.\n")
        0==0