import csv


class ContactManager:
    def __init__(self, name="", phone_number="", email="", website="", b_day="", picture=""):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.website = website
        self.b_day = b_day
        self.picture = picture
        self.value = {}
        self.all_contact = []

    def add_contact(self, contact={}):

        self.all_contact.append(contact)

        print("\n")
        print(self.all_contact)

    def collect_contact(self):
        self.value = {}
        print("\nPlease enter a new contact")
        requests = ['Name', 'Phone Number', 'Email', 'Website', 'Birthday', 'Picture']
        for request in requests:
            self.value[request] = str(input("Please enter your {}: ".format(request)))
        self.add_contact(self.value)

    def delete_contact(self, contact_name):
        # Delete a contact by name
        contacts = self.get_contact()
        for index, name in enumerate(contacts):
            if contact_name == name['Name']:
                contacts.pop(index)
                print("\n Successful removed contact")
                break
        else:
            print("\nPlease brother what is your problem!")

    def search_contact(self, contact_name):
        contacts = self.get_contact()
        for index, name in enumerate(contacts):
            if contact_name == name['Name']:
                print("""
 This is the contact you want:
 Name: {Name}
 Phone Number:{Phone Number}
 Email: {Email}
 Website: {Website}
 Birthday:{Birthday}
 Picture:{Picture}
 """.format(**name))
                break
        else:
            print("\nPlease brother what are you looking for!")

    def get_contact(self):
        return self.all_contact

    def display_all_contact(self):
        every_contact = self.get_contact()
        for contact in every_contact:
            print("""
 Name: {Name}
 Phone Number: {Phone Number}
 Email: {Email}
 Website: {Website}
 Birthday: {Birthday}
 picture: {Picture}
            """.format(**contact))
            print("=" * 40)

    def gensis(self):

        user_selected = ""

        while user_selected is not 'Q':

            print("""
 A. Add Contact
 B. Delete Contact
 C. Search Contact
 D. Show All Contact
 Q. Quit
 """)

            user_selected = str(input("Please Select the Value you want btw A, B, C, D, Q:")).upper()

            if user_selected == "A":
                # contact_name = str(input("Please Enter a contact name to search f"))
                self.collect_contact()
            elif user_selected == "B":
                contact_name = str(input("\nPlease enter a contact name to delete: "))
                self.delete_contact(contact_name)
            elif user_selected == "C":
                contact_name = str(input("\nPlease enter a contact name you want: "))
                self.search_contact(contact_name)
            elif user_selected == "D":
                print("All Contacts:")
                self.display_all_contact()
            elif user_selected == "Q":
                break
            else:
                print("\nPlease enter a valid option")

contact_manager = ContactManager()
contact_manager.gensis()
