print("Hello world")

#importing module
import ImportModule

#by making the entire command into a function I can repeat it at will when the user wants to make another search as many times as needed
def main():
    #re-assigning variables from module program
    phone_towing = ImportModule.Towing_Company
    phone_laundry = ImportModule.Laundry_Company
    phone_computer = ImportModule.Computer_Company
    phone_hardware = ImportModule.Hardware_Company
    phone_plumber = ImportModule.Plumber_Company

    #creating search database with user input and establishing the premise behind the program
    print("Our digitial phobnebook offers a library of phone numbers and services to its users!")
    print("""Search for one of our following services to continue: 
 - Towing Company, 
 - Laundry Company, 
 - Computer Company, 
 - Hardware Company, 
 - Plumbing Company""")
    #user types for the service they desire
    searcheng = input("Search:")
    #checks if the user input matches the databases options
    #if input has a match with library it prints a phone number
    #this is not the most efficient way too do this but its the easiest
    if searcheng == ("towing"):
        print("Phone number:", phone_towing)
    elif searcheng == ("towing company"):
        print("Phone number:", phone_towing)
    elif searcheng == ("laundry"):
        print("Phone number:", phone_laundry)
    elif searcheng == ("Laundry Company"):
        print("Phone number:", phone_laundry)
    elif searcheng == ("computer"):
        print("Phone number:", phone_computer)
    elif searcheng == ("Computer Company"):
        print("Phone number:", phone_computer)
    elif searcheng == ("hardware Company"):
        print("Phone number:", phone_hardware)
    elif searcheng == ("plumber"):
        print("Phone number:", phone_plumber)
    elif searcheng == ("hardware"):
        print("Phone number:", phone_hardware)
    elif searcheng == ("plumbing Company"):
        print("Phone number:", phone_plumber)
    else:
        print("this item is not available in our database")

#running the program initially
main()
#runs the program again if the user wants too, regardless of if the retrieve a phone number initially
pop = input("Would you like to make another search?")
if pop == ("yes"):
    main()
else: print("Thank you for using Digital Phonebook")
    
