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
        # self.all_contact = self.read_csv()

    def add_contact(self, contact):

        self.all_contact.append(contact)

        # print(self.all_contact)
        print("\n --Contact Successfully Added--")

    def collect_contact(self):
        self.value = {}
        print("\nPlease enter a new contact")
        requests = ['Name', 'Phone Number', 'Email', 'Website', 'Birthday', 'Picture']
        for request in requests:
            self.value[request] = str(input("Please enter your {}: ".format(request)))
        # self.add_contact(self.value)
        self.write_csv(self.value)

    # Read all contacts from csv file
    def read_csv(self):
        with open('csv-contact.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            contact_file = filter(lambda data: data, csv_reader)
            all_contact_file = list(contact_file)
        return all_contact_file

    def write_csv(self, contacts):
        # num =0
        with open('csv-contact.csv', 'a') as csv_writer:
            header_name = ['Name', 'Phone Number', 'Email', 'Website', 'Birthday', 'Picture']
            csv_write_data = csv.DictWriter(csv_writer, fieldnames=header_name)

            csv_write_data.writerow(contacts)

    def delete_contact(self, contact_name):
        # Delete a contact by name
        contacts = self.get_contact()
        for index, name in enumerate(contacts):
            if contact_name == name['Name']:
                contacts.pop(index)
                print("\n --Successful removed contact--")
                break
        else:
            print("\n **Please brother what is your problem!**")

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
            print("\n **Please brother what are you looking for!**")

    def get_contact(self):
        csv_data = self.read_csv()
        if csv_data:
            self.all_contact = csv_data
        else:
            print("\n **No Contact to show you**")
        return self.all_contact

    def display_all_contact(self):
        # print("YO")
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
                print("\n **Invalid enter a valid option**")

contact_manager = ContactManager()
contact_manager.gensis()
# contact_manager.write_csv({'Name': 'Ndi', 'Phone Number': '12', 'Email': 'ii@gmail.com', 'Website': 'ii.com', 'Birthday': '00', 'Picture': 'rr.png'})

