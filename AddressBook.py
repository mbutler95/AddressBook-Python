import pickle
import os
class Contact:
    def __init__(self,ID,name,email,phone):
        self.ID=ID
        self.name=name
        self.email=email
        self.phone=phone
    def __str__(self):
         return "\nID:{0}\nName:{1}\nEmail address:{2}\nPhone:{3}\n".format(self.ID,self.name,self.email,self.phone)
    def change_name(self,name):
        self.name=name
    def change_email(self,email):
        self.email=email
    def change_phone(self,phone):
        self.phone=phone

def add_contact():
    address_book_file = ''
    try:
        address_book_file=open("address_book_file","rb")
    except FileNotFoundError:
        address_book_file=open("address_book_file","wb+")
    is_file_empty=os.path.getsize("address_book_file")<1
    if is_file_empty:
        list_contacts=[]
    else:
        list_contacts=pickle.load(address_book_file)
    try:
        contact=get_contact_info_from_user()
        address_book_file=open("address_book_file","wb")
        list_contacts.append(contact)
        pickle.dump(list_contacts,address_book_file)
        print("Contact added")
    except KeyboardInterrupt:
        print("Contact not added")
    except EOFError:
        print("Contact not added")
    finally:
         address_book_file.close()

def change_value():
    address_book_file=open("address_book_file","rb")
    is_file_empty=os.path.getsize("address_book_file")<1
    if is_file_empty:
        print("Address book is empty")
    else:
        list_contacts=pickle.load(address_book_file)
        change_target = input("Enter the name of the person to change the details of: ")
        change_condition = False
        for each_contact in list_contacts:
            while change_condition != True:
                if change_target == "Quit":
                    break
                elif change_target.lower() == each_contact.name.lower():
                    change_condition = True
                    print('\nEnter "Name", "Email" or "Phone" to select the detail to change')
                    choice = input("Enter your choice: ")
                    if choice== "Name":
                        Contact.change_name(each_contact, name=input("Enter name to change to: "))
                        address_book_file=open("address_book_file","wb")
                        pickle.dump(list_contacts,address_book_file)
                        return
                    elif choice== "Email":
                        Contact.change_email(each_contact, email=input("Enter email to change to: "))
                        address_book_file=open("address_book_file","wb")
                        pickle.dump(list_contacts,address_book_file)
                        return
                    elif choice== "Phone":
                        Contact.change_phone(each_contact, phone=input("Enter phone number to change to: "))
                        address_book_file=open("address_book_file","wb")
                        pickle.dump(list_contacts,address_book_file)
                        return
                else:
                    print("Name not found, please try again")
                    change_target = (input('Re-enter a name or type "Quit" to return to the main menu: '))
                    
    address_book_file.close()                       

def get_contact_info_from_user():
    address_book_file=open("address_book_file","rb")
    is_file_empty=os.path.getsize("address_book_file")<1
    if is_file_empty:
        list_contacts=[]
    else:
        list_contacts=pickle.load(address_book_file)
    try:
        contact_ID=len(list_contacts)+1
        contact_name=input("Enter contact name: ")
        contact_email=input("Enter contact email: ")
        contact_phone=input("Enter contact phone number: ")
        contact=Contact(contact_ID,contact_name,contact_email,contact_phone)
        return contact
    except EOFError as e:
        raise e
    except KeyboardInterrupt as e:
        raise e

def search_contact():
     address_book_file=open("address_book_file","rb")
     is_file_empty=os.path.getsize("address_book_file")<1
     if is_file_empty:
         print("Address book is empty")
     else:
         search_name=input("Enter the name: ")
         is_contact_found=False
         list_contacts=pickle.load(address_book_file)
         for each_contact in list_contacts:
             contact_name=each_contact.name
             search_name=search_name.lower()
             contact_name=contact_name.lower()
             if(contact_name==search_name):
                 print(each_contact)
                 is_contact_found=True
                 return 1
         if is_contact_found != True:
             print("No contact found with the search name")
     address_book_file.close()

def clear_file():
    address_book_file=open("address_book_file","wb")

def delete_file():
    os.remove("address_book_file")

def print_book():
     address_book_file=open("address_book_file","rb")
     is_file_empty=os.path.getsize("address_book_file")<1
     if is_file_empty:
         print("Address book is empty")
     else:
         list_contacts=pickle.load(address_book_file)
         for each_contact in list_contacts:
             print(each_contact)
     address_book_file.close()
     
def sort_entries():
    address_book_file=open("address_book_file","rb")
    is_file_empty=os.path.getsize("address_book_file")<1
    if is_file_empty:
        print("Address book is empty")
    else:
        list_contacts=pickle.load(address_book_file)
        list_contacts.sort(key=lambda x: x.name)
        address_book_file=open("address_book_file","wb")
        pickle.dump(list_contacts,address_book_file)
        for each_contact in list_contacts:
             print(each_contact, end="\n")
    address_book_file.close()


while True:
    print("\nMain Menu")
    print('Options : \n\
"Add" to add contact.\n\
"Change" to alter and existing contact.\n\
"Search" to search for a specific contact.\n\
"Print" to print contact list.\n\
"Sort" to sort contacts alphabetically.\n\
"Clear" to empty the contact list.\n\
"Quit" to exit the program.\n')
    choice=input("Enter your choice: ")
    if (choice.lower()=='quit'):
        break
    elif (choice.lower()=='add'):
        add_contact()
    elif (choice.lower()=='change'):
        change_value()
    elif (choice.lower()=='search'):
        search_contact()
    elif (choice.lower()=='clear'):
        clear_file()
    elif (choice.lower()=='delete'):
        delete_file()
    elif (choice.lower()=='print'):
        print_book()
    elif (choice.lower()=='sort'):
        sort_entries()
    else:
        print("Incorrect choice")
