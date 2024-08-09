class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact.name or query in contact.phone]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}\n")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print("Enter new details (leave blank to keep current value):")
                new_name = input("Name: ") or contact.name
                new_phone = input("Phone: ") or contact.phone
                new_email = input("Email: ") or contact.email
                new_address = input("Address: ") or contact.address
                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print("Contact updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            contact_book.update_contact(name)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
