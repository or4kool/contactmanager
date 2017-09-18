class ContactManager:
    def __init__(self, name="", phone_number="", email="", website="", b_day="", picture=""):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.website = website
        self.b_day = b_day
        self.picture = picture
        self.value = {}

    def create_contact(self):

        requests = ['Name', 'Phone Number', 'Email', 'Website', 'Birthday', 'Picture']
        for request in requests:
            self.value[request] = str(input("Please enter your {}: ".format(request)))

        print("""Thank you {Name}
        Your Phone Number is: {Phone Number}
        Your Email is: {Email}
        Your Website is: {Website}
        Your Birthday is: {Birthday}
        Your Picture address is: {Picture}
        """.format(**self.value))


contact_manager = ContactManager()
contact_manager.create_contact()
