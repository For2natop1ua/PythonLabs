import Registration as reg


class DesktopReg(reg.Registration):
    administrator = None

    def __init__(self, id, date, name, phone, administrator):
        super().__init__(id, date, name, phone)
        self.administrator = administrator

    def print_info(self):
        print("------Desktop Registration------")
        super().print_info()
        print("Administrator: {}".format(self.administrator))
