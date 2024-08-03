#Task-05 : this project is all about creating a contact book using python. Which will store name, address, phone number and email-id of contacts. The user can view contact, search contact, add contact, update contact as well as delete contact through this contact book 



def add_contact(contact_book, name, address, phone, email):
    contact_book[name] = {
        "address": address,
        "phone": phone,
        "email": email
    }
    print(f"Contact '{name}' added.")

def update_contact(contact_book, name, address=None, phone=None, email=None):
    if name in contact_book:
        if address:
            contact_book[name]['address'] = address
        if phone:
            contact_book[name]['phone'] = phone
        if email:
            contact_book[name]['email'] = email
        print(f"Contact '{name}' updated.")
    else:
        print(f"Contact with name '{name}' not found.")

def delete_contact(contact_book, name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact with name '{name}' not found.")

def view_contact(contact_book, name):
    if name in contact_book:
        contact = contact_book[name]
        print(f"Name: {name}, Address: {contact['address']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print(f"Contact with name '{name}' not found.")

def search_contacts(contact_book, search_term):
    found = False
    for name, contact in contact_book.items():
        if search_term.lower() in name.lower() or search_term.lower() in contact['email'].lower():
            print(f"Name: {name}, Address: {contact['address']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
    if not found:
        print(f"No contact found with search term: {search_term}")

def view_all_contacts(contact_book):
    if contact_book:
        for name, contact in contact_book.items():
            print(f"Name: {name}, Address: {contact['address']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts available.")

# Main function to run the program

def main():
    contact_book = {}

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. View Contact")
        print("5. Search Contacts")
        print("6. View All Contacts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            email = input("Enter email ID: ")
            add_contact(contact_book, name, address, phone, email)
        elif choice == '2':
            name = input("Enter the name of the contact to update: ")
            new_address = input("Enter new address (leave blank to keep unchanged): ")
            new_phone = input("Enter new phone number (leave blank to keep unchanged): ")
            new_email = input("Enter new email ID (leave blank to keep unchanged): ")
            update_contact(contact_book, name, address=new_address, phone=new_phone, email=new_email)
        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(contact_book, name)
        elif choice == '4':
            name = input("Enter the name of the contact to view: ")
            view_contact(contact_book, name)
        elif choice == '5':
            search_term = input("Enter name or email to search: ")
            search_contacts(contact_book, search_term)
        elif choice == '6':
            view_all_contacts(contact_book)
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
