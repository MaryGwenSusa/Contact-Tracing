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
    personLog = input("Full Name (FN, MD, SN): ")
    vaccineStats = input("Did you have full dose of vaccine? (y/n) ").lower()
    if vaccineStats == 'yes':
        vaccineStats == 'Fully Vaccinated'

    nameKey = personLog[0]
    vaccineKey = vaccineStats[0]

    personsInContact[nameKey] = {vaccineKey}
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