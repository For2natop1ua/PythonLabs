import Registration as reg


class WebReg(reg.Registration):
    browser = None
    ipAddress = None

    def __init__(self, id, date, name, phone, browser, ipAddress):
        super().__init__(id, date, name, phone)
        self.browser = browser
        self.ipAddress = ipAddress

    def print_info(self):
        print("------Web Registration------")
        super().print_info()
        print("Browser: {0}\nIP_address: {1}".format(self.browser, self.ipAddress))
