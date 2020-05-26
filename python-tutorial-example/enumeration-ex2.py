import emoji

cake_list=['Vanilla Cake','Butter Scotth Cake','Red Valvet Cake','Mango Cake','Orange Cake']
Pastry=['Strawberry Pastry','Vanilla Pastry','Simple Pastry','Onion Pastry']
Juice=['Vanilla Shake','Mango shake','strawberry shake','ras malai']

#all_item=cake_list

print('\n',"Welcome to CakeWala!!".center(30,'-'),"\n")

order=input("You want to order something? Yes=y, No=n ")

if order=='y':
    print("\nThis is the menu \n\nCakes-")
    for i, cakes in enumerate(cake_list, start=1):       
        print("%s. %s"%(i,cakes))
    print("\n\nPastries")
    for j, Pastries in enumerate(Pastry, start=1):
        print("%s. %s"%(j,Pastries))
    print("\n\nJuice")
    for k, Juices in enumerate(Juice, start=1):
        print("%s. %s"%(k,Juices))
elif order == 'n':
    exit()
else:
    print("\n\nInvalid option\n")
    order=input("You want to order something? Yes=y, No=n ")
    if order=='y':
        print("\nThis is the menu \n\nCakes-")
        for i, cakes in enumerate(cake_list, start=1):       
            print("%s. %s"%(i,cakes))
        print("\n\nPastries")
        for j, Pastries in enumerate(Pastry, start=1):
            print("%s. %s"%(j,Pastries))
        print("\n\nJuice")
        for k, Juices in enumerate(Juice, start=1):
             print("%s. %s"%(k,Juices))
    elif order =='n':
        exit()
    else:
        print("maximum retries over. Thank You for visiting the CakeWala!! ")
        exit()

order=[order for order in input("\n\nWhat you want to order, comma (,) seperated): ").split(",")]



All_items=cake_list+Pastry+Juice


if order[0:] in All_items:
    print("Your order %s is ready, Please help yourself"%order)



else:
    print("Invalid Item. Please go your home and cook yourself",emoji.emojize(":winking_face_with_tongue:") *10)

    