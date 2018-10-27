# Wasting time. Loops and Flow practice

print ('Welcome to your own pet shop!\nYou can add pets and check for them later')
listchoice = []
while True:
    print ('Choose following:')
    print ('1. Enter your pet names')
    print ('2. Get The list of your pets')
    print ('3. check if the desired pet is in ur database')

    choice = input ()
    
    if int(choice) == 1:
        while True:
            print ('keep entering names. if you wanna stop just hit enter')
            name= input()
            if name == '':
                print ('Done taking inputs')
                break
            else:
                listchoice += [name] #listify the 'name' to type-match
    elif int(choice)== 2:
        if listchoice != []:
            for stuff in listchoice:
                print (stuff)
        else:
            print ('No Item There')
    elif int (choice) == 3:
        check = input ("Enter the pet name: ")
        if check in listchoice:
            print ('the pet is in there')
        else:
            print ('No such pets')
    else:
        print ('Wrong input')
        
