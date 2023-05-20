import os
import time


# Tax computation function
def computeTax(salary):
    if salary > 8000000:
        tax = 2410000 + ((salary - 8000000) * .35)
    elif salary > 2000000:
        tax = 490000 + ((salary - 2000000) * .32)
    elif salary > 800000:
        tax = 130000 + ((salary - 800000) * .3)
    elif salary > 400000:
        tax = 30000 + ((salary - 400000) * .25)
    elif salary > 250000:
        tax =  (salary - 250000) * .2
    else:
        tax = 0
    return tax


# Program loop
responses = ('yes', 'y')
while True:
    # Name entry and validation
    while True:
        entry1 = input('Enter your full name (FN, LN): ')
        if entry1 != '':
            name = entry1
            break
        else:
            print("Do not leave the name blank")
            time.sleep(1)
            os.system('clear')
    # id number checking
    while True:
        entry2 = input('Enter your ID number: ')
        if entry2.isdigit():
            if int(entry2) > 10000000:
                # data validation
                id = int(entry2)
                break
            else:
                print("Invalid ID number")
                time.sleep(1)
                os.system('clear')
        else:
            print("Invalid ID number")
            time.sleep(1)
            os.system('clear')
    # email verification
    while True:
        entry3 = input('Enter email address: ')
        if '@' in entry3:
            email = entry3
            break
        else:
            print('Invalid email address')
            time.sleep(1)
            os.system('clear')

    # Input and checking of input
    while True:
        entry = input('Enter your annual salary: ')
        if entry.isdigit():
            if float(entry) > 0:
                # data validation
                salary = float(entry)
                break
            else:
                print("Invalid input")
                time.sleep(1)
                os.system('clear')
        else:
            print("Invalid input")
            time.sleep(1)
            os.system('clear')

    # output
    print('Name: {0}\nID: {1}'.format(name, id))
    print('Salary: P{0:.2f}\nTax: P{1:.2f}'.format(salary, computeTax(salary)))

    # continuation question
    cont = input('\nWould you like to continue? (y/n)\n')
    if cont not in responses:
        break


