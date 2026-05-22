contacts = {}

def add_contact():
    name = input("Enter the Contact Name : ")
    number = input("Enter the Contact Person : ")

    contacts[name] = number
    print("Contact Added Successfully")

def show_contact():
    if len(contacts) == 0:
        print("No Contatcs Found")
    else:
        print("Contact List")

        for name, number in contacts.items():
            print(name , ":" , number)
    
def search_contact():
    search_name = input("Enter The Contact Person : ")  
    
    if search_name in contacts:
        print("Contact Found")
        print(search_name , ":" , contacts[search_name]) 

    else:
        print("Contact Not Found")    

def delete_contact():
    dlt_contact = input("Enter Contact Want to Delete : ")

    if dlt_contact in contacts:
        del contacts[dlt_contact]
        print("Contacts Deleted")
    else:
        print("Contacts not Found")
    
while True:
    print("Contact Book System")
    print("1. Add Contact")
    print("2 . Show Contact")
    print("3 . Search Contact")
    print("4 . Delete Contact")
    print("5 . Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        add_contact()
    
    elif choice == "2":
        show_contact()

    elif choice == "3":
        search_contact()
    
    elif choice == "4":
        delete_contact()
    
    elif choice == "5":
        print("Exit....")
        break

    else:
        print("Invalid Choice")





contacts = {}

def add_contact():
    name = input("Enter the Contact Person : ")
    number = input("Enter the Contact Number : ")

    contacts[name] = number
    print("Contact Added Successfully")

def show_contact():
    if len(contacts) == 0:
        print("No Contacts Found")
    else:
        print("Contacts Found")
    
    for name , number in contacts.items():
        print(name , ":" , number)

def search_contact():
    search_name = input("Enter the Search Person : ")

    if search_name in contacts:
        print("Contacts Searched")
        print(search_name , ":" , contacts[search_name])
    else:
        print("Not Found")

def delete_contact():
    dlt_name = input("Enter the Contact Delete : ")

    if dlt_name in contacts:
        del contacts[dlt_name]
        print("Contact Deleted")
    else:
        print("No Contacts Found")
    
while True:
    print("Contacts List Found")
    print("1 . Add Contact")
    print("2 . Show Contact")
    print("3 . Search Contact")
    print("4 . Delete Contact")
    print("5 . Exit...")

    choice = input("Enter Choice Number (1 - 5) : ")

    if choice == "1":
        add_contact()
    
    elif choice == "2":
        show_contact()
    
    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()
    
    elif choice == "5":
        print("Exit...")
        break

    else:
        print("Invalid Choice : ")
