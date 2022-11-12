#Write a python program for contact tracing: 

#Allow user to select item in the menu (check if valid) 
def menuOption():
    #Display a menu of options 
    """
    Menu: 
        1 -> Log-in 
        2 -> Search 
        3 -> Exit (y/n)
    """

    personsInContact ={}
    personLog = input("Full Name (FN, MD, SN): ").title()

    try:
        age = int(input("Age: "))
    except ValueError:
        print('Please input your real age in number format.')
        age = int(input("Age: "))
        
    address = input("Address (House Number, Street, Barangay, Town/City, Province): ").title()
    
    try:
        contactNum = int(input('Contact Number: '))
    except ValueError:
        print('Please input your real contact number as we will uphold to the Data Privacy Act.')
        contactNum = int(input('Contact Number: '))





    vaccineStats = input("Did you have full dose of vaccine? (y/n) ").lower()
    if 'y' in vaccineStats:
        vaccineStats = 'Fully Vaccinated'
    else:
        vaccineStats = input("Did you only have first dose? (y/n) ").lower()
        if 'y' in vaccineStats:
            vaccineStats = '1st dose'
        else:
            vaccineStats = 'Unvaccinated'

    boosterStats = input("Did you have a booster? (y/n) ").lower()
    if 'y' in boosterStats:
        boosterStats = 'Yes'
    else:
        boosterStats = 'N/A'
       



    nameKey = personLog
    ageKey = age
    addressKey = address
    contactKey = contactNum
    vaccineKey = vaccineStats
    boosterKey = boosterStats

    personsInContact[nameKey] = {
        'Age': ageKey,
        'Address': addressKey,
        'Contact Number': contactKey,
        'Vaccine Status:': vaccineKey,
        'Booster': boosterKey
        
        
        
        }
    print(personsInContact)


print(menuOption.__doc__)
menuOption()


"""- Perform the selected option 
- Option 1: Ask personal data for contact tracing (Listed are sample only, add more) 
Use dictionary to store the info 
Use the full name as key 
The value is another dictionary of personal information 
- Option 2: Search, ask full name then display the record 
- Option 3: Ask the user if want to exit or retry. 
Menu: 1 -> Add an item 2 -> Search 3 -> Exit (y/n) 
What do you want to do? (1-3): 1 
Full name: Danilo Madrigalejos 
Age: 30 
Address: Eastwood 
Phone number: 1234567890 
Saved! 
What do you want to do? (1-3): 2 
Full name: Danilo Madrigalejos 
Age: 30 
Address: Eastwood 
Phone number: 1234567890 
What do you want to do? (1-3): 3 
Exit? n
"""