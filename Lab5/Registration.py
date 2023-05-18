class Registration:
    id = None
    date = None
    name = None
    phone = None

    def __init__(self, id, date, name, phone):
        self.id = id
        self.date = date
        self.name = name
        self.phone = phone

    def print_info(self):
        print("id = {0}\ndate = {1}\nname = {2}\nphone = {3}".format(self.id, self.date, self.name, self.phone))

    def print_info_qr(self):
        print("name = {0}\nphone = {1}".format(self.name, self.phone))
