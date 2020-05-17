Are_You_Hungry=True

while Are_You_Hungry:
    Answer=input("Bhook lagi h beta? (y=yes, n=no) ")
    if Answer == 'y':
        print("Ye lo cookies kha lo.")

        Are_You_Hungry=True
        while Are_You_Hungry:
            Answer=input("Or bhookh lagi h? (y=yes, n=no) ")
            if Answer == 'y':
                print("Ok, to ye lo bread kha lo.")
                
                Are_You_Hungry=True
                while Are_You_Hungry:
                    Answer=input("Abhi bhi bhook lagi h kya? (y=yes, n=no) ")
                    if Answer=='y':
                        print("Ye lo cake khao - fruity piyo or apni bhookh mitao")
                        Are_You_Hungry=False
                    else:
                        print("To jao fir so jao yaha kya kre ho, or logo ko aane do jinko bhook lagi h.")
                        Are_You_Hungry=False
            else:
                print("To jao fir so jao yaha kya kre ho, or logo ko aane do jinko bhook lagi h.")
                Are_You_Hungry=False
    elif Answer == 'n':
        Are_You_Hungry=False
        print("To jao fir so jao yaha kya kre ho, or logo ko aane do jinko bhook lagi h.")
    else:
        print("Yaha time pass ku kre ho beta thodi padai kr lo apke hi kam aayegi.")
        Are_You_Hungry=False