   ### FIRST SOLUTION  ###

def phonebook(deger):

    match int(str(deger)) :
        case 1:
            x = input("Find the phone number of : ")
            if x in rehber:
                print(rehber[x])
            else: print(f"Couldn't find phone number of {x}")
        case 2:
            a = input("Insert name of the person : ")
            b = input("Insert phone number of the person:")
            if not b.isdigit():
              print ("Invalid input format, cancelling operation ...")
              return 
            rehber[a] = b
            print(rehber)
            print(f"Phone number of {a} is inserted into the phonebook")
        case 3:
            x = input("Whom to delete from phonebook : ")
            del rehber[x]
            print(rehber)
            print(f"{x} is deleted from the phonebook")
        case 4:
          print('Exiting Phonebook')
          exit()
rehber = {}
while True:
    try:
        deger = int(input("Welcome to the phonebook application \
         \n 1. Find phone number \
         \n 2. Insert a phone number \
         \n 3. Delete a person from the phonebook \
         \n 4. Terminate \
         \n Select operation on Phonebook App (1/2/3) :" ))    
        phonebook(deger)
    except ValueError:
         print("Enter a number 1 ,2, 3, 4 ")
         continue

       
                ### SECOND SOLUTION  ###

phonebook = {}

def find(keyword):
    return phonebook.get(keyword, f"Couldn't find phone number of {keyword}")

def add(name, phone_number):
    phonebook[name] = phone_number
    return f'Phone number of {name} is inserted into the phonebook'

def delete(name):
    try:
        phonebook.pop(name)
    except KeyError as err:
        return f'{err} is not in the phonebook'
    else:
        return f'{name} is deleted from the phonebook'

if __name__ == '__main__':
    print('Welcome to the phonebook application')
    print('1. Find phone number')
    print('2. Insert a phone number')
    print('3. Delete a person from the phonebook')
    print('4. Terminate')
    no = input('Select operation on Phonebook App (1/2/3) : ')
    while True:
        if no == '1':
            name = input('Find the phone number of : ')
            print(find(name))
            print(" ")
        elif no == '2':
            name = input('Insert name of the person : ')
            try:
                number = int(input('Insert phone number of the person: '))
            except ValueError as err:
                print('Invalid input format, cancelling operation ...')
            else:
                print(add(name, number))
            print(" ")
        elif no == '3':
            name = input('Whom to delete from phonebook : ')
            print(delete(name))
            print(" ")
        elif no == '4':
            print('Exiting Phonebook')
            break
        else:
            print('Wrong operation')

        print('1. Find phone number')
        print('2. Insert a phone number')
        print('3. Delete a person from the phonebook')
        print('4. Terminate')
        no = input('Select operation on Phonebook App (1/2/3) : ')




















# Welcome to the phonebook application
# 1. Find phone number
# 2. Insert a phone number
# 3. Delete a person from the phonebook
# 4. Terminate
# Select operation on Phonebook App (1/2/3) : 2
# Insert name of the person : John
# Insert phone number of the person: ten
# Invalid input format, cancelling operation ...

# 1. Find phone number
# 2. Insert a phone number
# 3. Delete a person from the phonebook
# 4. Terminate
# Select operation on Phonebook App (1/2/3) : 2
# Insert name of the person : Alex
# Insert phone number of the person: 1234
# Phone number of Alex is inserted into the phonebook

# 1. Find phone number
# 2. Insert a phone number
# 3. Delete a person from the phonebook
# 4. Terminate
# Select operation on Phonebook App (1/2/3) : 1
# Find the phone number of : Alex
# 1234

# 1. Find phone number
# 2. Insert a phone number
# 3. Delete a person from the phonebook
# 4. Terminate
# Select operation on Phonebook App (1/2/3) : 3
# Whom to delete from phonebook : Alex
# Alex is deleted from the phonebook

# 1. Find phone number
# 2. Insert a phone number
# 3. Delete a person from the phonebook
# 4. Terminate
# Select operation on Phonebook App (1/2/3) : 1
# Find the phone number of : Alex
# Couldn't find phone number of Alex

# 1. Find phone number
# 2. Insert a phone number
# 3. Delete a person from the phonebook
# 4. Terminate
# Select operation on Phonebook App (1/2/3) : 4
# Exiting Phonebook