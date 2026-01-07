class Contact_List:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact_obj):
        self.contacts.append(contact_obj)

    def display_contacts(self):
        print("Contact List:")
        print(f"{'Name':<15} {'Email':<20} {'Telephone':<15}")
        print("-" * 50)
        for contact in self.contacts:
            print(f"{contact.name:<15} {contact.email:<20} {contact.telephone:<15}")