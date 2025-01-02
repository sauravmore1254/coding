class ContactManager:
    def __init__(self):
        # Initialize an empty list to store contacts
        self.contacts = []

    def add_contact(self):
        # Collect contact details from the user
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()
        
        # Add the contact to the list
        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        print(f"Contact {name} added successfully!\n")

    def view_contacts(self):
        # Display all saved contacts
        if not self.contacts:
            print("No contacts found.\n")
            return

        print("Contact List:")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
        print()

    def search_contact(self):
        # Search for a contact by name or phone number
        query = input("Enter name or phone number to search: ").strip()
        results = [contact for contact in self.contacts if query in contact['name'] or query in contact['phone']]

        if not results:
            print("No contacts found matching your query.\n")
            return

        print("Search Results:")
        for contact in results:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")

    def update_contact(self):
        # Update details of an existing contact
        query = input("Enter name or phone number of the contact to update: ").strip()
        for contact in self.contacts:
            if query == contact['name'] or query == contact['phone']:
                print("Current Details:")
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")

                # Allow the user to update fields, keeping current values if blank
                contact['name'] = input("Enter new name (leave blank to keep current): ") or contact['name']
                contact['phone'] = input("Enter new phone (leave blank to keep current): ") or contact['phone']
                contact['email'] = input("Enter new email (leave blank to keep current): ") or contact['email']
                contact['address'] = input("Enter new address (leave blank to keep current): ") or contact['address']
                
                print("Contact updated successfully!\n")
                return

        print("No contact found with the given details.\n")

    def delete_contact(self):
        # Delete a contact by name or phone number
        query = input("Enter name or phone number of the contact to delete: ").strip()
        for i, contact in enumerate(self.contacts):
            if query == contact['name'] or query == contact['phone']:
                confirm = input(f"Are you sure you want to delete {contact['name']}? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    self.contacts.pop(i)  # Remove the contact from the list
                    print("Contact deleted successfully!\n")
                else:
                    print("Deletion canceled.\n")
                return

        print("No contact found with the given details.\n")

    def menu(self):
        # Display the menu and handle user choices
        while True:
            print("--- Contact Manager ---")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            # Map user input to corresponding actions
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

# Entry point for the program
if __name__ == "__main__":
    manager = ContactManager()
    manager.menu()
