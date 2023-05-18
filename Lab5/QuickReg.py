import Registration as reg


class QuickReg(reg.Registration):

    def __init__(self, id, date, name, phone):
        super().__init__(id, date, name, phone)

    def print_info(self):
        print("------Quick Registration------")
        super().print_info_qr()
