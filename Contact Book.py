# Contact Management System

# List to store contacts as dictionaries
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    # Store contact details in a dictionary
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(f"Contact for {name} added successfully.\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts available.\n")
        return
    
    print("Contact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter name or phone number to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    if found_contacts:
        print("Search Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
    else:
        print("No contacts found.\n")

# Function to update a contact
def update_contact():
    search_term = input("Enter name or phone number of the contact to update: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            print(f"Updating contact for {contact['name']}")
            contact['name'] = input("Enter new name: ")
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print(f"Contact updated successfully.\n")
            return
    print("No contact found with that name or phone number.\n")

# Function to delete a contact
def delete_contact():
    search_term = input("Enter name or phone number of the contact to delete: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            contacts.remove(contact)
            print(f"Contact for {contact['name']} deleted successfully.\n")
            return
    print("No contact found with that name or phone number.\n")

# Function to display the menu and handle user input
def contact_manager():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the contact manager
if __name__ == "__main__":
    contact_manager()
