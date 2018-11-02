pbook = {}       #phonebook dictionary practice

while True:
    print('PhoneBOOK APP!')
    print('1. See All entry')
    print('2. Check if an entry is there')
    print ('3. Enter new entry\n')

    choice = input("Type your choice: ")
    if choice == '1':
        if len(pbook) == 0:
            print('No entries yet\n')
        else:
            print(pbook)

    if choice == '2':
        check = input("Enter name to check: ")
        if check in pbook:
            print ('It is there and the number is '+ str(pbook[check]))
        else:
            print ('Entry not there\n')

    if choice == '3':
        name = input ("Contact Name: ")
        number = input("Contact Number: ")

        pbook[name] = number
        print('Successfully Saved!\n')
        
            
