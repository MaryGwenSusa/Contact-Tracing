#Write a python program for contact tracing: 

def logIn():
    #Display a menu of options 
    """
    Menu: 
        1 -> Log-in 
        2 -> Search 
        3 -> Exit (y/n)
    """
    log = int(input('Enter the number of people to log: '))
    for num in range(0,log):
    #Ask personal data for contact tracing 
        personsInContact ={}
        personLog = input("Full Name (FN, MD, SN): ").title()

        try:
            age = int(input("Age: "))
        except ValueError:
            print('Please input your real age in number format.')
            age = int(input("Age: "))
            
        address = input("Address (House Number, Street, Barangay, Town/City, Province): ").title()
        
        try:
            contactNum = input('Contact Number: ')
        except ValueError:
            print('PLease input your real contact number as we will uphold the Data Privacy Act.')
            contactNum = input('Contact Number: ')

        vaccineStats = input("Did you have full dose of vaccine? (y/n) ").lower()
        if 'y' in vaccineStats:
            vaccineStats = 'Fully Vaccinated'
        else:
            vaccineStats = input("Did you only have first dose? (y/n) ").lower()
            if 'y' in vaccineStats:
                vaccineStats = '1st dose'
            else:
                vaccineStats = 'Unvaccinated'


       
        nameKey = personLog
        ageKey = age
        addressKey = address
        contactKey = contactNum
        vaccineKey = vaccineStats


        #Use dictionary to store the info 
        personsInContact[nameKey] = {
            'Age': ageKey,
            'Address': addressKey,
            'Contact Number': contactKey,
            'Vaccine Status:': vaccineKey,


            }
            
    print('Saved!')
    searchLogs = input('Do you want to search a suspected/positive individual in the directory? (y/n) ')
    if 'y' in searchLogs:
        for pName, pInfoDict in personsInContact.items():
            print('\nFull name:', pName)

            for key in pInfoDict:
                print(key + ':', pInfoDict[key])
    else:
        exit()


def menuOption():
    #Display a menu of options 
    """
    Menu: 
        1 -> Log-in 
        2 -> Search 
        3 -> Exit (y/n)
    """
    #Allow user to select item in the menu (check if valid)
    try:
        userTask = int(input('What do you want to do? '))
    except ValueError:
        print('Please enter only any of the given menu options.')
    if userTask == 1:
        logIn()
    elif userTask == 2:
        print('Add logs first. Directory(dict) is currently empty.')
        logIn()
    elif userTask == 3:
        confirmation = input('Are you sure you want to exit? (y/n) ')
        if 'y' in confirmation:
            exit()
        else:
            menuOption()

        
print(menuOption.__doc__)
menuOption()